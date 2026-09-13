import sqlite3

# Connect to SQLite database
con = sqlite3.connect("employee.db")
cur = con.cursor()

# Create employee table
cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    designation TEXT,
    department TEXT,
    salary REAL
)
""")

con.commit()


# CREATE - Add employee
def create():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    designation = input("Enter Designation: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    cur.execute(
        "INSERT INTO employee VALUES (?, ?, ?, ?, ?)",
        (emp_id, name, designation, department, salary)
    )

    con.commit()
    print("Employee added successfully.")


# READ - Display employees
def read():
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()

    print("\nEmployee Records:")
    for row in rows:
        print(row)


# UPDATE - Update employee details
def update():
    emp_id = int(input("Enter Employee ID to update: "))

    name = input("Enter new Name: ")
    designation = input("Enter new Designation: ")
    department = input("Enter new Department: ")
    salary = float(input("Enter new Salary: "))

    cur.execute("""
    UPDATE employee
    SET name = ?, designation = ?, department = ?, salary = ?
    WHERE emp_id = ?
    """, (name, designation, department, salary, emp_id))

    con.commit()
    print("Employee details updated successfully.")


# DELETE - Delete employee
def delete():
    emp_id = int(input("Enter Employee ID to delete: "))

    cur.execute(
        "DELETE FROM employee WHERE emp_id = ?",
        (emp_id,)
    )

    con.commit()
    print("Employee deleted successfully.")


# Main program
while True:
    print("\n--- Employee Management System ---")
    print("1. Create Employee")
    print("2. Read Employee Records")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create()

    elif choice == "2":
        read()

    elif choice == "3":
        update()

    elif choice == "4":
        delete()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

# Close database
con.close()