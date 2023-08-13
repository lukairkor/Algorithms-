#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
- BFS breadth first search 
- queue implementation
- looking for shortest path
- czy graf jest spojny
"""
from collections import deque


def person_is_seler(name):
    return name[-1] == 'm'


def check(name):
    serch_que = deque()
    serch_que += graf[name]
    searched = []  # checked before
    while serch_que:
        person = serch_que.popleft()
        if not person in searched:  # did whe check it before
            if person_is_seler(person):
                print(person + " sprzedaje mango!")
                return True
            else:
                serch_que += graf[person]
                searched.append(person)
    return False


if __name__ == "__main__":
    graf = {"ja": ["Michal", "Tomek", "Joanna"], "Michal": ["Jan"], "Tomek": ["Alicja"], "Joanna": ["Jakub"],
            "Jan": [], "Alicja": [], "Jakub": []}

    print(graf)
    print(check("ja"))
