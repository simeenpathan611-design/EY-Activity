import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("⚠️ Please add your OPENROUTER_API_KEY in .env file")

# Initialize Google Gemma model via OpenRouter
llm = ChatOpenAI(
    model="google/gemma-2-9b-it",  # you can also try "google/gemma-2-27b-it"
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    temperature=0.6,
)

# Initialize conversational memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
personal_memory = []  # For user "facts" (like notes or reminders)


# === TOOL 1: Remember ===
def remember_fact(text):
    fact = text.replace("remember", "", 1).strip()
    if not fact:
        return "Agent: Please specify what to remember."
    personal_memory.append(fact)
    return f"Agent: Noted — I’ll remember that you said: '{fact}'."


# === TOOL 2: Recall ===
def recall_facts():
    if not personal_memory:
        return "Agent: You haven't told me anything to remember yet."
    notes = "\n".join([f"{i + 1}. {fact}" for i, fact in enumerate(personal_memory)])
    return f"Agent: Here's what I remember:\n{notes}"


# === TOOL 3: Forget ===
def forget_facts(command):
    if not personal_memory:
        return "Agent: There’s nothing to forget right now."
    if "all" in command:
        personal_memory.clear()
        return "Agent: All your saved memories have been cleared."
    elif "last" in command:
        removed = personal_memory.pop()
        return f"Agent: I forgot the last memory: '{removed}'."
    else:
        return "Agent: Use 'forget last' or 'forget all'."


# === TOOL 4: Summarize Conversation (uses Gemma) ===
def summarize_chat():
    history = memory.load_memory_variables({}).get("chat_history", [])
    if not history:
        return "Agent: No conversation to summarize yet."
    conversation_text = "\n".join([f"{msg.type}: {msg.content}" for msg in history])
    prompt = f"Summarize this conversation briefly:\n{conversation_text}"
    response = llm.invoke(prompt)
    return f"Agent (Summary): {response.content}"


# === TOOL 5: Default chat handler ===
def chat_with_llm(user_input):
    response = llm.invoke(user_input)
    memory.save_context(inputs={"input": user_input}, outputs={"output": response.content})
    return f"Agent: {response.content}"


# === MAIN LOOP ===
def run_memory_agent():
    print("🤖 Conversational Memory Agent")
    print("Available commands:")
    print("- remember <something>  → store memory")
    print("- recall                 → show all remembered facts")
    print("- forget last / all      → delete memory")
    print("- summarize              → summarize conversation")
    print("- exit                   → quit\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("👋 Goodbye!")
            break
        elif user_input.startswith("remember"):
            print(remember_fact(user_input))
        elif user_input == "recall":
            print(recall_facts())
        elif user_input.startswith("forget"):
            print(forget_facts(user_input))
        elif user_input == "summarize":
            print(summarize_chat())
        else:
            print(chat_with_llm(user_input))
        print()


# === RUN AGENT ===
if __name__ == "__main__":
    run_memory_agent()