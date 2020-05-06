"""
 Bubble sort algorithm:
   iterates over the list comparing each pair and swapping elements
   if out of order. Keeps iterations until no more swaps are done
"""


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

l1 = []
l2 = [3]
l3 = [1, -22, 3.8, 1.6]
l4 = [2, 3, 1]
l5 = [6, 5]

print(bubble_sort(l3))

