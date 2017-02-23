from vec2 import Vec2
from functions import lerp
import copy
import math


class Line2(object):
    def __init__(self, p1, p2):
        if len(p1) < 2 or len(p2) < 2:
            raise ValueError("Length of p1, p2 must be 2 at least.")
        self.points = [Vec2(p1[0], p1[1]), Vec2(p2[0], p2[1])]

    def __getitem__(self, key):
        if key < 0 or key > 1:
            raise ValueError("Integer key in the range [0;1] required.")
        return self.points[key]

    def __setitem__(self, key, value):
        if len(value) < 2:
            raise ValueError("Value length must be 2 at least.")
        if key < 0 or key > 1:
            raise ValueError("Integer key in the range [0;1] required.")
        self.points[key] = Vec2(value[0], value[1])

    def __len__(self):
        return 2

    def __str__(self):
        return 'Line2({}; {})'.format(self.points[0], self.points[1])

    def __copy__(self):
        return Line2(copy.copy(self.points[0]), copy.copy(self.points[1]))

    def __deepcopy__(self, memodict={}):
        return Line2(copy.deepcopy(self.points[0]), copy.deepcopy(self.points[1]))

    def __neg__(self):
        return Line2(self.points[1], self.points[0])

    def __eq__(self, other):
        return self.points[0] == other[0] and self.points[1] == other[1]

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def direction(self):
        return (self.points[1] - self.points[0]).get_normalized()

    @property
    def left_normal(self):
        return self.direction.left_normal

    @property
    def right_normal(self):
        return self.direction.right_normal

    def projection_coef(self, pt):
        """Returns the coefficient of projection point pt to this line. The valid result is in the range [0.0;1.0].
        If the result is less than 0.0 or more than 1.0, there is no projection the point to this line."""
        v2 = self.points[1] - self.points[0]
        l = v2.length_squared()
        if l == 0.0:
            return 0.0
        return (pt - self.points[0]).dot(v2) / l

    def project(self, proj_coef):
        """Returns the 2D point projected to the line according to projection coefficient proj_coef.
        The coefficient must be in the range [0.0;1.0] otherwise ValueError raises."""
        if proj_coef < 0.0 or proj_coef > 1.0:
            raise ValueError("proj_coef must be in the range [0.0;1.0]")
        return lerp(self.points[0], self.points[1], proj_coef)

    def project_point(self, pt):
        """Returns the projection of 2D point pt to the line. The result may be None in the case then
        there is no projection the point to this line."""
        try:
            return self.project(self.projection_coef(pt))
        except ValueError:
            return None

    def distance_squared(self, pt):
        """Returns the shortest squared distance between the point pt and the line."""
        v2 = self.points[1] - self.points[0]
        l = v2.length_squared()
        if l == 0.0:
            return (pt - self.points[0]).length_squared()
        cp = (Vec2(pt[0], pt[1]) - self.points[0]).cross(v2)
        return cp * cp / l

    def distance(self, pt):
        """Returns the shortest distance between the point pt and the line."""
        return math.sqrt(self.distance_squared(pt))
