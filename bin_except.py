# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 1/31/2023
# Description: binary search function but with an exception raised if the
# search target isn't found

class TargetNotFound(Exception):
    """exception for search target not being found by the binary search"""
    pass

def bin_except(a_list, target):
    """
      Searches a_list for an occurrence of target
      If found, returns the index of its position in the list
      If not found, returns -1, indicating the target value isn't in the list
      """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
        if first == last:
            if a_list[first] != target:
                print("Target not found")
                raise TargetNotFound



