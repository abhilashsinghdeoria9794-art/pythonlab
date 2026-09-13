students=[]

def insert_student(name,roll,course):
    student={"name":name,"roll":roll,"course":course}
    students.append(student)
def delete_student(roll):
    for student in students:
        if student["roll"]==roll:
            student.remove(student)
            return
        
def search_student(roll):
    for student in students:
        if student["roll"]==roll:
            return student
    return None

insert_student("abhilash",153,"CSE")
insert_student("adarsh",160,"CSE")
insert_student("Anand",72,"CSE")
print(search_student(72))
delete_student(160)
print(students)    