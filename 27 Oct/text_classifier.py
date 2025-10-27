from transformers import pipeline

# Load a pre-trained Hugging Face model for sentiment analysis
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline("sentiment-analysis", model=model_name)

# Ask user for text input
text = input("Enter a sentence to analyze: ")

# Run the classification
result = classifier(text)[0]

# Display the result
print(f"\nText: {text}")
print(f"Sentiment: {result['label']}")
print(f"Confidence: {result['score']:.2f}")