from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True

data = {
    "name": "Simeen",
    "age": 22,
    "email": "simeen@example.com",
}
student = Student(**data)

print(student)
print(student.name)