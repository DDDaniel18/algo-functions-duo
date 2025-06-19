def bubble_sort(lst):
    """
    מקבלת רשימה lst ומחזירה עותק ממויין בעזרת Bubble Sort
    """
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(lst):
    """
    מקבלת רשימה lst ומחזירה רשימה ממוינת בעזרת Quick Sort
    (פונקציה רקורסיבית)
    """
    if len(lst) < 2:
        return lst.copy()
    pivot = lst[len(lst)//2]
    less    = [x for x in lst if x <  pivot]
    equal   = [x for x in lst if x == pivot]
    greater = [x for x in lst if x >  pivot]
    return quick_sort(less) + equal + quick_sort(greater)
