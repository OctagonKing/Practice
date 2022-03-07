# -*- coding: utf-8 -*-
#
# Given a list of n integers arr[0..(n-1)], determine the number of different
# pairs of elements within it which sum to k.
# If an integer appears in the list multiple times, each copy is considered to
# be different; that is, two pairs are considered different if one pair includes
# at least one array index which the other doesn't, even if they include the
# same values.


def numberOfWays(arr, k):
    """Return number of ways

    >>> numberOfWays([1, 2, 3, 4, 3], 6)
    2
    """
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) == k:
                print((arr[i], arr[j]))
                count += 1
    return count
