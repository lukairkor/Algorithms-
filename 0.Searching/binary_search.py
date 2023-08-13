#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- Binary Tree Search
- O(logn)
- looking for mid
- znacznie szybsze od wyszukiwania prostego mierzy się podając tępo zwiekszania
się pracy wraz z przysrostem liczby danych
"""
import random


# generating an example list
def list_gen():
    """generating list"""
    lis = []
    step = random.randrange(1, 4, 1)
    for i in range(0, 1000, step):
        lis.append(i)
    # print(lista)
    return lis


# binary search algorithm
def binary_tree(searched, lis):
    """search algorithm function"""
    begin = 0
    end = len(lis) - 1
    while begin <= end:
        mid = int((end - begin))
        # print(mid)
        checked_item = lis[mid]
        if checked_item == searched:
            return mid
        elif checked_item > searched:
            end = mid - 1
        else:
            begin = mid + 1


if __name__ == "__main__":
    searc_item = 18
    lista = list_gen()
    result = binary_tree(searc_item, lista)
    print(result)
