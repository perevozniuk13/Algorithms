# SELECTION SORT
def selectionSort(list):
    for i in range(len(list)):
        currentMin = list[i]
        for j in range(i+1, len(list)):
            temp = list[j]
            if currentMin < temp:
                continue
            elif currentMin > temp:
                currentMin = temp
            else:
                return  -1
        ind = list.index(currentMin)
        list[i], list[ind] = list[ind], list[i]
    return list


# BUBBLE SORT
def bubbleSort(list):
    for i in range(len(list)):
        currentMax = list[0]
        for j in range(0, len(list)-1):
            temp = list[j+1]
            if currentMax > temp:
                ind = list.index(currentMax)
                list[j+1], list[ind] = list[ind], list[j+1]
            elif currentMax < temp:
                currentMax = temp
            else:
                return -1
    return list



# INSERTION SORT

def insertionSort(list):
    for i in range(len(list)-1):
        if list[i+1] > list[i]:
            continue
        elif list[i+1] < list[i]:
            current = list[i+1]
            list[i], list[i+1] = list[i+1], list[i]
            for j in reversed(range(i)):
                if current < list[j]:
                    ind = list.index(current)
                    list[j], list[ind] = list[ind], list[j]
                else:
                    continue
    return list


# QUICK SORT (using last element as a pivot)

def quickSort(list):
    if len(list) <= 1:
        return list
    pivot = list[-1]
    itemsGreater = []
    itemsSmaller = []
    for i in range(len(list)-1):
        if list[i] < pivot:
            itemsSmaller.append(list[i])
        else:
            itemsGreater.append(list[i])
    return quickSort(itemsSmaller) + [pivot] + quickSort(itemsGreater)



# MERGE SORT
def merge(left, right):
    new_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        elif left[i] > right[j]:
            new_list.append(right[j])
            j += 1
    new_list.extend(left[i:])
    new_list.extend(right[j:])
    return new_list


def mergeSort(list):
    if len(list) <= 1:
        return list
    midLen = int(len(list) / 2)
    leftPart = mergeSort(list[:midLen])
    rightPart = mergeSort(list[midLen:])
    return merge(leftPart, rightPart)

