import CSP_5_02_Sorting as HW
x = [10, 70, 30, 20, 60, 40, 90, 80, 50]
y = [9,8,7,6,5,4,3,2,1]
long = []
for i in range(200,0,-1):
    long.append(i)
l = long.copy()
l.sort()

def test_bubble_sort():
    assert HW.bubbleSort(x.copy()) ==([10, 20, 30, 40, 50, 60, 70, 80, 90], 11, 40)
    assert HW.bubbleSort(y.copy()) ==([1, 2, 3, 4, 5, 6, 7, 8, 9], 36, 72)
    assert HW.bubbleSort(long.copy()) == (l,19900,39800)



def test_insertion_sort():
    assert HW.insertionSort(x.copy()) == ([10, 20, 30, 40, 50, 60, 70, 80, 90], 11, 19)
    assert HW.insertionSort(y.copy()) == ([1, 2, 3, 4, 5, 6, 7, 8, 9], 36, 36)
    assert HW.insertionSort(long.copy()) == (l, 19900, 19900)


def test_selection_sort():
    assert HW.selectionSort(x.copy()) == ([10, 20, 30, 40, 50, 60, 70, 80, 90], 8, 36)
    assert HW.selectionSort(y.copy()) == ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 36)
    assert HW.selectionSort(long.copy()) == (l, 199, 19900)
