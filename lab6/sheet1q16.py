import sqlite3

# connect to database
con = sqlite3.connect("student.db")
cur = con.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    ScholarID TEXT,
    name TEXT,
    department TEXT,
    cgpa REAL
)
""")

# insert student details
ScholarID = input("Enter Your Scholar ID: ")
name = input("Enter Name: ")
department = input("Enter Department: ")
cgpa = float(input("Enter CGPA: "))

cur.execute(
    "INSERT INTO student VALUES (?, ?, ?, ?)",
    (ScholarID, name, department, cgpa)
)

con.commit()

print("\nStudent details stored successfully.")
# display student details
print("\nStudent Details:")
cur.execute("SELECT * FROM student")

for row in cur.fetchall():
    print("ScholarID :", row[0])
    print("Name        :", row[1])
    print("Department  :", row[2])
    print("CGPA        :", row[3])
    print()
# close connection
con.close()