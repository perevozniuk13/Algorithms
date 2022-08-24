# BINARY SEARCH
import math

def binarySearch(element, list):
    i = math.ceil(len(list) / 2) - 1
    while True:
        if list[i] == element:
            return i
        elif list[i] > element:
            i -= 1
        else:
            i += 1
