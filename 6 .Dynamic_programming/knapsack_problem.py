#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:14:30 2021
- when we can divide the main problem into sub-problems
- similar to recursion but not identical
- like inducting reasoning in practice
@author: lukas
"""


def knap_sack(knap_capac, weight, value, capac_parts, products):
    dp = [0 for i in range(knap_capac + 1)]  # zero filled empty knapsack

    for i in range(1, capac_parts + 1):  # first our element value (from 6)
        print("\nelement name (row): ", products[i], "\nvalue: ", value[i - 1], "\nweight: ", weight[i - 1])
        for w in range(knap_capac, 0, -1):  # from 6 to 1 (kg)
            print("table column weight: ", w)
            if weight[i - 1] <= w:  # if the weight (of our product) is less or equal to
                # our first slot

                # finding the maximum value
                # from equation
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])
                print(dp)  # 26 [0, 0, 0, 0, 0, 0, 10] -> [0, 6, 9, 11, 16, 19, 21]
    return dp[knap_capac]  # returning the maximum value of knapsack


products = {1: "water", 2: "book", 3: "food", 4: "jacket", 5: "camera"}

# Driver code
value = [10, 3, 3, 5, 6]  # items values
weight = [3, 1, 2, 2, 1]  # items weight
knap_capac = 6  # knapsack capacity
capac_parts = len(value)  # how many values
print(knap_sack(knap_capac, weight, value, capac_parts, products))
