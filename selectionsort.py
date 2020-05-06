"""
 Selection sort algorithm:
   in each iteration over the list finds the minimum element and substitutes
   for the first non sorted position. Ex: 1st iteration puts min in list[0}
"""


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
        i_min = low
        for i in range(low, high):
            if lst[i] < lst[i_min]:
                i_min = i
        return i_min

    size = len(lst)

    for index in range(size):
        swap(index, index_min(index, size))

    return lst


# Tests

l1 = []
l2 = [3]
l3 = [1, -22, 3.8, 1.6]
l4 = [2, 3, 1]
l5 = [6, 5]

print(selection_sort(l1))
print(selection_sort(l2))
print(selection_sort(l3))
print(selection_sort(l4))
print(selection_sort(l5))