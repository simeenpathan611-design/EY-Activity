import streamlit as st
import os
import pandas as pd
import sqlite3
from data_agent.graph_agent import create_data_agent_graph
from data_agent.nodes.load_excel import load_excel_to_sql

st.set_page_config(page_title="Data Agent", layout="wide")
st.title("Data Agent")

@st.cache_resource
def get_agent():
    return create_data_agent_graph()

agent = get_agent()

st.sidebar.header("Upload Excel Files")
uploaded_files = st.sidebar.file_uploader("Upload your Excel files", type=["xlsx"], accept_multiple_files=True)

db_path = "data_agent.db"

# Load uploaded Excel files into SQLite
if uploaded_files:
    st.sidebar.success(f"{len(uploaded_files)} file(s) uploaded.")
    for file in uploaded_files:
        file_path = os.path.join("excel_files", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
        load_excel_to_sql(file_path,db_path)
    st.sidebar.success("Excel files converted to SQLite.")

st.header("Ask a Question about Your Data")
question = st.text_input("Enter your question here:")

if question:
    with st.spinner("Processing your question..."):
        result = agent.invoke({"question": question})
        st.successs("Done")
        st.write("### AI Answer:")
        st.write(result.get("result"))

if st.checkbox("Show Raw Result Data"):
    conn = sqlite3.connect(db_path)
    tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    st.write("### Tables in Database:",tables)

    selected_table = st.selectbox("Select a table to view data:", tables['name'])
    if selected_table:
        df = pd.read_sql_query(f"SELECT * FROM {selected_table} LIMIT 100;", conn)
        st.dataframe(df)
