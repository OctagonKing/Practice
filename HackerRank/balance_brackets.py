# -*- coding: utf-8 -*-

# Application of stack


def isBalanced(s):
    """
    Return a string containing brackets only is balanced or not.

    >>> s1 = "{(([])[])[]}[]"
    >>> isBalanced(s1)
    'YES'
    """
    # Write your code here
    if len(s) % 2 == 1:
        return "NO"
    left = "{[("
    match = {"}": "{", "]": "[", ")": "("}
    stack = []
    for char in s:
        if char in left:
            stack.append(char)
        else:
            if stack == [] or stack.pop() != match[char]:
                return "NO"
    if stack:
        return "NO"
    return "YES"
