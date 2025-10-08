from fastapi.testclient import TestClient
from courses import app

client = TestClient(app)

def test_get_all_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(),list)

def test_add_new_course():
    new_course = {
        "id":2,"title":"Data Science","duration":40,"fee":4000,"is_active":True
    }
    response = client.post("/courses/",json=new_course)
    assert response.status_code == 201
    assert response.json()["title"] == "Data Science"

def test_add_new_courses():
    new_course = {
        "id":1,"title":"Data Science","duration":40,"fee":4000,"is_active":True
    }
    response = client.post("/courses/",json=new_course)
    assert response.status_code == 400
    assert response.json()["detail"] == "Course ID already exists"

def test_add_new_coursess():
    new_course = ({
        "id":3,"title":123,"duration":0,"fee":-7000,"is_active":True
    })
    response = client.post("/courses/",json=new_course)
    assert response.status_code == 422
    # assert "greater than" in response.json()

def test_get_courses():
    response = client.get("/courses")
    data = response.json()
    assert isinstance(data, list)
    assert all("title" in course for course in data)