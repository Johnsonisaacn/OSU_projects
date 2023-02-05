# Author: Isaac Johnson
# GitHub UserID: Johnsonisaacn
# Date: 11/23/2022
# Description: two classes, Point and LineSegment, that take coordinates as parameters and calculate
# distances between points, slopes of line segments, and if two segments are parallel
class Point:
    def __init__(self, x_coord, y_coord):
        """initializes data members"""
        self._x_coord = x_coord
        self._y_coord = y_coord
    def get_x_coord(self):
        """returns x coordinate"""
        return self._x_coord
    def get_y_coord(self):
        """returns y coordinate"""
        return self._y_coord
    def distance_to(self, point2):
        """calculates the distance between two points"""
        x1 = self.get_x_coord()
        y1 = self.get_y_coord()
        x2 = point2.get_x_coord()
        y2 = point2.get_y_coord()
        distance =(((x2-x1)**2)+((y2-y1)**2))**.5
        return distance
class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        """initializes data members"""
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2
    def get_endpoint_1(self):
        """returns endpoint_1"""
        return self._endpoint_1
    def get_endpoint_2(self):
        """returns endpoint_2"""
        return self._endpoint_2
    def length(self):
        """calculates the length between two points"""
        point_1 = self.get_endpoint_1()
        point_2 = self.get_endpoint_2()
        length = Point.distance_to(point_1, point_2)
        return length
    def is_parallel_to(self, line2):
        """returns True if the two lines are parallel, False if not"""
        point1 = self.get_endpoint_1()
        point2 = self.get_endpoint_2()
        m1 = int((point2.get_y_coord() - point1.get_y_coord())/(point2.get_x_coord() - point1.get_x_coord()))
        point3 = line2.get_endpoint_1()
        point4 = line2.get_endpoint_2()
        m2 = int((point4.get_y_coord() - point3.get_y_coord()) / (point4.get_x_coord() - point3.get_x_coord()))
        if m1 == m2:
            return True
        else:
            return False

    def slope(self):
        """finds and returns the slope of two line segments"""
        point1 = self.get_endpoint_1()
        point2 = self.get_endpoint_2()
        segment_slope = (point2.get_y_coord() - point1.get_y_coord())/(point2.get_x_coord() - point1.get_x_coord())
        return segment_slope




