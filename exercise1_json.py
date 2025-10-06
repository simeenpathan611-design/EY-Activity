import json
import logging

logging.basicConfig(filename="app.log",level=logging.INFO,format="%(asctime)s - (message)s")

try:
    with open("student.json","r") as f:
        student = json.load(f)
    logging.info("File read successful")

    print("Student Names:")
    for student in student:
        print(student["name"])

    new_student = {"name":"Arjun","age":20,"course":"Data Science","marks":78}
    student.append(new_student)
    logging.info("Student Added")

    with open("student.json","w") as f:
        json.dump(student,f,indent=4)
        logger.info("File saved")

except Exception as e:
    logging.error(e)