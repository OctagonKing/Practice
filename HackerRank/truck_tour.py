# -*- coding: utf-8 -*-
def truckTour(petrolpumps):
    """
    Return the first index that the truck can go through all the pumps
    each row represents a pump, with [a,b], a is amount of petrol, b is distance
    to next pump
    the truck will go as a circle

    >>> p = [[1, 5], [10, 3], [3, 4]]
    >>> truckTour(p)
    1
    """
    # Write your code here
    start = 0
    start_candidates = []
    while start < len(petrolpumps):
        cur_info = petrolpumps[start]
        if cur_info[0] >= cur_info[1]:
            start_candidates.append(start)
        start += 1

    for can in start_candidates:
        acc = petrolpumps[can][0]
        acc -= petrolpumps[can][1]
        # if acc < 0:
        #     continue
        i = 1
        while i <= len(petrolpumps) - 1 and acc >= 0:
            check = can + i
            if check >= len(petrolpumps):
                check -= len(petrolpumps)
            acc += petrolpumps[check][0]
            acc -= petrolpumps[check][1]
            i += 1
        if i == len(petrolpumps):
            return can
