# -*- coding: utf-8 -*-
"""
-dla grafow ważonych
-brak krawedzi o ujemnej wadze w grafie aby zadzialal,
inaczej stosujemy algorytm Bellmana-Forda

"""
# budowa grafu na podstawie tablicy skrotow
graph = {"start": {}}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
print(graph["start"].keys())  # sasiedzi wezla start
print(graph["start"]["a"])  # waga krawedzi
# dodawanie pozostalych wezlow oraz ich sasiadow
graph["a"] = {}
graph["a"]["meta"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["meta"] = 5

graph["meta"] = {}  # wezel mety nie ma zadnych sasiadow
print(graph)

# implementacja tabeli kosztow
infinity = float("inf")
costs = {'a': 6, 'b': 2, 'fin': infinity}

# implementacja tablicy rodzicow
parents = {'a': "start", 'b': "start", 'meta': None}

# rejestrowanie sprawdzonych wezlow
processed = []

# algorytm
