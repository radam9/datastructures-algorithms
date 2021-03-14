import random

limit = 1000000
ordered_array = [r for r in range(limit)]
unordered_array = random.sample(range(limit), limit)
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


def bubblesort(array):
    last_index = len(array) - 1

    sorting = True

    while sorting:
        sorting = False
        for index in range(last_index):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                sorting = True
        last_index -= 1

    return array
