CREATE DATABASE IF NOT EXISTS HospitalDB;
USE HospitalDB;

CREATE TABLE Patients (
patient_id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
gender CHAR(1),	
city VARCHAR(50)
);

CREATE TABLE Doctors (
doctor_id INT PRIMARY KEY,
name VARCHAR(50),
specialization VARCHAR(50),
experience INT 
);

CREATE TABLE Appointments (
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

CREATE TABLE MedicalRecords (
record_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
diagnosis VARCHAR(100),
treatment VARCHAR(100),
date DATE,
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

CREATE TABLE Billing(
bill_id INT PRIMARY KEY,
patient_id INT,
amount DECIMAL(10,2),
bill_date DATE,
status VARCHAR(20),
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

INSERT INTO Patients VALUES
(1,'Rahul',34,'M','Mumbai'),
(2,'Radha',24,'F','Pune'),
(3,'Sahil',40,'M','Nipani'),
(4,'Nehal',55,'F','Kolhapur'),
(5,'Ram',42,'M','Bangalore'),
(6,'Rishi',64,'M','Delhi'),
(7,'Minal',22,'F','Jaipur');

INSERT INTO Doctors VALUES
(11,'Dr.Ramesh','Cardiology',25),
(12,'Dr.Sita','Orthopedics',20),
(13,'Dr.Suresh','Pediatrics',18),
(14,'Dr.Anjali','Dermatology',22),
(15,'Dr.Arvind','Neorology',20);

INSERT INTO MedicalRecords VALUES
(201,1,11,'Chest Pain','ECG & Medicines','2025-09-01'),
(202,2,13,'Fever','Paracetamol','2025-09-02'),
(203,3,12,'Fracture','Plaster Cast','2025-09-03'),
(204,4,11,'High BP','Lifestyle Changes','2025-09-04'),
(205,5,15,'Headache','MRI & Treatment','2025-09-05'),
(206,6,14,'Skin Allergy','Ointments','2025-09-06'),
(207,7,12,'Back Pain','Physiotherapy','2025-09-07');

INSERT INTO Billing VALUES
(301,1,1500,'2025-09-01','Paid'),
(302,2,2500,'2025-09-02','UnPaid'),
(303,3,1000,'2025-09-03','Paid'),
(304,4,2000,'2025-09-04','Paid'),
(305,5,3500,'2025-09-05','UnPaid'),
(306,6,4500,'2025-09-06','Paid'),
(307,7,3000,'2025-09-07','UnPaid');

SELECT p.name,d.name AS doctor_name
FROM Patients p
JOIN Appointments a ON p.patient_id = a.patient_id
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE d.specialization = 'Cardiology';

SELECT a.appointment_id, p.name AS patient_name,a.appointment_date
FROM Appointments 
JOIN Patients p ON a.patient_id = p.patient_id
WHERE a.doctor_id = 11;

SELECT b.bill_id, p.name, b.amount, b.bill_date
FROM Billing b
Join Patients p ON b.patient_id = p.patient_id
WHERE b.status = 'UnPaid';

DELIMITER $$
CREATE PROCEDURE GetPatientHistory(IN pat_id INT)
BEGIN
SELECT m.date,d.name AS doctor_name,m.diagnosis,m.treatment
FROM MedicalRecords m
JOIN Doctors d ON m.doctor_id = d.doctor_id
WHERE m.patient_id = pat_id;
END $$

DELIMITER $$
CREATE PROCEDURE GetDoctorAppointments(IN doc_id INT)
BEGIN
SELECT a.appointment_date,p.name AS patient_name
FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
WHERE a.doctor_id = doc_id;
END $$

DELIMITER ;

CALL GetPatientHistory(1);
CALL GetDoctorAppointments(11);