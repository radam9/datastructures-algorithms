import random

limit = 10000000
array = [r for r in range(limit)]
search_value = random.randint(0, limit)


def linearsearch(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index
    return None


def binarysearch(array, search_value):
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
