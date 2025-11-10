import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def analyze_sentiment(text: str):
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "messages": [
                {"role": "system",
                 "content": (
                     "You are a helpful sentiment analysis assistant."
                     "Classify the sentiment of this text as Positive, Negative, or Neutral.\nText: {text}"
                 )
                 },
                 {
                     "role": "user",
                     "content": text
                 }
            ]
        }


        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        model_output = result["choices"][0]["message"]["content"].strip()

        # Extract only sentiment word
        if "positive" in model_output.lower():
            sentiment = "Positive"
        elif "negative" in model_output.lower():
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {"sentiment": sentiment, "raw_response": model_output}

    except Exception as e:
        return {"error": str(e)}