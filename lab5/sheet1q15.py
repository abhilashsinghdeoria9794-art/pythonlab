import numpy as np
from scipy.optimize import minimize

# Define the function
def f(v):
    x, y = v
    return (x - 2)**2 + (y - 2)**2

# Initial guess
initial_guess = [0, 0]

# Perform optimization
result = minimize(f, initial_guess, method='BFGS')

# Display results
print("Optimization Result:")
print("x =", result.x[0])
print("y =", result.x[1])
print("Minimum value =", result.fun)
print("Success =", result.success)
print("Message =", result.message)