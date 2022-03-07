# -*- coding: utf-8 -*-

# You are given an array arr of N integers. For each index i, you are required
# to determine the number of contiguous subarrays that fulfill the following
# conditions:
# The value at index i must be the maximum element in the contiguous subarrays,
# and these contiguous subarrays must either start from or end on index i.


def count_subarrays(arr):
    """
    Return count list for arr

    >>> count_subarrays([3, 4, 1, 6, 2])
    [1, 3, 1, 5, 1]
    """
    result = []
    for i in range(len(arr)):
        count = 0
        first = 0
        while first < i:
            if max(arr[first:(i+1)]) == arr[i]:
                count += 1
            first += 1
        last = i+1
        # print("first count: " + str(count))
        while last < len(arr)+1:
            if max(arr[i: last]) == arr[i]:
                count += 1
            last += 1
        result.append(count)
    return result

if __name__ == "__main__":
    pass
