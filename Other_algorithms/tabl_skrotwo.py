# -*- coding: utf-8 -*-
"""
-jest to slownik w pythonie
-zwykla lista wyszukiwanie proste
-cache, DNS, filtrowanie
"""
from collections import deque
serch_que = deque()
slownik = {"Michal": ["Jan"], "Tomek": ["Alicja"], "Joanna": ["Jakub"], "Krzysztof": ["Marek"],
           "ja": ["Michal", "Tomek", "Joanna", "Krzysztof"]}

# print(slownik["ja"])

czy_juz_jest = slownik.get("Michal")
# print(czy_juz_jest)

serch_que += slownik["ja"]
print(serch_que)
