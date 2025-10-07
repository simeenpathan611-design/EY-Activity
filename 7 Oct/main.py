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



#Post
@app.post(path="/students/{id}")
def add_students(student:Student):
    students.apend(student.dict())
    return {"message":"Students added successfully","student":student}


#Put
@app.put("/students/{student_id")
def update_student(student_id:int, updated_student:Student):
    for i,s in enumerate(students):
        if s["id"] == student_id:
            students[i].update(updated_student.dict())
            return {"message":"Students updated successfully","student":updated_student}
    raise HTTPException(status_code=404, detail="student not found")



#Delete
@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            return {"message":"Students deleted successfully","student":s}
    raise HTTPException(status_code=404, detail="student not found")