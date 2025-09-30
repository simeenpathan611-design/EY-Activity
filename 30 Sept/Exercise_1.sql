CREATE DATABASE IF NOT EXISTS SchoolsDB;
USE SchoolsDB;

CREATE TABLE Students (
student_id INT PRIMARY KEY,
student_name VARCHAR(50),
city VARCHAR(50)
);


CREATE TABLE Courses (
course_id INT PRIMARY KEY,
course_name VARCHAR(50)
);

CREATE TABLE Enrollments (
enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT,
course_id INT,
grade DECIMAL (4,2),
FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

INSERT INTO Students VALUES
(1,'Simeen','Kolhapur'),
(2,'Shayaan','Pune'),
(3,'Shruti','Goa'),
(4,'Saman','Mumbai');

INSERT INTO Courses VALUES
(101,'Maths'),
(102,'Science'),
(103,'Physics');

INSERT INTO Enrollments VALUES
(301,1,101,85.5),
(302,2,102,90.0),
(303,1,101,75.5),
(304,2,102,80.0);

-- LEVEL 1
-- 1

DELIMITER $$
CREATE PROCEDURE ListAllStudents()
BEGIN
SELECT * FROM Student;
END $$
DELIMITER ;

-- 2

DELIMITER $$
CREATE PROCEDURE ListAllCourses()
BEGIN
SELECT * FROM Courses;
END $$
DELIMITER ;

-- 3

DELIMITER $$
CREATE PROCEDURE FindStudentByCity(IN city_name VARCHAR(50))
BEGIN
SELECT * FROM Students WHERE city = city_name;
END $$
DELIMITER ;


-- LEVEL 2
-- 1

DELIMITER $$
CREATE PROCEDURE ListStudentsWithCourses()
BEGIN
SELECT s.student_id,s.student_name,c.course_name
FROM Student s 
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;
END $$
DELIMITER ;

-- 2

DELIMITER $$
CREATE PROCEDURE StudentsInCourse(IN cid INT)
BEGIN
SELECT s.student_id,s.student_name,c.course_name
FROM Student s 
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_id = cid;
END $$
DELIMITER ;

-- 3

DELIMITER $$
CREATE PROCEDURE CountStudentsPerCourse()
BEGIN
SELECT s.student_id,s.student_name,c.course_name, COUNT (e.student_id) AS student_count
FROM Courses c 
LEFT JOIN Enrollments e ON e.course_id = e.course_id
GROUP BY c.course_id,course_name;
END $$
DELIMITER ;


-- LEVEL 3
-- 1

DELIMITER $$
CREATE PROCEDURE StudentsCoursesGrades()
BEGIN
SELECT s.student_id,s.student_name,c.course_name,e.grade
FROM Student s 
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;
END $$
DELIMITER ;

-- 2

DELIMITER $$
CREATE PROCEDURE CoursesByStudents(IN sid INT)
BEGIN
SELECT s.student_id,s.student_name,c.course_name,e.grade
FROM Student s 
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE s.student_id = sid;
END $$
DELIMITER ;

-- 3

DELIMITER $$
CREATE PROCEDURE AvgGradePerCourse()
BEGIN
SELECT c.course_id,c.course_name, AVG (e.grade) AS avg_grade
FROM Courses c 
JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id,course_name;
END $$
DELIMITER ;

CALL ListAllStudent();
CALL ListALlCourses();
CALL FindStudentByCity('Mumbai');
CALL ListStudentsWithCourses();
CALL StudentInCourses(101);
