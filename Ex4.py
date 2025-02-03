def indice_maior_elemento(list, actualIndex=0, maxIndex=None, maxElement=None):
    if actualIndex == len(list):
        return maxIndex
    elif maxElement is None or list[actualIndex] > maxElement:
        maxIndex = actualIndex
        maxElement = list[actualIndex]
    return indice_maior_elemento(list, actualIndex + 1, maxIndex, maxElement)
print(indice_maior_elemento([1, 5, 3, 9, 2]))