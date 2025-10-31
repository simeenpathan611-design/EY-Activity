import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from langchain.memory import ConversationBufferMemory

# Load environment
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("Missing OPENROUTER_API_KEY in .env")

# Initialize Gemma via OpenRouter
llm = ChatOpenAI(
    model="google/gemma-2-9b-it",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.4,
    max_tokens=512
)


# === AGENT 1: Summarizer ===
def summarizer_agent(text):
    prompt = f"Summarize the following text in 3-4 sentences:\n{text}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()


# === AGENT 2: Sentiment Analyzer ===
def sentiment_agent(summary):
    prompt = f"Analyze the sentiment (positive, neutral, negative) of this text:\n{summary}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()


# === AGENT 3: Improver / Formatter ===
def improver_agent(summary, sentiment):
    prompt = f"""
Based on this summary and sentiment, create a professional short report.

Summary: {summary}
Sentiment: {sentiment}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()



memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# CHAIN LOGIC
def process_text_through_chain(text):
    print("\n Step 1: Summarizing...")
    summary = summarizer_agent(text)
    print(summary)

    print("\n Step 2: Analyzing Sentiment...")
    sentiment = sentiment_agent(summary)
    print(sentiment)

    print("\n Step 3: Improving and Finalizing Report...")
    final_report = improver_agent(summary, sentiment)
    print(final_report)

    memory.save_context(
        inputs={"input": text},
        outputs={"summary": summary, "sentiment": sentiment, "report": final_report},
    )

    return final_report


# === MAIN ===
if __name__ == "__main__":
    print("Agent Chain: Summarizer → Sentiment → Improver")
    while True:
        text = input("\nEnter text to process (or 'exit'): ")
        if text.lower() == "exit":
            break
        result = process_text_through_chain(text)
        print("\nFinal Output:\n", result)