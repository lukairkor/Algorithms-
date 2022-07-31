#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:58:58 2021

@author: lukas
"""
import numpy as np
import matplotlib.pyplot as plt

#
vec = []

# function
def fib(n):
    wynik = 1
    if n <= 2:
        return wynik
    else:
        wynik = fib(n-2) + fib(n-1)
        vec.append(wynik)
    return wynik

#\ 
n_numb = 14
# call function
fib(n_numb)

#remove duplicates
new_vec = list(set(vec))
new_vec.insert(0, 1)
new_vec.insert(0, 1)
new_vec.sort()
new_vec_max = max(new_vec)
new_vec_max_to_str = str(new_vec_max)
#
x = np.linspace(1, n_numb + 1, len(new_vec), endpoint=False)
y = new_vec
#
fig, ax = plt.subplots()
line1, = ax.plot(x, y, 'ro')
#
ax.set_title('Fibonacci Sequence result: ' + new_vec_max_to_str)
line1, = ax.plot(x, y)
#
ax.minorticks_on()
ax.grid(which='major', color='r', linestyle='-', linewidth=0.5)
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()
