# -*- coding: utf-8 -*-
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt# Our integral approximation function

# f(x) = x² from 0 to 1.
def integral_approximation(f, a, b):
    return (b-a)*np.mean(f)# Integrate f(x) = x^2

# function
def f1(x):
    return x**2

# Define bounds of integral
a = 0
b = 1

# Generate function values
x_range = np.arange(a,b+0.001,.001)
fx = f1(x_range)

# Approximate integral
approx = integral_approximation(fx,a,b)
approx

# plt.xlim([-1,1])

plt.plot(x_range, fx)
plt.show()

# Scipy approximation
sc = integrate.quad(f1,a,b)
print(sc)

