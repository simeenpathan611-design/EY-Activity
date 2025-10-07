#Put
@app.put("/students/{student_id")
def update_student(student_id:int, updated_student:Student):
    for i,s in enumerate(students):
        if s["id"] == student_id:
            students[i].update(updated_student.dict())
            return {"message":"Students updated successfully","student":updated_student}
    raise HTTPException(status_code=404, detail="student not found")