# Student record  using tuple and set

# student detail
student1 = ("1", "Adarsh")
student2 = ("2", "Gunjan")
#course detail
courses1 = {"Python", "English", "DBMS"}
courses2 = {"Python", "C", "DBMS"}

print("Student 1:", student1)
print("Student 2:", student2)

# Common courses
print("Common courses:", courses1.intersection(courses2))
# All courses
print("All courses:", courses1.union(courses2))
# Courses only taken by Student 1
print("only student 1:", courses1.difference(courses2))
# courses only taken by Student 2
print("only student 2:", courses2.difference(courses1))