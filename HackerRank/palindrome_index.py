# -*- coding: utf-8 -*-
# Given a string of lowercase letters in the range ascii[a-z], determine the
# index of a character that can be removed to make the string a palindrome.
# There may be more than one solution, but any will do. If the word is already
# a palindrome or there is no solution, return -1. Otherwise, return the index
# of a character to remove.


def palindrome_index(s):
    """
    Return -1 if s is palindrome or there is no solution
    return the index if can get a palindrome with removing the char

    >>> palindrome_index("aaab")
    3
    >>> palindrome_index("bcbc")
    0
    """
    if s == s[::-1]:
        return -1
    front_pt = 0
    end_pt = len(s) - 1
    # Find the place that the character differs
    while front_pt < end_pt:
        if s[front_pt] != s[end_pt]:
            break
        front_pt += 1
        end_pt -= 1
    # Remove either one to check whether it satisfies the palindrome
    if s[front_pt + 1: end_pt + 1] == s[front_pt + 1: end_pt + 1][::-1]:
        return front_pt
    elif s[front_pt: end_pt] == s[front_pt: end_pt][::-1]:
        return end_pt
    # If it still cannot form a palindrome, then there is no solution
    else:
        return -1

