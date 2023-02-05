# Author: Isaac Johnson
# GitHub Username: Johnsonisaacn
# Date: 11/2/2022
# Description: creates class Person to input names and ages and function std_dev
# that calculates the standard deviation of ages pulled from a list
class Person:
    """Takes a person's name and age as input and can
    pull them using a get_age method"""

    def __init__(self, name, age):
        """Takes the name and age of the person as input"""
        self._name = name
        self._age = age

    def get_age(self):
        """Allows the user to query a person's age"""
        return self._age

def std_dev(person_list):
    """Takes a list of people's ages as a parameter and
    returns the standard deviation of ages"""
    ages_list = []
    for i in person_list:
        age = i.get_age()
        ages_list.append(age)
    pop_size = len(ages_list)
    mean = sum(ages_list ) /pop_size
    standard_dev = (sum([( x -mean )**2 for x in ages_list] ) /pop_size )**0.5
    return standard_dev