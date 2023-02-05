# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 10/19/2022
# Description: a function that takes a positive integer as input and returns the
# corresponding value of the Fibonacci Sequence

def fib(term):
    """Function fib takes a positive integer, term, as a parameter and
    returns the corresponding value of the Fibonacci Sequence starting
    with 1
    """
    num1 = 0
    num2 = 1
    for integer in range(2, term+1):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    return num2

