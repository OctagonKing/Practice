# -*- coding: utf-8 -*-
# !/bin/python3

# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
# Given a 2n * 2n matrix, find a maximum of sum of upper-left n*n matrix


# Key point: consider what is the candidates for each value in the final matrix
def flippingMatrix(matrix):
    """
    flip the matrix to find the maximum sum of upper left n*n matrix

    >>> m1 = [[1, 2], [3, 4]]
    >>> flippingMatrix(m1)
    4
    >>> m2 = [[1,2,4,3], [5,6,7,8], [11,12,9,10], [13,14,15,16]]
    >>> flippingMatrix(m2)
    54
    >>> m3 = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    >>> flippingMatrix(m3)
    414
    """
    size = len(matrix)
    n = size // 2
    result = 0
    for i in range(n):
        for j in range(n):
            candidates = [matrix[i][j], matrix[i][-j - 1],
                          matrix[-i - 1][j], matrix[-i - 1][-j - 1]]
            result += max(candidates)
    return result


# Wrong answer below
def flip_matrix(matrix):
    """
    flip the matrix to find the maximum sum of upper left n*n matrix

    >>> m1 = [[1, 2], [3, 4]]
    >>> flippingMatrix(m1)
    4
    >>> m2 = [[1,2,4,3], [5,6,7,8], [11,12,9,10], [13,14,15,16]]
    >>> flippingMatrix(m2)
    54
    >>> m3 = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    >>> flippingMatrix(m3)
    414
    """

    size = len(matrix)
    n = size // 2
    # test1: flip row first then flip column
    test1 = matrix.copy()
    for i in range(size):
        row = test1[i]
        first = sum(row[:n])
        second = sum(row[n:])
        if first < second:
            test1[i].reverse()

    for i in range(n):
        col = []
        for j in range(size):
            col.append(test1[j][i])
        first = sum(col[:n])
        second = sum(col[n:])
        if first < second:
            reverse_col(test1, i)

    result1 = cal_upper(test1)

    # test2: flip column first then flip row
    test2 = matrix.copy()
    for i in range(size):
        col = []
        for j in range(size):
            col.append(test2[j][i])
        first = sum(col[:n])
        second = sum(col[n:])
        if first < second:
            reverse_col(test2, i)

    for i in range(n):
        row = test2[i]
        first = sum(row[:n])
        second = sum(row[n:])
        if first < second:
            test2[i].reverse()

    result2 = cal_upper(test2)

    return max(result1, result2)


def cal_upper(matrix):
    size = len(matrix)
    n = size // 2
    result = 0
    for i in range(n):
        for j in range(n):
            result += matrix[i][j]
    return result


def reverse_col(matrix, i):
    size = len(matrix)
    n = size // 2
    for index in range(n):

        matrix[index][i], matrix[-index - 1][i] = matrix[-index - 1][i], \
                                                  matrix[index][i]


if __name__ == '__main__':
    m3 = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43],
          [62, 98, 114, 108]]
    flip_matrix(m3)
    print(m3)
    print(flip_matrix(m3))
