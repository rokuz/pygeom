from vec2 import Vec2
from functions import almost_equal
from line2 import Line2
import copy


class Tri2(object):
    def __init__(self, p1, p2, p3):
        if len(p1) < 2 or len(p2) < 2 or len(p3) < 2:
            raise ValueError("Length of p1, p2, p3 must be 2 at least.")
        self.points = [Vec2(p1[0], p1[1]), Vec2(p2[0], p2[1]), Vec2(p3[0], p3[1])]

    def __getitem__(self, key):
        if key < 0 or key > 2:
            raise ValueError("Integer key in the range [0;2] required.")
        return self.points[key]

    def __setitem__(self, key, value):
        if len(value) < 2:
            raise ValueError("Value length must be 2 at least.")
        if key < 0 or key > 2:
            raise ValueError("Integer key in the range [0;2] required.")
        self.points[key] = Vec2(value[0], value[1])

    def __len__(self):
        return 3

    def __str__(self):
        return 'Tri2({}; {}; {})'.format(self.points[0], self.points[1], self.points[2])

    def __copy__(self):
        return Tri2(copy.copy(self.points[0]), copy.copy(self.points[1]), copy.copy(self.points[2]))

    def __deepcopy__(self, memodict={}):
        return Tri2(copy.deepcopy(self.points[0]), copy.deepcopy(self.points[1]), copy.deepcopy(self.points[2]))

    def __eq__(self, other):
        return self.points[0] == other[0] and self.points[1] == other[1] and self.points[2] == other[2]

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_degenerate(self):
        """Checks if the triangle is degenerate."""
        p13 = self.points[0] - self.points[2]
        p23 = self.points[1] - self.points[2]
        return p13.cross(p23) == 0.0

    def is_point_inside(self, pt):
        """Checks if a point pt is inside the triangle. Edges of the triangle are considered."""
        if len(pt) < 2:
            raise ValueError("Length of pt must be 2 at least.")
        p13 = self.points[0] - self.points[2]
        p23 = self.points[1] - self.points[2]
        denom = p13.cross(p23)
        if denom == 0.0:
            return almost_equal(Line2(self.points[0], self.points[1]).distance_squared(pt), 0.0) or \
                   almost_equal(Line2(self.points[1], self.points[2]).distance_squared(pt), 0.0) or \
                   almost_equal(Line2(self.points[2], self.points[0]).distance_squared(pt), 0.0)
        pt3 = Vec2(pt[0], pt[1]) - self.points[2]
        a = pt3.cross(p23) / denom
        if a < 0.0 or a > 1.0:
            return False
        b = p13.cross(pt3) / denom
        if b < 0.0 or b > 1.0:
            return False
        c = 1.0 - a - b
        return 0.0 <= c <= 1.0

    def is_point_strict_inside(self, pt):
        """Checks if a point pt is inside the triangle. Edges of the triangle are not considered."""
        if len(pt) < 2:
            raise ValueError("Length of pt must be 2 at least.")
        p13 = self.points[0] - self.points[2]
        p23 = self.points[1] - self.points[2]
        denom = p13.cross(p23)
        if denom == 0.0:
            return False
        pt3 = Vec2(pt[0], pt[1]) - self.points[2]
        a = pt3.cross(p23) / denom
        if a <= 0.0 or a >= 1.0:
            return False
        b = p13.cross(pt3) / denom
        if b <= 0.0 or b >= 1.0:
            return False
        c = 1.0 - a - b
        return 0.0 < c < 1.0
