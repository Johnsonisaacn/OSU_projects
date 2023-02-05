# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 10/19/2022
# Description: defining a function fall_distance that takes the time
# in seconds as input and gives the distance an object has fallen in meters

def fall_distance(seconds):
    """This function takes time in seconds as a parameter and calculates the
    distance an object has fallen in meters
    """
    GRAVITY = 9.8
    distance = 0.5 * GRAVITY * seconds ** 2
    return distance

