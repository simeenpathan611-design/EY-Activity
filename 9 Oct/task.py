from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

students = [
    {"id":1,"name":"Simeen Pathan","age":22,"course":"Data Science"},
    {"id":2,"name":"Shruti Aamte","age":21,"course":"Artificial Intelligence"},
    {"id":3,"name":"Aamna Sheikh","age":23,"course":"Cloud Computing"},
    {"id":4,"name":"Saman Khan","age":24,"course":"Machine Learning"},
    {"id":5,"name":"Soni Pandey","age":20,"course":"Cybersecurity"},
]

@app.get("/students/")
async def get_students():
    return JSONResponse(content={"students":students})

@app.get("/",response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student</title>
        <style>
            body {
                font-family:Arial,sans-serif;
                margin:50px;
                background-color:#f4f4f9;
                color:#333;
                text-align:center;
            }
            table {
                margin:20px auto;
                border-collapse:collapse;
                width:70%;
                box-shadow:0 0 10px rgba(0,0,0,0.1);
                background-color:white;
            }
            th, td {
                border:1px solid #ddd;
                padding:12px;
            }
            th {
                background-color:#4CAF50;
                color:white;
                }
        <style>
    </head>
    <body>
        <h1>Student List</h1>
        <table id="studentTable">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Course</th>
                </tr>
            </thead>
            <tbody id="tableBody">
                <!-- Students will load here -->
            </tbody>
        </table>
        
        <script>
            async function fetchStudents() {
                const response = await fetch('/students);
                const data = await response.json();
                const tableBody = document.getElementById('tableBody');
                tbody.innerHTML = '';
                
                data.students.forEach(student => {
                    const row = '
                        <tr>
                            <td>${student.id}</td>
                            <td>${student.name}</td>
                            <td>${student.age}</td>
                            <td>${student.course}</td>
                        </tr>
                    ';
                    tbody.innerHTML += row;
                });
            }
            fetchStudents();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

