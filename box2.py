import sys
import copy
from vec2 import Vec2
from functions import almost_equal


class Box2(object):
    """2D box."""
    def __init__(self, min_pt=Vec2(sys.float_info.max, sys.float_info.max),
                 max_pt=Vec2(sys.float_info.min, sys.float_info.min)):
        self.__min = Vec2(min_pt[0], min_pt[1])
        self.__max = Vec2(max_pt[0], max_pt[1])
        if not self.is_empty():
            self.__correct_box()

    def __correct_box(self):
        tmin = copy.copy(self.__min)
        tmax = copy.copy(self.__max)
        self.__min = Vec2(min(tmin.x, tmax.x), min(tmin.y, tmax.y))
        self.__max = Vec2(max(tmin.x, tmax.x), max(tmin.y, tmax.y))

    def is_empty(self):
        """Checks if the box is in empty state."""
        return almost_equal(self.__min.x, sys.float_info.max) and almost_equal(self.__min.y, sys.float_info.max) and \
               almost_equal(self.__max.x, sys.float_info.min) and almost_equal(self.__max.y, sys.float_info.min)

    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, value):
        self.__min = Vec2(value[0], value[1])
        self.__correct_box()

    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, value):
        self.__max = Vec2(value[0], value[1])
        self.__correct_box()

    def __getitem__(self, key):
        if key == 0:
            return self.__min
        elif key == 1:
            return self.__max
        else:
            raise ValueError("Integer key in the range [0;1] required.")

    def __setitem__(self, key, value):
        if len(value) < 2:
            raise ValueError("Value length must be 2 at least.")
        if key == 0:
            self.min = Vec2(value[0], value[1])
        elif key == 1:
            self.max = Vec2(value[0], value[1])
        else:
            raise ValueError("Integer key in the range [0;1] required.")

    def __len__(self):
        return 2

    def __str__(self):
        return 'Box2({}; {})'.format(self.__min, self.__max)

    def __copy__(self):
        return Box2(copy.copy(self.min), copy.copy(self.max))

    def __deepcopy__(self, memodict={}):
        return Box2(copy.copy(self.min), copy.copy(self.max))

    def __eq__(self, other):
        return self.__min == other.__min and self.__max == other.__max

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def left_top(self):
        return Vec2(self.__min.x, self.__max.y)

    @property
    def right_top(self):
        return copy.copy(self.__max)

    @property
    def right_bottom(self):
        return Vec2(self.__max.x, self.__min.y)

    @property
    def left_bottom(self):
        return copy.copy(self.__min)

    @property
    def center(self):
        return (self.__min + self.max) * 0.5

    @property
    def size_x(self):
        return self.__max.x - self.__min.x

    @property
    def size_y(self):
        return self.__max.y - self.__min.y

    @property
    def size(self):
        return Vec2(self.size_x, self.size_y)

    def is_intersect(self, box):
        """Checks intersection of 2 boxes."""
        return not (self.__max.x < box.min.x or self.__min.x > box.max.x or
                    self.__max.y < box.min.y or self.__min.y > box.max.y)

    def is_point_inside(self, pt):
        """Checks if a point is inside the box. Edges of the box are considered."""
        return not (self.__min.x > pt[0] or pt[0] > self.__max.x or self.__min.y > pt[1] or pt[1] > self.__max.y)

    def is_point_strict_inside(self, pt):
        """Checks if a point is inside the box. Edges of the box are not considered."""
        return not (self.__min.x >= pt[0] or pt[0] >= self.__max.x or self.__min.y >= pt[1] or pt[1] >= self.__max.y)

    def is_box_inside(self, box):
        """Checks if a box in inside this box."""
        return self.is_point_inside(box.min) and self.is_point_inside(box.max)
