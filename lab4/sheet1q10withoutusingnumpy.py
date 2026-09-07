r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

print("Enter Matrix A:")
A = [list(map(int, input().split())) for _ in range(r1)]

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

print("Enter Matrix B:")
B = [list(map(int, input().split())) for _ in range(r2)]

print("\nMatrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

if r1 == r2 and c1 == c2:
    print("\nAddition:")
    C = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    for row in C:
        print(row)

    print("\nSubtraction:")
    C = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(A[i][j] - B[i][j])
        C.append(row)

    for row in C:
        print(row)
else:
    print("\nAddition and subtraction not possible.")

if c1 == r2:
    print("\nMultiplication:")
    C = []

    for i in range(r1):
        row = []
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        C.append(row)

    for row in C:
        print(row)
else:
    print("\nMultiplication not possible.")

print("\nTranspose of Matrix A:")
for j in range(c1):
    row = []
    for i in range(r1):
        row.append(A[i][j])
    print(row)

print("\nTranspose of Matrix B:")
for j in range(c2):
    row = []
    for i in range(r2):
        row.append(B[i][j])
    print(row)