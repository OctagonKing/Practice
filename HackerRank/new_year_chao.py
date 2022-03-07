# -*- coding: utf-8 -*-
# It is New Year's Day and people are in line for the Wonderland rollercoaster
# ride. Each person wears a sticker indicating their initial position in the
# queue from 1 to n. Any person can bribe the person directly in front of them
# to swap positions, but they still wear their original sticker. One person can
# bribe at most two others.
# Determine the minimum number of bribes that took place to get to a given
# queue order. Print the number of bribes, or, if anyone has bribed more than
# two people, print Too chaotic.


def minimumBribes(q):
    """
    Print the status of q

    >>> q = [1, 2, 5, 3, 7, 8, 6, 4]
    >>> minimumBribes(q)
    7
    >>> q2 = [2, 5, 1, 3, 4]
    >>> minimumBribes(q2)
    Too chaotic
    """
    # Write your code here
    count = 0
    for i in range(len(q)):
        suppose_pos = q[i] - 1
        if suppose_pos - i > 2:
            print("Too chaotic")
            return
        for j in range(max(suppose_pos - 1, 0), i):
            if q[j] > q[i]:
                count += 1
    print(count)
