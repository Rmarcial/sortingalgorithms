"""
 Bubble sort algorithm:
   iterates over the list comparing each pair and swapping elements
   if out of order. Keeps iterations until no more swaps are done
"""
import random
import time


def bubble_sort(lst):
    """
    Sorts a list
    Complexity: O(n²)
    :param lst:
    :return: sorted list
    """

    def swap(a, b):
        lst[a], lst[b] = lst[b], lst[a]

    size = len(lst)

    if size <= 1:
        return lst

    else:
        swapped = True  # at least one iteration
        while swapped:
            swapped = False
            for i in range(size - 1):  # from 0 to before last element
                if lst[i] > lst[i + 1]:
                    swap(i, i + 1)
                    swapped = True
    return lst


# Tests
print()

list_size = 1000
max_rand = 500
numbers = []

for n in range(list_size):
    numbers.append(random.randint(0, max_rand))

start = time.clock()
bubble_sort(numbers)
stop = time.clock()

print("bubble sort:", stop - start, "seg")
