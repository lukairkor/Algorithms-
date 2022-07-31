#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 23:22:44 2022

@author: lukas
"""

string1 = "ala"
string2 = "aln"

def is_pallindrom(string_1):
    return string_1 == string_1[::-1]

print(is_pallindrom(string1))
print(is_pallindrom(string2))
    
    