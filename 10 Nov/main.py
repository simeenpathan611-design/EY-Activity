from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import analyze_sentiment
from middleware import log_requests
from database import store_feedback

app = FastAPI()

app.middleware("http")(log_requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Llama SentimentSense API is running!"}


@app.post("/predict")
async def predict(data: dict):
    text = data.get("text", "")
    return analyze_sentiment(text)


@app.post("/feedback")
def feedback(data: dict):
    store_feedback(data["text"], data["sentiment"], data["feedback"])
    return {"message": "Feedback received!"}