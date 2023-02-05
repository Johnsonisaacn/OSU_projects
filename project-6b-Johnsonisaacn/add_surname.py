# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 11/2/2022
# Description: adds the Surname Kardashian to names that start with K from a list input
def add_surname(fn_list):
    """This function takes a list of first names as a parameter and
    returns all names that start with the letter K with the surname
    Kardashian affixed to it"""
    k_names = []
    full_names = []
    [k_names.append(i) for i in fn_list if i[0] == "K"]
    full_names = [f+" Kardashian" for f in k_names]
    return full_names