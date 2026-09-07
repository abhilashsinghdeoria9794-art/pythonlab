import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#given data
x=np.array([1,2,3,4,5,6])
y=np.array([6,17,34,57,86,121])

#define second degree polynomial
def polynomial(x,a,b,c):
    return a*x**2+ b*x +c
#fit the polynomial 
coefficients,covariance=curve_fit(polynomial,x,y)
a,b,c=coefficients

#dislay coefficients
print("Estimated polynomail coefficients : ")
print("a=",a)
print("b=",b)
print("c=",c)

print("\n Fitted polynomial: ")
print(f"y={a:.2f}x^2+{b:.2f}x+{c:.2f}")

#generate point for fitted curve 
x_fit= np.linspace(1,6,100)
y_fit=polynomial(x_fit,a,b,c)
#plot original data points
plt.scatter(x,y,label="original data ")
plt.plot(x_fit,y_fit,label="Fitted Curve ")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Second -Degree Polynomial fit")
plt.legend()
plt.grid(True)
plt.show()
