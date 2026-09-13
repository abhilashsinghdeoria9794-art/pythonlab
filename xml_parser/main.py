import xml.etree.ElementTree as ET

tree = ET.parse("university_records.xml")
root = tree.getroot()

print("UNIVERSITY RECORDS")
print("=" * 60)

print("University:", root.get("name"))

campus = root.find("campus")

print("Location:", campus.find("location").text)
print("Established:", campus.find("established").text)
print("Website:", campus.find("website").text)

print("\nDEPARTMENT DETAILS")
print("=" * 60)

departments = root.find("departments")

for department in departments.findall("department"):

    department_id = department.get("id")
    name = department.find("name").text
    hod = department.find("hod").text
    building = department.find("building").text

    print("\nDepartment ID:", department_id)
    print("Department:", name)
    print("HOD:", hod)
    print("Building:", building)

    students = department.find("students")

    print("\nStudents:")

    for student in students.findall("student"):

        student_id = student.get("id")

        first_name = student.find(
            "personal_details/name/first_name"
        ).text

        last_name = student.find(
            "personal_details/name/last_name"
        ).text

        cgpa = student.find(
            "academic_details/cgpa"
        ).text

        year = student.find(
            "academic_details/year"
        ).text

        semester = student.find(
            "academic_details/semester"
        ).text

        print(
            f"  {student_id} - {first_name} {last_name} "
            f"- Year: {year}, Semester: {semester}, CGPA: {cgpa}"
        )