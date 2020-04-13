'''
Assume array is sorted, return True if target is in the array
'''


import random


def binary_search(array, target):
    # Set boundaries for low and high marks to search
    low = 0
    high = len(array)
    # While low and high do not overlap...
    while low < high:
        # Check the midpoint
        midpoint = (low + high) // 2
        print(midpoint)
        # If it's equal, return True
        if array[midpoint] == target:
            return True
        # Else, if target is smaller
        elif target < array[midpoint]:
            # set the high to midpoint value
            high = midpoint - 1
        # Else if target is bigger
        else:
            # set the low to midpoint value
            low = midpoint + 1
    # If we get to the end, return False
    return False


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(a, 6)

# Take unsorted array and return sorted array


def insertion_sort(array):
    # Divide your hand into sorted on the left and unsorted on the right
    # Sorted is just the first element
    # then go card by card and move them into place.
    # Loop through all elements in unsorted...
    for i in range(1, len(array)):
        temp = array[i]
        j = i  # j is our sliding index
        # Shift sorted to the right until correct position found
        while j > 0 and temp < array[j - 1]:
            array[j] = array[j - 1]  # Slide over one element
            j -= 1
        # Insert at that position
        array[j] = temp
        print(array)
    return array


array = list(range(1, 11))
random.shuffle(array)
insertion_sort(array)
