#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Time complexity: O(N)
Auxiliary Space: O(1)
"""

def lin_search(lis, res):
    '''linear search function'''
    for i, elem in enumerate(lis):
        if elem == res:
            return "on position: ", i
    return "not in list"


if __name__ == "__main__":
    li = [1, 2, 3, 1, 5, 6]
    # result = 3
    print(lin_search(li, 3))
