from vec2 import Vec2
from functions import almost_equal
from line2 import Line2
from geom_exceptions import TriangleException
import copy
import math


class Tri2(object):
    """2D triangle."""
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

    def edge(self, index):
        """Returns an edge of triangle as 2D line. Index must be in the range [0;2]."""
        if index < 0 or index > 2:
            raise ValueError("Index must be in the range [0;2]")
        return Line2(self.points[index], self.points[(index + 1) % 3])

    def distance_squared(self, pt):
        """Returns the shortest squared distance between point pt and the triangle."""
        min_dist = self.edge(0).distance_squared(pt)
        for i in range(1, 3):
            d = self.edge(i).distance_squared(pt)
            if d < min_dist:
                min_dist = d
        return min_dist

    def nearest_edge_index(self, pt):
        """Returns index of the nearest edge to point pt."""
        min_index = 0
        min_dist = self.edge(min_index).distance_squared(pt)
        for i in range(1, 3):
            d = self.edge(i).distance_squared(pt)
            if d < min_dist:
                min_dist = d
                min_index = i
        return min_index

    def distance(self, pt):
        """Returns the shortest distance between point pt and the triangle."""
        return math.sqrt(self.distance_squared(pt))

    def square(self):
        """Calculates square of the triangle."""
        a = self.edge(0).length()
        b = self.edge(1).length()
        c = self.edge(2).length()
        p = (a + b + c) * 0.5
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def get_point_inside(self, barycentric):
        """Calculates a point inside triangle by means of barycentric coordinates.
        Sum of barycentric coordinates must be equal to 1."""
        if not almost_equal(barycentric[0] + barycentric[1] + barycentric[2], 1.0):
            raise ValueError("Sum of barycentric coordinates must be equal to 1.")
        return self.points[0] * barycentric[0] + self.points[1] * barycentric[1] + self.points[2] * barycentric[2]

    def incenter(self):
        """Calculates incenter of the triangle."""
        a = self.edge(1).length()
        b = self.edge(2).length()
        c = self.edge(0).length()
        p = a + b + c
        if p == 0.0:
            return self.points[0]
        return (self.points[0] * a + self.points[1] * b + self.points[2] * c) / p

    def incircle_radius(self):
        """Calculates incircle radius of the triangle."""
        a = self.edge(0).length()
        b = self.edge(1).length()
        c = self.edge(2).length()
        p = (a + b + c) * 0.5
        if p == 0.0:
            return 0.0
        return math.sqrt((p - a) * (p - b) * (p - c) / p)

    def circumcenter(self):
        """Calculates circumcenter of the triangle. TriangleException raises if the triangle is degenerate."""
        p01 = self.points[0] - self.points[1]
        p02 = self.points[0] - self.points[2]
        p12 = self.points[1] - self.points[2]
        d = 2.0 * (self.points[0].x * p12.y - self.points[1].x * p02.y + self.points[2].x * p01.y)
        if d == 0.0:
            raise TriangleException("Circumcenter couldn't be calculated for a degenerate triangle")
        l0 = self.points[0].length_squared()
        l1 = self.points[1].length_squared()
        l2 = self.points[2].length_squared()
        x = (l0 * p12.y - l1 * p02.y + l2 * p01.y) / d
        y = (l1 * p02.x - l0 * p12.x - l2 * p01.x) / d
        return Vec2(x, y)

    def circumcircle_radius(self):
        """Calculates circumcircle radius of the triangle. TriangleException raises if the triangle is degenerate."""
        a = self.edge(0)
        b = self.edge(1)
        c = self.edge(2)
        d = 2.0 * math.fabs(a.as_vector().cross(b.as_vector()))
        if d == 0.0:
            raise TriangleException("Circumcircle radius couldn't be calculated for a degenerate triangle")
        return a.length() * b.length() * c.length() / d

    def get_connectivity(self, other):
        """Calculated connectivity between 2 triangles. The result is array of integers.
        Each pair is indices of connected edges. It there are 6 indices in the array then the triangle covers
        the same area."""
        result = []
        for i in range(0, 3):
            for j in range(0, 3):
                edge1 = self.edge(i)
                edge2 = other.edge(j)
                if edge1 == edge2 or edge1 == -edge2:
                    result.append(i)
                    result.append(j)
        return result

