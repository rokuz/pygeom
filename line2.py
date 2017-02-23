from vec2 import Vec2
from functions import lerp
import copy


class Line2(object):
    def __init__(self, p1, p2):
        assert isinstance(p1, Vec2) and isinstance(p2, Vec2)
        self.points = [p1, p2]

    def __getitem__(self, key):
        if key < 0 or key > 1:
            raise ValueError("Integer key in the range [0;1] required")
        return self.points[key]

    def __setitem__(self, key, value):
        if not isinstance(value, Vec2):
            raise TypeError("Type of value must be Vec2")
        if key < 0 or key > 1:
            raise ValueError("Integer key in the range [0;1] required")
        self.points[key] = value

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
        return (self.points[1] - self.points[0]).left_normal()

    @property
    def right_normal(self):
        return (self.points[1] - self.points[0]).right_normal()

    def projection_coef(self, pt):
        """Returns the coefficient of projection point pt to this line. The valid result is in the range [0.0;1.0].
        If the result is less than 0.0 or more than 1.0, there is no projection the point to this line."""
        v2 = self.points[1] - self.points[0]
        l = v2.length_squared()
        if l == 0.0:
            if self.points[0] == pt:
                return 0.0
            return -1.0
        return (pt - self.points[0]).dot(v2) / l

    def project(self, proj_coef):
        """Returns the 2D point projected to the line according to projection coefficient proj_coef.
        The coefficient must be in the range [0.0;1.0] otherwise ValueError raises."""
        if proj_coef < 0.0 or proj_coef > 1.0:
            raise ValueError("proj_coef must be range [0.0;1.0]")
        return lerp(self.points[0], self.points[1], proj_coef)

    def project_point(self, pt):
        """Returns the projection of 2D point pt to the line. The result may be None in the case then
        there is no projection the point to this line."""
        try:
            return self.project(self.projection_coef(pt))
        except ValueError:
            return None
