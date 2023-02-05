# Author - Isaac Johnson
# GitHub username - Johnsonisaacn
# Date - 10/26/2022
# Description - recursive program that calculates the product of two positive integers input
# by user, without using multiplication function

def multiply(num1,num2):
    """
    This function takes two positive integers as input
    and finds the product of the two using recursion
    """
    if num1 == 1:
        return num2
    num1 -= 1
    return num2 + multiply(num1,num2)
