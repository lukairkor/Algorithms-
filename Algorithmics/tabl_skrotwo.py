# -*- coding: utf-8 -*-
"""
-jest to slownik w pythonie
-zwykla lista wyszukiwanie proste
-cache, DNS, filtrowanie
"""
from collections import deque
serch_que = deque()
slownik = {}

slownik["Michal"] = ["Jan"]
slownik["Tomek"] = ["Alicja"]
slownik["Joanna"] = ["Jakub"]
slownik["Krzysztof"] = ["Marek"]
slownik["ja"] = ["Michal", "Tomek", "Joanna", "Krzysztof"]
# print(slownik["ja"])

czy_juz_jest = slownik.get("Michal")
# print(czy_juz_jest)

serch_que += slownik["ja"]
print(serch_que)

