import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="root")
if mycon.is_connected():
    print("sucessfully connected")
cursor = mycon.cursor()
#creating database
cursor.execute("CREATE DATABASE school")

# using "school" database
cursor.execute("USE school")

#Creating table and adding columns
cursor.execute("CREATE TABLE students (""student_id INT, ""first_name VARCHAR(255), "
               "last_name VARCHAR(255), ""age INT, ""grade FLOAT)")
# Task 2: Inserting a new student record
cursor.execute("INSERT INTO students (student_id, first_name, last_name, age, grade) VALUES (%s, %s, %s, %s,%s)",
               (11,"Alice", "Smith", 18, 95.5))
mycon.commit()

# Task 3: Updating the grade of the student with the first name "Alice"
cursor.execute("UPDATE students SET grade = %s WHERE first_name = %s", (97.0, "Alice"))
mycon.commit()

#Task 4: Deleting the student with the last name "Smith"
cursor.execute("DELETE FROM students WHERE last_name = %s", ("Smith",))
mycon.commit()

# Task 5: Fetching and display all student records
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

print("Student Records:")
for student in students:
    print(student)
# Closing the cursor and database connection
cursor.close()
mycon.commit()


