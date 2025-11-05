from langgraph.graph import StateGraph, END
from data_agent.nodes.load_excel import load_excel_to_sql
from data_agent.nodes.embed_sql import embed_sql_schema
from data_agent.nodes.query_sql import ask_query
 
def create_data_agent_graph():
    graph = StateGraph(dict)
    
    graph.add_node("load_excel", load_excel_to_sql)
    graph.add_node("embed_sql", embed_sql_schema)
    graph.add_node("query_sql", ask_query)
    
    graph.set_entry_point("load_excel")
    graph.add_edge("load_excel", "embed_sql")
    graph.add_edge("embed_sql", "query_sql")
    graph.add_edge("query_sql", END)
    
    return graph.compile()