#!/usr/bin/env python3


class Score(object):

    def __init__(self, goals=0, points=0):
        self.points = points
        self.goals = goals

    def __str__(self):
        return '{:d} goal(s) and {:d} point(s)'.format(self.goals, self.points)

    def __eq__(self, other):
        return self.overall_points() == other.overall_points()

    def __gt__(self, other):
        return self.overall_points() > other.overall_points()

    def __lt__(self, other):
        return self.overall_points() < other.overall_points()

    def __ge__(self, other):
        return self.overall_points() >= other.overall_points()

    def __le__(self, other):
        return self.overall_points() <= other.overall_points()

    def __add__(self, other):
        return Score(self.goals + other.goals, self.points + other.points)

    def __sub__(self, other):
        return Score(self.goals - other.goals, self.points - other.points)

    def __iadd__(self, other):
        z = self + other
        self.goals, self.points = z.goals, z.points
        return self

    def __isub__(self, other):
        z = self - other
        self.goals, self.points = z.goals, z.points
        return self

    def __mul__(self, other):
        return Score(self.goals * other, self.points * other)

    def __rmul__(self, other):
        return Score(self.goals * other, self.points * other)

    def __imul__(self, other):
        z = self * other
        self.goals, self.points = z.goals, z.points
        return self

    def overall_points(self):
        return int((self.goals * 3) + self.points)
