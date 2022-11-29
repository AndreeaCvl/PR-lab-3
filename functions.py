import sqlite3

global db
db = sqlite3.connect(':memory:', check_same_thread=False)

db.execute('''CREATE TABLE STUDENTS
                    (ID INT PRIMARY KEY     NOT NULL,
                    NAME           TEXT    NOT NULL,
                    YEAR            INT     NOT NULL);''')

db.commit()


def fetch_db_all():
    students = []

    # Use a row factory to access values by column name
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    # convert row objects to dictionary
    for i in rows:
        student = {"id": i["id"], "name": i["name"], "year": i["year"]}
        students.append(student)

    return students


def fetch_db(student_id):
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    select_query = """select * from STUDENTS where id = ?"""
    cursor.execute(select_query, (student_id,))

    # return one single row.
    row = cursor.fetchone()

    student = {"id": row["id"], "name": row["name"], "year": row["year"]}

    return student


def add_student(data):
    cursor = db.cursor()

    add_record = """INSERT INTO STUDENTS (ID,NAME,YEAR) \
              VALUES (?, ?, ?);"""
    try:
        cursor.execute(add_record, (data['id'], data['name'], data['year']))
        db.commit()
    except:
        return "UNIQUE constraint failed: STUDENTS.ID"

    new_student = fetch_db(cursor.lastrowid)

    return new_student


def update_student(student):
    cursor = db.cursor()

    sql_update_query = """Update STUDENTS set name = ?, year = ? where id = ?"""
    cursor.execute(sql_update_query, (student["name"], student["year"], student["id"],))

    db.commit()

    upd_student = fetch_db(student["id"])

    return upd_student


def delete_student(student_id):
    sql_delete_query = "DELETE from students WHERE id = ?"
    db.execute(sql_delete_query, (student_id,))
    db.commit()

    return "Record deleted"
