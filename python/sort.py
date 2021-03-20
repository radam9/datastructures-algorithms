import random

limit = 1000000
unordered_array = random.sample(range(limit), limit)


def bubble_sort(array):
    """Sort array in place using Bubble Sort"""
    last_index = len(array) - 1

    sorting = True

    while sorting:
        sorting = False
        for index in range(last_index):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                sorting = True
        last_index -= 1


def selection_sort(array):
    """Sort array in place using Selection Sort"""
    array_length = len(array)
    for index in range(array_length - 1):
        lowest_index = index

        for index_two in range(index + 1, array_length):
            if array[index_two] < array[lowest_index]:
                lowest_index = index_two

        if lowest_index != index:
            array[index], array[lowest_index] = array[lowest_index], array[index]


def insertion_sort(array):
    """Sort array in place using Instertion Sort"""
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


def _partition(array, right_pointer, left_pointer):
    pivot = array[right_pointer]
    index = left_pointer - 1

    for pointer in range(left_pointer, right_pointer):
        if array[pointer] < pivot:
            index += 1
            array[index], array[pointer] = array[pointer], array[index]
    array[index + 1], array[right_pointer] = array[right_pointer], array[index + 1]
    return index + 1


def quicksort(array, right_pointer=None, left_pointer=0):
    """Sort array in place using QuickSort"""
    if not right_pointer:
        right_pointer = len(array) - 1

    if right_pointer <= left_pointer:
        return

    pivot_index = _partition(array, right_pointer, left_pointer)

    quicksort(array, pivot_index - 1, left_pointer)
    quicksort(array, right_pointer, pivot_index + 1)
