#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
- Divide and Conquer algorithm paradigm
- using recursion
- widely used
- when input size larger than RAM size
- for sorting linked list
- for inversion count problem
"""

def merg_sort(mer_arr):
    """Merge sorting function"""

    # list length
    l_leng = len(mer_arr)

    # list already sorted
    if l_leng > 1:
        # find list midpoint
        mid = l_leng // 2
        # divide array
        arr_left = mer_arr[:mid]
        arr_right = mer_arr[mid:]
        # sorting array halfs
        merg_sort(arr_left)
        merg_sort(arr_right)

        i = j = k = 0

        # while left and right have single element
        while i < len(arr_left) and j < len(arr_right):
            # check with number is greater
            if arr_left[i] < arr_right[j]:
                # add left elements to end of mer_arr k
                mer_arr[k] = arr_left[i]
                i += 1
            else:
                # add right elements to end of mer_arr k
                mer_arr[k] = arr_right[j]
                j += 1
            k += 1
        # check second array
        while i < len(arr_left):
            mer_arr[k] = arr_left[i]
            i += 1
            k += 1

        while j < len(arr_right):
            mer_arr[k] = arr_right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [3, 1, 8, 6, 2]
    merg_sort(arr)
    print(arr)
    