import os
import sqlite3
import chromadb
from openai import AzureOpenAI
from dotenv import load_dotenv
 
load_dotenv()
 
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION")
)
 
embedding_model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")
 
def embed_sql_schema(context):
    db_path = context["db_path"]
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
 
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection("excel_schema")
 
    for (table,) in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        for col in columns:
            col_name = col[1]
            text = f"Column '{col_name}' in table '{table}'"
            emb = client.embeddings.create(model=embedding_model, input=text).data[0].embedding
            collection.add(documents=[text], embeddings=[emb], ids=[f"{table}.{col_name}"])
    
    conn.close()
    print("Embeddings created and stored.")
    return context