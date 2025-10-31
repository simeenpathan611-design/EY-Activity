import os
from http.client import responses

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

llm = ChatOpenAI(
    model="google/gemma-3n-e4b-it:free",
    temperature=0.4,
    max_tokens=512,
    api_key=api_key,
    base_url=base_url,
)

def run_chat(text: str) -> str:
    """You are a friendly AI assistant"""
    prompt = text
    response = llm.invoke(prompt)
    return response.content.strip()

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

print("\n=== Start chatting with your Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    if user_input.lower().startswith("chat"):
        try:
            text = user_input.replace("chat", "", 1).strip()
            if not text:
                print("Agent:Please provide text to chat.")
                continue
        except Exception as e:
            print("Agent:Could not chat.", e)
            continue

    try:
        response = llm.invoke(user_input)
        print("Agent:", response.content)
        memory.save_context({"input": user_input}, {"output": response.content})
    except Exception as e:
        print("Error:", e)