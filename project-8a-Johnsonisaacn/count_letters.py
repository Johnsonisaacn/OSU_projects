# Author: Isaac Johnson
# GitHub UserID: Johnsonisaacn
# Date: 11/16/2022
# Description: takes a string as input and creates a dictionary with the letters in the string
# and how many of that letter the string contains
def count_letters(new_str):
    """
    this function takes a string as a parameter and returns a dictionary where the keys are upper-case
    letters found in the string and the values are the number of times that letter appears
    """
    letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    new_set = set()
    new_dict = {}
    for i in new_str:
        i = i.upper()
        if i in letter_list:
            new_set.add(i)
    for i in new_set:
        counter = 0
        for letter in new_str:
            if letter.upper() == i:
                counter += 1
        new_dict[i] = counter
    return new_dict
