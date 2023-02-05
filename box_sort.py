# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 1/31/2023
# Description: this program creates a box class and a sort function

class Box:
    """creates a box object from parameters length, width, and height. has a function to calculate and
    return volume of the box object"""

    def __init__(self, length, width, height):
        """initializes data members"""

        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """returns the length dimension"""

        return self._length

    def get_width(self):
        """returns the width dimension"""

        return self._width

    def get_height(self):
        return self._height

    def volume(self):
        """returns volume of box object"""

        return (self._length * self._width * self._height)

def box_sort(box_list):
    """Sorts a list of box objects in ascending order of volume"""
    for box in range(1, len(box_list)):
        value = box_list[box].volume()
        box_object = box_list[box]
        pos = box - 1
        while pos >= 0 and box_list[pos].volume() < value:
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = box_object
    return box_list





