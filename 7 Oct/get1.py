from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    id:int
    name: str
    age:int
    course: str

students = [
    {"id":1,"name":"Rahul","age":18,"course":"AI"},
    {"id":2,"name":"Priya","age":20,"course":"ML"},
]

@app.get("/students")
def get_students():
    return {"students":students}

@app.get("/students/{id}")
def get_student(student_id: int):
    for s in students:
        if s["id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="student not found")