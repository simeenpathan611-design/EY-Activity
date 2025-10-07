#Delete
@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for s in students:
        if s["id"] == student_id:
            students.remove(s)  
            return {"message":"Students deleted successfully","student":s}
    raise HTTPException(status_code=404, detail="student not found")