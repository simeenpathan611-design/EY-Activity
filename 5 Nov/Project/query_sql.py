import os
import sqlite3
import pandas as pd
import re
from openai import AzureOpenAI
from dotenv import load_dotenv
import chromadb

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION")
)

# Get deployment names
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
embedding_model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")

def ask_query(context):
    question = context["question"]
    db_path = context["db_path"]

    # Initialize ChromaDB client
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection("excel_schema")

    # Create embedding for the question
    emb = client.embeddings.create(model=embedding_model, input=question).data[0].embedding
    results = collection.query(query_embeddings=[emb], n_results=5)
    semantic_context = "\n".join(results["documents"][0]) if results["documents"] else ""

    # Connect to SQLite DB and extract schema
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = ""
    for (table,) in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        cols = cursor.fetchall()
        schema += f"\nTable {table}: {[col[1] for col in cols]}"

    # Construct prompt for SQL generation
    prompt = f"""
    You are an expert data analyst.
    Use the schema and semantic context to generate a correct SQL query for the question below.

    Note: The database is SQLite. Do not use MySQL-specific syntax like SHOW COLUMNS.

    SCHEMA:
    {schema}

    CONTEXT:
    {semantic_context}

    QUESTION:
    {question}

    Return only the SQL query.
    """

    # Get SQL query from OpenAI
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    # Clean SQL query (remove markdown formatting)
    sql_query = response.choices[0].message.content.strip()
    sql_query = re.sub(r"^```sql\s*|\s*```$", "", sql_query.strip(), flags=re.IGNORECASE)

    print("\nGenerated SQL:\n", sql_query)

    # Execute SQL query
    try:
        if not sql_query.lower().startswith(("select", "show", "pragma")):
            raise ValueError("Generated SQL query is not valid or safe to execute.")

        df = pd.read_sql_query(sql_query, conn)
        print("Query Result:\n", df)
        context["result"] = df.to_dict(orient="records")
    except Exception as e:
        print(f"Error executing SQL:\n{sql_query}\nError: {e}")
        context["result"] = f"SQL Error: {e}"

    conn.close()
    return context