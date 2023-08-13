#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 23:17:20 2022

@author: lukas
"""

a = "bark"
b = "krab"


def is_anagram(a, b):
    # check if equal number of characters
    # eliminate duplicates
    if set(a) == set(b):
        print("are anagrams")
    else:
        print("are not anagrams")


is_anagram(a, b)
