# -*- coding: utf-8 -*-
# Given two arrays A and B of length N, determine if there is a way to make A
# equal to B by reversing any subarrays from array B any number of times.
from collections import Counter

def are_they_equal(array_a, array_b):
    """return True if they are equal by reversing sub-lists

    >>> are_they_equal([1, 2, 3, 4], [1, 4, 3, 2])
    True

    """
    return Counter(array_a) == Counter(array_b)
