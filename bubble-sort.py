def bubblesort(list):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                isSorted = False
                tempList = list[i]
                list[i] = list[i+1]
                list[i+1] = tempList
    return list
