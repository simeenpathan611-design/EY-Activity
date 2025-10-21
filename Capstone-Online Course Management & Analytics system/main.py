from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import pandas as pd
import logging
from datetime import datetime
import asyncio
import os

app = FastAPI(title="Online Course Management & Analytics System")

#logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)


os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

#df
courses = pd.DataFrame([
    {"CourseID": "C181", "Title": "Python for Beginners", "Category": "Programming", "Duration": 40},
    {"CourseID": "C102", "Title": "Machine Learning Basics", "Category": "AI", "Duration": 60},
    {"CourseID": "C183", "Title": "Data Visualization with Power BI", "Category": "Analytics", "Duration": 30},
    {"CourseID": "C104", "Title": "Cloud Fundamentals", "Category": "Cloud", "Duration": 50}
])

students = pd.DataFrame([
    {"StudentID": "5081", "Name": "Neha", "Email": "neha@example.com", "Country": "India"},
    {"StudentID": "5082", "Name": "Arjun", "Email": "arjun@example.com", "Country": "UAE"},
    {"StudentID": "5083", "Name": "Sophia", "Email": "sophia@example.com", "Country": "UK"},
    {"StudentID": "5004", "Name": "Ravi", "Email": "ravi@example.com", "Country": "India"},
    {"StudentID": "5005", "Name": "Meena", "Email": "meena@example.com", "Country": "USA"}
])

enrollments = pd.DataFrame([
    {"EnrollmentID": "E001", "StudentID": "5001", "CourseID": "C181", "EnrollDate": "2025-10-01", "Progress": 0},
    {"EnrollmentID": "E002", "StudentID": "5002", "CourseID": "C102", "EnrollDate": "2025-10-02", "Progress": 60},
    {"EnrollmentID": "E003", "StudentID": "5003", "CourseID": "C181", "EnrollDate": "2025-10-03", "Progress": 100},
    {"EnrollmentID": "E004", "StudentID": "5001", "CourseID": "C183", "EnrollDate": "2025-10-04", "Progress": 50},
    {"EnrollmentID": "E005", "StudentID": "5004", "CourseID": "C104", "EnrollDate": "2025-10-05", "Progress": 20},
    {"EnrollmentID": "E006", "StudentID": "5005", "CourseID": "C102", "EnrollDate": "2025-10-06", "Progress": 75},
])


#mid
class Course(BaseModel):
    CourseID: str
    Title: str
    Category: str
    Duration: int

class Student(BaseModel):
    StudentID: str
    Name: str
    Email: str
    Country: str

class Enrollment(BaseModel):
    EnrollmentID: str
    StudentID: str
    CourseID: str
    EnrollDate: str
    Progress: int


#CRUD-courses
@app.get("/courses")
def get_courses():
    return courses.to_dict(orient="records")

@app.post("/courses")
def add_course(course: Course):
    global courses
    if course.CourseID in courses["CourseID"].values:
        raise HTTPException(status_code=400, detail="Course already exists")
    courses = pd.concat([courses, pd.DataFrame([course.dict()])], ignore_index=True)
    logging.info(f"Added new course: {course.Title}")
    return {"message": "Course added successfully"}

@app.put("/courses/{course_id}")
def update_course(course_id: str, updated: Course):
    global courses
    idx = courses.index[courses["CourseID"] == course_id]
    if len(idx) == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    courses.loc[idx, :] = list(updated.dict().values())
    logging.info(f"Updated course: {course_id}")
    return {"message": "Course updated"}

@app.delete("/courses/{course_id}")
def delete_course(course_id: str):
    global courses
    courses = courses[courses["CourseID"] != course_id]
    logging.info(f"Deleted course: {course_id}")
    return {"message": "Course deleted"}


#CRUD-students
@app.get("/students")
def get_students():
    return students.to_dict(orient="records")

@app.get("/students/india")
def get_indian_students():
    df = students[students["Country"].str.lower() == "india"]
    return df.to_dict(orient="records")

@app.post("/students")
def add_student(student: Student):
    global students
    if student.StudentID in students["StudentID"].values:
        raise HTTPException(status_code=400, detail="Student already exists")
    students = pd.concat([students, pd.DataFrame([student.dict()])], ignore_index=True)
    logging.info(f"Added new student: {student.Name}")
    return {"message": "Student added successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    global students
    students = students[students["StudentID"] != student_id]
    logging.info(f"Deleted student: {student_id}")
    return {"message": "Student deleted"}


#ETL
def process_enrollments():
    global enrollments, students, courses
    df = enrollments.merge(students, on="StudentID", how="left")
    df = df.merge(courses, on="CourseID", how="left")
    df["CompletionStatus"] = df["Progress"].apply(lambda x: "Completed" if x >= 80 else "In Progress")
    df["EnrollMonth"] = pd.to_datetime(df["EnrollDate"], errors="coerce").dt.month
    df.to_csv("data/processed_enrollments.csv", index=False)
    logging.info("ETL completed and saved processed_enrollments.csv")
    return df

@app.get("/etl")
def run_etl():
    df = process_enrollments()
    return {"message": f"ETL completed with {len(df)} records"}


#queue
@app.post("/enrollments")
async def add_enrollment(enroll: Enrollment, background_tasks: BackgroundTasks):
    global enrollments
    enrollments = pd.concat([enrollments, pd.DataFrame([enroll.dict()])], ignore_index=True)
    logging.info(f"New enrollment received: {enroll.EnrollmentID}")
    # Simulate async queue processing
    background_tasks.add_task(async_etl)
    return {"message": "Enrollment added & queued for processing"}

async def async_etl():
    await asyncio.sleep(2)
    process_enrollments()


#analysis
@app.get("/analytics")
def generate_analytics():
    df = pd.read_csv("data/processed_enrollments.csv")

    completion = df.groupby("CourseID")["CompletionStatus"].apply(lambda x: (x == "Completed").mean() * 100)
    students_per_category = df.groupby("Category")["StudentID"].nunique()
    country_enrollments = df.groupby("Country")["StudentID"].count()
    monthly_trends = df.groupby("EnrollMonth")["EnrollmentID"].count()

    summary = pd.DataFrame({
        "CompletionRatePerCourse": completion,
        "StudentsPerCategory": students_per_category,
        "CountryWiseEnrollments": country_enrollments,
        "MonthlyEnrollments": monthly_trends
    }).fillna(0)

    summary.to_csv("reports/learning_analytics.csv")
    logging.info("Analytics report generated")
    return {"message": "Analytics generated", "rows": len(summary)}


#daily report
@app.get("/daily-report")
def daily_report():
    df = process_enrollments()
    filename = f"reports/daily_enrollment_report_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(filename, index=False)
    logging.info(f"Daily report created: {filename}")
    return {"message": f"Daily report generated as {filename}"}