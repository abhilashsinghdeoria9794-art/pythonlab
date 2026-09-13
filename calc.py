a =float(input("enter a number:"))
operator = input("operation (+,-,/,*):")
b=float(input("enter second number:"))

if operator == "+":
    print("result:", a + b)

elif operator == "-":
    print("result:", a - b)

elif operator =="/":
    if b!=0:
        print("result:", a/b)
    else:
        print("cant divide by zero")

elif operator=="*":
    print("result:",a*b)
else:
    print("invalid number")
   