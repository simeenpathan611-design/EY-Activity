import pandas as pd
import os

df = pd.read_csv('processed_enrollments.csv')

df['EnrollMonth'] = pd.to_datetime(df['EnrollDate'], errors='coerce').dt.strftime('%B')

completion_rate = df.groupby('CourseID')['CompletionStatus'].apply(
    lambda x: (x == 'Completed').mean() * 100
).reset_index()
completion_rate['Metric'] = 'CompletionRate'
completion_rate = completion_rate.rename(columns={'CourseID': 'Name', 'CompletionStatus': 'Value'})

students_per_category = df.groupby('Category')['StudentID'].nunique().reset_index()
students_per_category['Metric'] = 'TotalStudents'
students_per_category = students_per_category.rename(columns={'Category': 'Name', 'StudentID': 'Value'})

country_enrollments = df.groupby('Country')['StudentID'].count().reset_index()
country_enrollments['Metric'] = 'CountryEnrollments'
country_enrollments = country_enrollments.rename(columns={'Country': 'Name', 'StudentID': 'Value'})

monthly_trends = df.groupby('EnrollMonth')['EnrollmentID'].count().reset_index()
monthly_trends['Metric'] = 'MonthlyEnrollments'
monthly_trends = monthly_trends.rename(columns={'EnrollMonth': 'Name', 'EnrollmentID': 'Value'})

analytics = pd.concat([completion_rate, students_per_category, country_enrollments, monthly_trends], ignore_index=True)

os.makedirs('reports', exist_ok=True)
analytics.to_csv('reports/learning_analytics.csv', index=False)

print("Analytics Report Generated: reports/learning_analytics.csv")