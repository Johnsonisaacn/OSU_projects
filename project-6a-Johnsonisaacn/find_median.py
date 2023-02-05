# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 11/2/2022
# Description: returns the median value of a list inputed into the function
def find_median(num_list):
    """This function takes a list of numbers as a parameter
    and returns the element of the list with
    the median value """
    middle = int(len(num_list)/2)
    median = 0
    sorted_list = sorted(num_list)
    if len(sorted_list)%2 == 0:
        middle_low = int(len(num_list)/2) - 1
        middle_hi = int(len(num_list)/2)
        median = (sorted_list[middle_low] + sorted_list[middle_hi])/2
    else:
        middle = int((len(num_list)+1)/2) - 1
        median = sorted_list[middle]
    return median