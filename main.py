from Sort import *
from BinarySearch import *

def search():
    a = input("Type in the list: ")
    list = [int(i) for i in a.split()]
    print("Your list: ", list)
    elem = int(input("Type in the element to find using Binary Search algorithm: "))
    print("Index of the element:", binarySearch(elem, list))

def sort_():
    a = input("Type in the list to sort: ")
    unsortedList = [int(i) for i in a.split()]
    print("Unsorted list: ", unsortedList)
    print("1 - Selection sort")
    print("2 - Bubble sort")
    print("3 - Insertion sort")
    print("4 - Quick sort")
    print("5 - Merge sort")
    num = int(input("Choose the type of sorting algorithm by typing the number: "))
    if num == 1:
        print(selectionSort(unsortedList))
    elif num == 2:
        print(bubbleSort(unsortedList))
    elif num == 3:
        print(insertionSort(unsortedList))
    elif num == 4:
        print(quickSort(unsortedList))
    elif num == 5:
        print(mergeSort(unsortedList))
    else:
        print("wrong number!")

search()
sort_()