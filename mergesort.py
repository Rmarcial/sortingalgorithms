"""
 Merge sort algorithm:
  divides the list in sublists, sorts all the sublists and merges the already
  sorted sublists in order
"""

import random
import time


def merge_sort(lst):
    """
    Sorts a list
    Complexity: O(n log n)
    :param lst:
    :return: sorted list
    """

    size = len(lst)

    if size <= 1:
        return lst

    else:
        middle = size // 2
        return merge(merge_sort(lst[:middle]), merge_sort(lst[middle:]))


# merges two ordered lists in an ordered list
def merge(lst_a, lst_b):

    if not lst_a:
        return lst_b

    elif not lst_b:
        return lst_a

    else:
        if lst_a[0] < lst_b[0]:
            return lst_a[:1] + merge(lst_a[1:], lst_b)
        else:
            return lst_b[:1] + merge(lst_a, lst_b[1:])


# Tests
print()

list_size = 1000
max_rand = 500
numbers = []

for n in range(list_size):
    numbers.append(random.randint(0, max_rand))

start = time.clock()
merge_sort(numbers)
stop = time.clock()

print("merge sort:", stop - start, "seg")

