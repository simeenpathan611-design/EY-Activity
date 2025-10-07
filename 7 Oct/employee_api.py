from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Employee Management API")

class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None


app = FastAPI(title="Employee Management API")

employees: List[Employee] = [
    Employee(id=1, name="Asha Patil", department="Engineering", salary=75000.0),
    Employee(id=2, name="Ravi Kumar", department="Finance", salary=60000.0),
    Employee(id=3, name="Meera Singh", department="HR", salary=50000.0),
]


@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees


@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="employee not found")


@app.post("/employees", response_model=Employee, status_code=201)
def create_employee(emp: Employee):
    if any(e.id == emp.id for e in employees):
        raise HTTPException(status_code=409, detail="employee already exists")
    employees.append(emp)
    return emp


@app.put("/employees/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, emp: EmployeeUpdate):
    for i, e in enumerate(employees):
        if e.id == emp_id:
            updated = e.dict()
            update_data = emp_update.dict(exclude_unset=True)
            updated.update(update_data)
            update_emp = Employe(**updated)
            employees[i] = updated_emp
            return updated_emp
    raise HTTPException(status_code=404, detail="employee not found")


@app.delete("/employees/{emp_id}", status_code=204)
def delete_employee(emp_id: int):
    for i, e in enumerate(employees):
        if e.id == emp_id:
            del employees[i]
            return
    raise HTTPException(status_code=404, detail="employee not found")


@app.get("/employees/count")
def employees_count():
    return {"count": len(employees)}