# open input and output files 
input_file=open("student.txt","r")
output_file=open("student.txt","w")

for line in input_file:
    data= line.split()
    name=data[0]
    m1=input(data[1])
    m2=input(data[2])
    m3=input(data[3])

    total=m1+m2+m3
    average=total/3

    if average>=90:
        grade="A"
    elif average>=75:
            grade="B"
    elif average>=50:
            grade="C"
    else:
        grade="F"

    output_file.write(f"{name} Total: {total} Average:{average:.f} Grade: {grade}\n")


    input_file.close()
    output_file.close()
    print("Result save in result.txt")