# Student Record Management using List and Dictionary

students = []
while True:
    print("1.Add  2.Delete  3.Search  4.Display  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        ScholarID = input("ScholarID No: ")
        name = input("Name: ")
        students.append({"ScholarID": ScholarID, "Name": name})
        print("Record Added")

    elif ch == "2":
        ScholarID = input("Enter ScholarID No to delete: ")
        for s in students:
            if s["ScholarID"] == ScholarID:
                students.remove(s)
                print("Record Deleted")
                break
        else:
            print("Record Not Found")

    elif ch == "3":
      ScholarID= input("Enter ScholarID No to search: ")
      for s in students:
            if s["ScholarID"] == ScholarID:
                print(s)
                break
            else:
               print("Record Not Found")

    elif ch == "4":
        for s in students:
            print(s)

    elif ch == "5":
        break

    else:
        print("Invalid Choice")