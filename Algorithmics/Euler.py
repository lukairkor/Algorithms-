#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:19:37 2021
-created 2500 years ago
-Greatest common divisor
@author: lukas
"""
a = 12
b = 9000

def Euler_alg(a, b):
    while(True):
        if a == b:
            return a
        elif a < b:
            b = b - a
        else:
            a = a - b
c = Euler_alg(a, b)
print(c)

