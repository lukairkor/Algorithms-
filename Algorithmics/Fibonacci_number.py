#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:58:58 2021

@author: lukas
"""

def fibonacci(n):
    wynik = 1
    if n <= 2:
        return wynik
    else:
        wynik = fibonacci(n - 2) + fibonacci(n - 1)
        return wynik
        
c = fibonacci(19)
print(c)