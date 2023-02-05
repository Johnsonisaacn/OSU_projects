# Author: Isaac Johnson
# GitHub Username: Johnsonisaacn
# Date: 11/5/2022
# Description: takes a list as a parameter and squares each value
def square_list(num_list=None):
    """This function takes a list of numbers and squares each number then returns the mutated
    list without printing"""
    if num_list is None:
        num_list = []
    for i in range(len(num_list)):
        num_list[i] = num_list[i] ** 2
    return num_list

