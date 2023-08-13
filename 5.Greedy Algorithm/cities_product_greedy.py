#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:33:09 2021
- Problem NP - zupelny (jak rozpoznac?)
- set cover problem
- aproximation algorithm
- where should I go to buy all products and visit little places?
@author: lukas
"""

# products I want to buy
cities_list = {"bread", "sugar", "butter", "meat", "rice", "tomato", "oil", "yoghurt"}

# wher are those products?
products = {"kl": {"bread", "butter", "rice", "oil", "yoghurt"}, "po": {"sugar", "tomato", "oil"},
            "wr": {"bread", "sugar", "butter", "rice", "yoghurt"}, "gd": {"meat", "rice", "oil"},
            "wa": {"sugar", "rice", "tomato", "yoghurt"}}

# our final destination plan
final_destinations = set()

while cities_list:
    # best place to start shoping (a lot of products there)
    best_desti = None
    # new products (not in previous cities)
    new_produc = set()
    for product, cities in products.items():
        # set intersection
        covered = cities_list & cities
        if len(covered) > len(new_produc):
            best_desti = product
            new_produc = covered

    cities_list -= new_produc
    final_destinations.add(best_desti)

print(final_destinations)
