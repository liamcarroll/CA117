#!/usr/bin/env python3


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)

    def midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)


class Circle(object):

    def __init__(self, centre=Point(0, 0), radius=0):
        self.centre = centre
        self.radius = radius

    def __str__(self):
        return 'Centre: {}\nRadius: {:d}'.format(self.centre, self.radius)

    def __add__(self, other):
        centre = self.centre.midpoint(other.centre)
        radius = self.radius + other.radius
        return Circle(centre, radius)
