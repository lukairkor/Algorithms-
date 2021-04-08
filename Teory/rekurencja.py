# -*- coding: utf-8 -*-
"""
-stos a rekurencja (funkcje na stosie)
-stos wywolan
"""
#example 1 adding numb to itself several times
"""def add_to_numb(base_number, numb_for_add):
    print(base_number)
    if base_number >= 100: #przypadek podstawowy
        return base_number
    else:                  #przypadek rekurencyjny
        add_to_numb(base_number + numb_for_add, numb_for_add)

if __name__ == "__main__":
    base_number = 23
    numb_for_add = 3
    x = add_to_numb(base_number, numb_for_add)"""

#example 2 counting elements stored by list elem_in_list
"""def count_elem(my_list):
    if my_list:             #unless list is not empty
          return 1 + count_elem(my_list[:-1])
    return 0 # else
    
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    x = count_elem(my_list)
    print(x)"""
    
#example 3 find largest number in the list
def count_elem(my_list, n):
    if len(my_list) == 1:             #unless list is not empty
          return my_list[0]
    else: 
        return  # else bazowy przypadek
    
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    x = count_elem(my_list, n = 3)
    print(x)
