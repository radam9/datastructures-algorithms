import random

limit = 1000000
unordered_array = random.sample(range(limit), limit)


def bubble_sort(array):
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


def selection_sort(array):
    array_length = len(array)
    for index in range(array_length - 1):
        lowest_index = index

        for index_two in range(index + 1, array_length):
            if array[index_two] < array[lowest_index]:
                lowest_index = index_two

        if lowest_index != index:
            array[index], array[lowest_index] = array[lowest_index], array[index]

    return array


def insertion_sort(array):
    array_length = len(array)
    for index in range(1, array_length):
        carry_value = array[index]
        position = index - 1

        while position >= 0:
            if carry_value < array[position]:
                array[position + 1] = array[position]
                position -= 1
            else:
                break
        array[position + 1] = carry_value

    return array
