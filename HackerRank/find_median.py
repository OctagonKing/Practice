
# Given an array with odd number of elements. Find the median
# Application of merge sort


def find_median(arr):
    """Return the median of the arr

    >>> a1 = [1,3,2,4,5]
    >>> find_median(a1)
    3
    """
    sorted_arr = sort(arr)
    mid = len(arr) // 2
    return sorted_arr[mid]


def sort(arr):
    """Return the sorted arr

    >>> a1 = [1]
    >>> sort(a1)
    [1]
    >>> a2 = [2,1]
    >>> sort(a2)
    [1, 2]
    >>> a3 = [3,2,4,1,5]
    >>> sort(a3)
    [1, 2, 3, 4, 5]
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    first = arr[:mid]
    second = arr[mid:]
    s_first = sort(first)
    s_second = sort(second)
    f_pointer = 0
    s_pointer = 0
    result = []
    while f_pointer < len(s_first) and s_pointer < len(s_second):
        cur_f = s_first[f_pointer]
        cur_s = s_second[s_pointer]
        assert(type(cur_f) == int)
        assert(type(cur_s) == int)
        if cur_f < cur_s:
            result.append(cur_f)
            f_pointer += 1
        else:
            result.append(cur_s)
            s_pointer += 1
    result.extend(s_first[f_pointer:])
    result.extend(s_second[s_pointer:])
    return result
