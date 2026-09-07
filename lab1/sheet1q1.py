num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of", num, "is", factorial)

if num <= 1:
    print(num, "is not a prime number.")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")