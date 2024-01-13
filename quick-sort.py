def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list.pop()

    greater = []
    lower = []

    for item in list:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)

    return quicksort(lower) + [pivot] + quicksort(greater)
