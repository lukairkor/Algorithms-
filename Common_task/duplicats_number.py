#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 23:12:01 2022

@author: lukas
"""


l = [1, 2, 2, 3, 1]

def dup_number(l):
    # creating sets
    dup, seen = set(), set()
    # iterating over our list
    for ele in l:
        # if number in seen add to dup
        if ele in seen:
            dup.add(ele)
        # if not add to ele
        seen.add(ele)
    return list(dup)


l = dup_number(l)
print(l)