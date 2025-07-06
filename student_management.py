import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="Thiru",
        password="1234",
        database="studentdb"
    )
    return conn

def add_student(name, age, grade):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    val = (name, age, grade)
    cursor.execute(sql, val)
    conn.commit()
    print("Student added successfully.")
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student List ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    conn.close()

def update_student(student_id, name, age, grade):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s"
    val = (name, age, grade, student_id)
    cursor.execute(sql, val)
    conn.commit()
    print("Student updated successfully.")
    conn.close()

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM students WHERE id=%s"
    val = (student_id,)
    cursor.execute(sql, val)
    conn.commit()
    print("Student deleted successfully.")
    conn.close()

def menu():
    while True:
        print("""
======= Student Management System =======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
""")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_student(name, age, grade)
        
        elif choice == '2':
            view_students()
        
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            update_student(student_id, name, age, grade)
        
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
