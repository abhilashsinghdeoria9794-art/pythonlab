import os
import xml.etree.ElementTree as ET

script_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(script_dir, "students.xml")
out_path = os.path.join(script_dir, "students_updated.xml")

tree = ET.parse(xml_path)
root = tree.getroot()

for student in root.findall("student"):
    if student.attrib.get("id") == "101":
        student.find("cgpa").text = "8.8"

new_student = ET.SubElement(root, "student", id="111")
ET.SubElement(new_student, "name").text = "Aarav Gupta"
ET.SubElement(new_student, "department").text = "CSE"
ET.SubElement(new_student, "year").text = "1"
ET.SubElement(new_student, "email").text = "aarav.gupta@example.com"
ET.SubElement(new_student, "cgpa").text = "9.2"

tree.write(out_path, encoding="utf-8", xml_declaration=True)
print(ET.tostring(root, encoding="unicode"))