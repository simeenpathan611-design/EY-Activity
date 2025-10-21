import queue, threading, pandas as pd, time

q = queue.Queue()

def producer():
    enrollments = pd.read_csv('enrollments.csv')
    for _, row in enrollments.iterrows():
        q.put(row.to_dict())
        print(f"Produced: {row['EnrollmentID']}")
        time.sleep(0.5)
    q.put(None)  # End signal

def consumer():
    processed = []
    while True:
        item = q.get()
        if item is None:
            break
        item['CompletionStatus'] = 'Completed' if item['Progress'] >= 80 else 'In Progress'
        processed.append(item)
        print(f"Consumed: {item['Enrollment ID']}")
    pd.DataFrame(processed).to_csv('processed_enrollments.csv', index=False)
    print("Consumer finished. Data saved.")


threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()