import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001"

st.title("💬 SentimentSense (Llama Edition)")
st.write("Analyze text sentiment using the Llama LLM via OpenRouter!")

text = st.text_area("Enter your text here:")
if st.button("Analyze Sentiment"):
    response = requests.post(f"{API_URL}/predict", json={"text": text})
    if response.status_code == 200:
        result = response.json()
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"Predicted Sentiment: **{result['sentiment']}**")
            st.caption(f"Model says: {result['raw_response']}")

            feedback = st.radio("Was this prediction correct?", ["Yes", "No"])
            if st.button("Submit Feedback"):
                requests.post(f"{API_URL}/feedback", json={
                    "text": text,
                    "sentiment": result["sentiment"],
                    "feedback": feedback
                })
                st.info("✅ Feedback recorded — thank you!")
    else:
        st.error("⚠️ Failed to connect to backend.")