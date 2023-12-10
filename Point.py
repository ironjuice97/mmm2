
class Point:
    """ A class to represent a point in 2D space. """

    def __init__(self, x, y):
        """ Initialize the point with x and y coordinates. """
        self.x = x
        self.y = y

    def delta_x(self, other):
        """ Calculate the absolute difference in x coordinate with another point. """
        return abs(self.x - other.x)

    def delta_y(self, other):
        """ Calculate the absolute difference in y coordinate with another point. """
        return abs(self.y - other.y)

    def distance_to(self, other):
        """ Calculate the distance to another point. """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
