import math
import copy
import geom_exceptions
import functions
import vec2_gen


class Vec2(vec2_gen.GenVec2):
    """2D Vector."""
    def __init__(self, x=0.0, y=0.0):
        vec2_gen.GenVec2.__init__(self, x, y)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise ValueError("Integer key in the range [0;1] required")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise ValueError("Integer key in the range [0;1] required")

    def __len__(self):
        return 2

    def __str__(self):
        return 'Vec2({}; {})'.format(self.x, self.y)

    def __copy__(self):
        return Vec2(self.x, self.y)

    def __deepcopy__(self, memodict={}):
        return Vec2(self.x, self.y)

    def __add__(self, other):
        return Vec2(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self

    def __sub__(self, other):
        return Vec2(self.x - other[0], self.y - other[1])

    def __isub__(self, other):
        self.x -= other[0]
        self.y -= other[1]
        return self

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __div__(self, scalar):
        return Vec2(self.x / scalar, self.y / scalar)

    def __truediv__(self, scalar):
        return Vec2(self.x / scalar, self.y / scalar)

    def __idiv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __eq__(self, other):
        return functions.almost_equal(self.x, other[0]) and functions.almost_equal(self.y, other[1])

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if functions.almost_equal(self.x, other[0]):
            return self.y < other[1]
        return self.x < other[0]

    def __gt__(self, other):
        if functions.almost_equal(self.x, other[0]):
            return self.y > other[1]
        return self.x > other[0]

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def length_squared(self):
        """Calculates squared length of a vector."""
        return self.x * self.x + self.y * self.y

    def length(self):
        """Calculates length of a vector."""
        return math.sqrt(self.length_squared())

    def normalize(self):
        """Performs vector normalization. Raises VectorException in case of zero length."""
        ls = self.length_squared()
        if ls == 0.0:
            raise geom_exceptions.VectorException("Zero-length normalization")
        l = math.sqrt(ls)
        self.x /= l
        self.y /= l

    def get_normalized(self):
        """Returns normalized copy of a vector. Raises VectorException in case of zero length."""
        c = copy.copy(self)
        c.normalize()
        return c

    def dot(self, v2):
        """Calculated dot product of current vector and vector v2."""
        return self.x * v2[0] + self.y * v2[1]

    def cross(self, v2):
        """Calculates cross product. It's a scalar which absolute value equals to
        square of a parallelogram constructed on the current vector and vector v2.
        The sign tells either v2 is on the left side (positive value) of the current
        vector or on the right side (negative value)."""
        return self.x * v2[1] - self.y * v2[0]

    @property
    def left_normal(self):
        """Calculates left normal vector to the current vector."""
        return Vec2(-self.y, self.x)

    @property
    def right_normal(self):
        """Calculates right normal vector to the current vector."""
        return Vec2(self.y, -self.x)
