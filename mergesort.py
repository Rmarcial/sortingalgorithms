"""
 Merge sort algorithm:
  divides the list in sublists, sorts all the sublists and merges the already
  sorted sublists in order
"""


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

l1 = []
l2 = [3]
l3 = [1, -22, 3.8, 1.6]
l4 = [2, 3, 1]
l5 = [6, 5]

print(merge_sort(l1))
print(merge_sort(l2))
print(merge_sort(l3))
print(merge_sort(l4))
print(merge_sort(l5))

