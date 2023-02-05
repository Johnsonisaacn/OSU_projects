# Author: Isaac Johnson
# Github username: Johnsonisaacn
# Date: 10/19/2022
# Definition: takes an integer as input and returns the number
# of steps taken to get to 1 in a Hailstone sequence

def hailstone(hail_num):
    """Takes a positive integer parameter, hail_num, and returns the
    number of steps taken to get to 1 from there using a Hailstone
    sequence
    """
    counter = 0
    if hail_num == 1:
        return counter
    else:
        while hail_num != 1:
            if hail_num % 2 == 0:
                hail_num = hail_num / 2
            else:
                hail_num = (hail_num * 3) + 1
            counter += 1
    return counter

