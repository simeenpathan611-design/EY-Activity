import csv

def store_feedback(text, sentiment, feedback):
    with open("feedback.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([text, sentiment, feedback])