"""
 Selection sort algorithm:
   in each iteration over the list finds the minimum element and puts it in
   the first non sorted position.
   After n iterations, the first n elements are sorted
"""

import random
import time


def selection_sort(lst):
    """
    Sorts a list
    Complexity: O(n²)
    :param lst:
    :return: sorted list
    """

    def swap(a, b):
        lst[a], lst[b] = lst[b], lst[a]

    # returns index of the minimum element in the list (from low to high-1)
    def index_min(low, high):
        idx = low
        for i in range(low, high):
            if lst[i] < lst[idx]:
                idx = i
        return idx

    size = len(lst)

    for index in range(size):
        swap(index, index_min(index, size))

    return lst


# Tests
print()

list_size = 1000
max_rand = 500
numbers = []

for n in range(list_size):
    numbers.append(random.randint(0, max_rand))

start = time.clock()
selection_sort(numbers)
stop = time.clock()

print("selection sort:", stop - start, "seg")

