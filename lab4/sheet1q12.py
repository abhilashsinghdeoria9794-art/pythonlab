import numpy as np

n = int(input("Enter the order of the matrix: "))

print("Enter the matrix:")
A = np.array([list(map(float, input().split())) for i in range(n)])

print("\nMatrix:")
print(A)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
for value in eigenvalues:
    print(round(value.real, 2))

print("\nEigenvectors:")
for i in range(n):
    print("Eigenvalue =", round(eigenvalues[i].real, 2))
    print("Eigenvector =", eigenvectors[:, i].real)

