# Author: Isaac Johnson
# GitHub UserID: Johnsonisaacn
# Date: 11/16/2022
# Description: finds the words in common in two sentences
def words_in_both(sentence1, sentence2):
    """
    Takes two sentences as parameters and returns a set of words found in both sentences
    """
    splts1 = sentence1.split()
    splts2 = sentence2.split()
    set1 = set()
    set2 = set()
    for word in splts1:
        set1.add(word.lower())
    for word in splts2:
        set2.add(word.lower())
    union = set1 & set2
    return union