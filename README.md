# Student Management System (Python + MySQL)

## 📌 Overview

A simple console-based Student Management System using **Python** and **MySQL** to perform CRUD operations:

- Add a new student
- View all students
- Update student details
- Delete a student

This app uses `mysql-connector-python` to connect to MySQL, making it easy to demonstrate database handling in Python.

---

## ⚙️ Features

- Console menu-driven interface
- Uses MySQL to store student data
- Cleanly separates CRUD functions
- Simple and easy to extend

---

## 🗂️ Technologies Used

- Python 3
- MySQL
- mysql-connector-python

---

## 🏗️ Database Setup

Run these commands in MySQL:

```sql
CREATE DATABASE studentdb;
USE studentdb;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    grade VARCHAR(10)
);
```

---

## 🔑 Connection Details

- **Username**: Your Username
- **Password**: Your Password

Update in the code:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="studentdb"
)
```

---

## 🚀 How to Run

1. Install dependencies:

```bash
pip install mysql-connector-python
```

2. Run the program:

```bash
python student_management.py
```

---

## 📌 Possible Enhancements

- Add data validation
- Add login authentication for the admin
- Build a GUI (e.g., with Tkinter)
- Store logs of changes

Feel free to extend it! 🚀

