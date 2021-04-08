#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:01:07 2021
-pivot - element osiowy wydajnosc od jego wyboru zalezy (wysoki stos)
-strategia dziel i rzadz, indukcja
@author: lukas
"""
import random
# create random filled list
fill = lambda f, n, s, st: [f(s, st) for i in range(n)]
list_ = fill(random.randint, 8, 1, 100)
print("not sortet: ", list_, "\n")

def quic_sort(list_):
    if len(list_) < 2:  #przypadek prosty
        return list_   
    else:               #przypadek rekurencyjny
        pivot = list_[0]
        less  = [i for i in list_[1:] if i <= pivot]
        greater  = [i for i in list_[1:] if i >= pivot]
        return quic_sort(less) + [pivot] + quic_sort(greater)

print("sorted: ", quic_sort(list_))        