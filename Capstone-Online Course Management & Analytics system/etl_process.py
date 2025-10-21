import pandas as pd

#data
courses = pd.read_csv('courses.csv')
students = pd.read_csv('students.csv')
enrollments = pd.read_csv('enrollments.csv')

#Merge
df = enrollments.merge(students, on='StudentID')
df = df.merge(courses, on='CourseID')


df['CompletionStatus'] = df['Progress'].apply(lambda x: 'Completed' if x >= 80 else 'In Progress')
df['EnrollMonth'] = pd.to_datetime(df['EnrollDate'], errors='coerce').dt.strftime('%B')

df.to_csv('processed_enrollments.csv', index=False)

print("ETL Process Completed. File saved as processed_enrollments.csv")