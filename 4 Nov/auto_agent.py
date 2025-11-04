from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# LLM configuration for AutoGen
llm_config = {
    "config_list": [
        {
            "model": "mistralai/mistral-7b-instruct:free",  # You can switch to gpt-4 or claude
            "api_key": api_key,
            "base_url": base_url,
            "max_tokens":100
        }
    ]
}

# Disable Docker (optional)
os.environ["AUTOGEN_USE_DOCKER"] = "0"

# Create agents
researcher = AssistantAgent(name="researcher", llm_config=llm_config)
summarizer = AssistantAgent(name="summarizer", llm_config=llm_config)
notifier = AssistantAgent(name="notifier", llm_config=llm_config)
user = UserProxyAgent(name="user")


# Define functions
def research(topic: str):
    """Fetch research info using LLM."""
    prompt = f"Research the latest information about {topic}. Provide 5 key points."
    result = researcher.generate_reply(messages=[{"role": "user", "content": prompt}])
    return result


def summarize(text: str):
    """Summarize research text using LLM."""
    prompt = f"Summarize the following text in 3 concise bullet points:\n\n{text}"
    result = summarizer.generate_reply(messages=[{"role": "user", "content": prompt}])
    return result


def notify(summary: str, output_mode="console", file_path="summary.txt"):
    """Print or save the summary."""
    if output_mode == "console":
        print("\n===== FINAL SUMMARY =====")
        print(summary)
        print("=========================")
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"✅ Summary saved to {file_path}")
    return "Notification sent."


# Register functions with agents
researcher.register_function({"research": research})
summarizer.register_function({"summarize": summarize})
notifier.register_function({"notify": notify})

# Orchestrate the workflow
topic = input("🔍 Enter a topic to research: ")
print("\n[1] Researching...")
research_output = research(topic)

print("\n[2] Summarizing...")
summary_output = summarize(research_output)

print("\n[3] Notifying...")
notify(summary_output, output_mode="console")  # Change to "file" for saving