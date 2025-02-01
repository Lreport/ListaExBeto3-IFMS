def soma_lista_aninhada(lista):
    sum = 0
    for NumInList in lista:
        if isinstance(NumInList, list):
            sum += soma_lista_aninhada(NumInList)
        else:
            sum += NumInList
    return sum
print(soma_lista_aninhada([1, [2, 3], [4, [5]]]))