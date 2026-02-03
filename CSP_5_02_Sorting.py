import random
from typing import List, Tuple

def bubbleSort(items: List[int]) -> Tuple[List[int], int, int]:
    """Sort a list using bubble sort and count swaps & comparisons."""
    swaps = comparisons = 0
    items = items.copy()               # keep the original list untouched
    n = len(items)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
                swapped = True
        if not swapped:                 # list already sorted
            break
    return items, swaps, comparisons


def insertionSort(items: List[int]) -> Tuple[List[int], int, int]:
    """Sort a list using insertion sort and count swaps & comparisons."""
    swaps = comparisons = 0
    items = items.copy()
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0:
            comparisons += 1          # compare items[j] with key
            if items[j] > key:
                items[j + 1] = items[j]
                swaps += 1
                j -= 1
            else:
                break
        items[j + 1] = key
    return items, swaps, comparisons

def selectionSort(items: List[int]) -> Tuple[List[int], int, int]:
    """Sort a list using selection sort and count swaps & comparisons."""
    swaps = comparisons = 0
    items = items.copy()
    n = len(items)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[min_index]:
                min_index = j
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
            swaps += 1
    return items, swaps, comparisons


# -------------------------------------------------
# Simple test driver
# -------------------------------------------------
if __name__ == "__main__":
    y = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(f"Bubble sort   : {bubbleSort(y)}")
    print(f"Insertion sort: {insertionSort(y)}")
    print(f"Selection sort: {selectionSort(y)}\n")

    x = list(range(50))
    random.shuffle(x)

    print(f"Bubble sort   : {bubbleSort(x)}")
    print(f"Insertion sort: {insertionSort(x)}")
    print(f"Selection sort: {selectionSort(x)}")
