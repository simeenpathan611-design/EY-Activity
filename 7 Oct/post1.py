#Post
@app.post(path="/students/{id}")
def add_students(student:Student):
    students.apend(student.dict())
    return {"message":"Students added successfully","student":student}