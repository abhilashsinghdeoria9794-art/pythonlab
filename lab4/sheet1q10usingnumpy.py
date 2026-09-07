import numpy as np

r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

print("Enter Matrix A:")
A = np.array([list(map(int, input().split())) for _ in range(r1)])

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

print("Enter Matrix B:")
B = np.array([list(map(int, input().split())) for _ in range(r2)])

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

if A.shape == B.shape:
    print("\nAddition:")
    print(A + B)

    print("\nSubtraction:")
    print(A - B)
else:
    print("\nAddition and subtraction not possible.")

if c1 == r2:
    print("\nMultiplication:")
    print(A @ B)
else:
    print("\nMultiplication not possible.")

print("\nTranspose of Matrix A:")
print(A.T)

print("\nTranspose of Matrix B:")
print(B.T)