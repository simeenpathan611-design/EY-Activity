class Student:
    def __init__(self, name, age,email):
        self.name = name
        self.age = age
        self.email = email

data ={
    "name":"Simeen",
    "age":22,
    "email":"simeen@example.com"
}
student = Student(**data)
print(student.age)