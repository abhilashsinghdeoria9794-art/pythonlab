import sqlite3

# Connect to database
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

# Insert sample employee records
employees = [
    (101, "Rahul", "Developer", "IT", 50000),
    (102, "Priya", "Manager", "HR", 60000),
    (103, "Amit", "Developer", "IT", 55000),
    (104, "Neha", "Analyst", "Finance", 45000),
    (105, "Ravi", "Manager", "HR", 65000)
]

cur.executemany(
    "INSERT OR IGNORE INTO employee VALUES (?, ?, ?, ?, ?)",
    employees
)

con.commit()


# Generate department-wise salary report
def salary_report():
    department = input("Enter Department: ")

    # Parameterized SQL query
    cur.execute("""
    SELECT emp_id, name, designation, salary
    FROM employee
    WHERE department = ?
    """, (department,))

    rows = cur.fetchall()

    if rows:
        print("\nSalary Report for", department)
        print("--------------------------------------")

        total = 0

        for row in rows:
            print("Employee ID :", row[0])
            print("Name        :", row[1])
            print("Designation :", row[2])
            print("Salary      :", row[3])
            print("--------------------------------------")

            total += row[3]

        print("Total Salary:", total)
        print("Number of Employees:", len(rows))

    else:
        print("No employees found in this department.")


# Generate report
salary_report()

# Close database
con.close()