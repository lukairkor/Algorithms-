#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 07:07:56 2022
-Obliczanie kata
@author: lukas
"""
import numpy as np
import math
# 0.0578
# P1 = -0.0053
# P2 = -0.0163
# P3 = 0.043
# P4 = -0.0038

# P1 = -0.0094
# P2 = -0.0277
# P3 = 0.0478
# P4 = 0.0015

# 0.0393
P1 = -0.0359
P2 = -0.0404
P3 = 0.0431
P4 = -0.0083

# a = np.array([P3, P4])
# b = np.array([P2, P1])

# inner = np.inner(a, b)
# norms = LA.norm(a) * LA.norm(b)

# cos = inner / norms
# rad = np.arccos(np.clip(cos, -0.001, 0.001))
# deg = np.rad2deg(rad)

# print(rad)  # 1.35970299357215
# print(deg)  # 77.9052429229879

Q1 = P2 - P1
Q2 = P4 - P3

wynik = Q1 + Q2
print(wynik)

# deg = np.rad2deg(wynik)
# print(deg)  # 77.9052429229879

