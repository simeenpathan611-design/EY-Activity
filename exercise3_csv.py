import csv
import logging

logging.basicConfig(filename="app.log",level=logging.INFO,format="%(levelname)s %(message)s")

data = [
    ["product","price","quantity"],
    ["Laptop",70000,2],
    ["Mouse",500,5],
    ["Keyboard",1200,3],
]

try:
    with open("sales.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    logging.info("Sales CSV written")

except Exception as e:
    logging.error(e)
    print("ERROR:sales.csv not found")

try:
    with open("sales.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                product = row["product"]
                price = int(row["price"])
                quantity = int(row["quantity"])
                total = price * quantity

                print(f"{product} total={total}")
                logging.info(f"{product} total={total}")

            except ValueError:
                logging.error("Sales CSV not found")
                print("ERROR:sales.csv not found")

except FileNotFoundError:
    logging.error("Sales CSV not found")
    print("ERROR:sales.csv not found")