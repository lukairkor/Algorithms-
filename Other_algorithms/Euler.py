#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 9 00:19:37 2021
 
@author: lukas
"""
a = 12
b = 9000


def euler_alg(a1, b1):
    while True:
        if a1 == b1:
            return a1
        elif a1 < b1:
            b1 = b1 - a1
        else:
            a1 = a1 - b1


c = euler_alg(a, b)
print(c)
