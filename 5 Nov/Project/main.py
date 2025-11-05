from data_agent.graph_agent import create_data_agent_graph
 
if __name__ == "__main__":
    agent = create_data_agent_graph()
 
    while True:
        question = input("\nAsk the question (or 'exit'): ")
        if question.lower() == "exit":
            break
        result = agent.invoke({"question": question})
        print("\nAnswer:", result.get("result"))