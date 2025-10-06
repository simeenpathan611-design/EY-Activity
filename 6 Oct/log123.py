import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Low memory warning")
logging.error("Error message")
logging.critical("Critical message")




try:
    value = int(input("Enter a number: "))
    print(10/value)

except ValueError:
    print("Please enter a valid number!")

except ZeroDivisionError:
    print("Can't divide by zero!")

finally:
    print("Execution Completed")