import numpy as np
from scipy.integrate import quad

# Define the mathematical function
def f(x):
    return x**3 + 2*x**2 + x + 1

# Point at which differentiation is required
x = 2

# Numerical differentiation
h = 1e-5
df = (f(x + h) - f(x - h)) / (2 * h)

print("Function: f(x) = x^3 + 2x^2 + x + 1")
print("Numerical derivative at x =", x, ":", df)

# Numerical integration
lower_limit = 0
upper_limit = 2

result, error = quad(f, lower_limit, upper_limit)

print("Numerical integration from", lower_limit, "to", upper_limit)
print("Integral =", result)
print("Estimated error =", error)