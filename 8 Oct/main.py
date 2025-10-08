from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float

employees =  [
    {"id":1, "name":"Asha Patil", "department":"Engineering", "salary":75000.0}]
    
@app.get("/employees")
def get_employees():
    return employees

@app.post("/employees", status_code=201)
def add_employee(new_employee: Employee):
    employees.append(new_employee.model_dump())
    return new_employee

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="employee not found")

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    for i, employee in enumerate(employees):
        if employee["id"] == employee_id:
            employees[i] = updated_employee.dict()
            return updated_employee
    raise HTTPException(status_code=404, detail="employee not found")


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for i, employee in enumerate(employees):
        if employee["id"] == employee_id:
            employees.pop(i)
            return {"message":"employee deleted"}
    raise HTTPException(status_code=404, detail="employee not found")


