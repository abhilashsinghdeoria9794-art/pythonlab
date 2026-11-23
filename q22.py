import os
import xml.etree.ElementTree as ET

script_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(script_dir, "students.xml")

tree = ET.parse(xml_path)
root = tree.getroot()

for student in root.findall("student"):
    sid = student.attrib.get("id")
    name = student.find("name").text
    dept = student.find("department").text
    year = student.find("year").text
    email = student.find("email").text
    cgpa = student.find("cgpa").text
    print(f"ID: {sid} | Name: {name} | Dept: {dept} | Year: {year} | Email: {email} | CGPA: {cgpa}")