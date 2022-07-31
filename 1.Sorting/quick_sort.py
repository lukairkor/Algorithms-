#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:01:07 2021
- Pivot is arbitrrary element in the collection
- Divide and conquer strategy, induction
- Probably one of best to use
@author: lukas
"""
import random


def quic_sort(ls_):
    '''quick sort implementation'''
    # simple case
    if len(ls_) < 2:
        return ls_

    # recursion case
    pivot = ls_[0]
    less  = [i for i in ls_[1:] if i <= pivot]
    greater  = [i for i in ls_[1:] if i >= pivot]
    return quic_sort(less) + [pivot] + quic_sort(greater)


if __name__ == '__main__':
    # create randomly filled list
    fill = lambda f, n, s, st: [f(s, st) for i in range(n)]
    list_ = fill(random.randint, 8, 1, 100)
    print("unsorted: ", list_, "\n")
    
    list_ = quic_sort(list_)
    print("sorted: ", list_)
