student={
    "name" : "simeen",
    "age" : 22,
    "course" : "AI & ML"
}


student["grade"] = "A"
student["age"] = 23

student.pop("course")
del student["grade"]
print(student)