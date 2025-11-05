import os
import pandas as pd
import sqlite3
 
def load_excel_to_sql(context):
    folder = "excel_files"
    db_name = "data_agent.db"
    conn = sqlite3.connect(db_name)
 
    for file in os.listdir(folder):
        if file.endswith(".xlsx"):
            file_path = os.path.join(folder, file)
            data = pd.read_excel(file_path, sheet_name=None)
            for sheet, df in data.items():
                table_name = f"{os.path.splitext(file)[0]}_{sheet}".lower().replace(" ", "_")
                df.to_sql(table_name, conn, if_exists="replace", index=False)
                print(f"Loaded table: {table_name}")
 
    conn.close()
    context["db_path"] = db_name
    return context