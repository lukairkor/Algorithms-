"""
-Binary Tree Search
-zlozonosc obliczeniowa O(logn)
-szukamy srodka
-znacznie szybsze od wyszukiwania prostego mierzy się podając tępo zwiekszania
się pracy wraz z przysrostem liczby danych
"""
import random
#generating example list
def list_gen():
    lista = []
    step = random.randrange(1, 4, 1)    
    for i in range(0, 1000, step):
        lista.append(i)
    # print(lista)
    return lista
#binary search algorithm
def binary_tree(searched, lista):
    begin = 0
    end = len(lista) - 1
    while begin <= end:
        mid = int((end - begin))
        # print(mid)
        checked_item = lista[mid]
        if checked_item == searched:
            return mid
        elif checked_item > searched:
            end = mid - 1
        else:
            begin = mid + 1
            
if __name__ == "__main__":
    searc_item = 18
    lista = list_gen()
    x = binary_tree(searc_item, lista)
    print(x)
