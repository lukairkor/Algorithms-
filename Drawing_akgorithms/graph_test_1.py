#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:43:14 2021

@author: lukas
"""
import igraph as ig

# kol_startowa = [1, 4, 5, 3, 6, 2]
# kol_docelowa = [5, 3, 2, 4, 6, 1]

g = ig.Graph(n = 6, edges = [(1, 5), (4, 3), (5, 2), (3, 4), (6, 6), (2, 1)], directed = True)

g.vs["name"] = ["6", "1", "2", "3", "4", "5"]
g.vs["mass"] = [2523, 3123, 1812, 4713, 2223, 2312]

layout = g.layout("kk")

g.vs["label"] = g.vs["name"]

color_dict = {"1": "blue", "2": "pink","3": "brown", "4": "brown","5": "blue", "6": "pink"}
ig.plot(g, layout = layout, bbox = (300, 300), margin = 20, vertex_color = 
                                [color_dict[name] for name in g.vs["name"]])

















