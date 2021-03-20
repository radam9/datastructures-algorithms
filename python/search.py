import random
from sort import _partition

limit = 1000000
ordered_array = [r for r in range(limit)]
search_value = random.randint(0, limit)


def linear_search(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index
    return None


def binary_search(array, search_value):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) / 2
        midpoint_value = array[midpoint]

        if search_value == midpoint_value:
            return midpoint
        elif search_value < midpoint_value:
            upper_bound = midpoint - 1
        elif search_value > midpoint_value:
            lower_bound = midpoint + 1

    return None


def quick_select(array, value, right=None, left=0):
    if not right:
        right = len(array) - 1

    pivot = _partition(array, right, left)

    if value == pivot:
        result = array[pivot]
    elif value < pivot:
        result = quick_select(array, value, right=pivot - 1, left=left)
    elif value > pivot:
        result = quick_select(array, value, right, left=pivot + 1)
    return result
