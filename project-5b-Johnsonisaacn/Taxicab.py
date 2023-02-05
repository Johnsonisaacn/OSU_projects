# Author - Isaac Johnson
# GitHub username - Johnsonisaacn
# Date - 10/26/2022
# Description - this class takes input of two integers and gives coordinates on an x/y plane
# and total distance travelled
class Taxicab:
    """
    Takes two integers as input and converts them to
    x and y coordinates on a plane. User can input movement
    on the x and y axis and can find current coordinates
    after moving and the total distance travelled.
    """
    def __init__(self, x_coord, y_coord):
        """Sets the initial coordinates from user input
        and initializes the odometer
        """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def move_x(self, x_movement):
        """Allows user to move the x coordinate and tracks
        that distance travelled in the odometer
        """
        self._x_coord = self._x_coord + x_movement
        self._odometer = self._odometer + abs(x_movement)
    def move_y(self, y_movement):
        """Allows user to move the y coordinate and tracks
        that distance travelled in the odometer
        """
        self._y_coord = self._y_coord + y_movement
        self._odometer = self._odometer + abs(y_movement)
    def get_x_coord(self):
        """Allows the user to query the x coordinate
        """
        return self._x_coord
    def get_y_coord(self):
        """Allows the user to query the y coordinate
        """
        return self._y_coord
    def get_odometer(self):
        """Allows the user to query the total distance travelled
        """
        return self._odometer
