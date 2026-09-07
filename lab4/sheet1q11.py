import numpy as np

n = int(input("Enter the order of the matrix: "))

print("Enter the matrix:")
A = np.array([list(map(float, input().split())) for i in range(n)])

print("\nMatrix:")
print(A)

det = np.linalg.det(A)
print("\nDeterminant =", det)

if det != 0:
    inverse = np.linalg.inv(A)
    print("\nInverse:")
    print(inverse)
else:
    print("\nInverse does not exist")

rank = np.linalg.matrix_rank(A)
print("\nRank =", rank) 