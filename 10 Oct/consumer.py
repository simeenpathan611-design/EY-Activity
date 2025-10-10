import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue="student_tasks")

def callback(ch, method, properties, body):
    task = json.loads(body)
    print("Recieved:",task)
    time.sleep(2)
    print("Task processed for student:",task["student_id"])

channel.basic_consume(queue="student_tasks", on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

