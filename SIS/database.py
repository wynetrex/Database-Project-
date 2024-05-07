
import sqlite3
def Database():
    #creating student database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    #creating STUD_REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")

def getAllStudents():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM STUD_REGISTRATION;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def updateRecord(name, contact, email, branch, rollno):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    command_to_execute = f"UPDATE STUD_REGISTRATION SET STU_NAME='{name}',STU_CONTACT='{contact}',STU_EMAIL='{email}',STU_BRANCH='{branch}', STU_ROLLNO={rollno};"
    cursor.execute(command_to_execute)
    connection.commit()
    connection.close()
