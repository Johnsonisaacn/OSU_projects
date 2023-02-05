# Author: Isaac Johnson
# Github Username: Johnsonisaacn
# Date: 11/5/2022
# Description: Takes a list and returns it in the reverse order
def reverse_list(new_list=None):
    """Function takes a list as a parameter and returns the list in reverse order"""
    if new_list is None:
        new_list = []
    list_length = len(new_list)
    for i in range(len(new_list)):
        new_list.append(0)
    for i in range(len(new_list)):
        new_list[-i-1] = new_list[i]
    while len(new_list) > list_length:
        del new_list[0]
    return new_list


