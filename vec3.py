import math
import copy
import exceptions
import functions
import vec3_gen


class Vec3(vec3_gen.GenVec3):
    """3D Vector."""
    def __init__(self, x=0.0, y=0.0, z=0.0):
        vec3_gen.GenVec3.__init__(self, x, y, z)

    def from_vec2(self, v):
        self.x = v[0]
        self.y = v[1]
        self.z = 0.0

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise ValueError("Integer key in the range [0;2] required")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise ValueError("Integer key in the range [0;2] required")

    def __len__(self):
        return 3

    def __str__(self):
        return 'Vec3({}; {}; {})'.format(self.x, self.y, self.z)

    def __copy__(self):
        return Vec3(self.x, self.y, self.z)

    def __deepcopy__(self, memodict={}):
        return Vec3(self.x, self.y, self.z)

    def __add__(self, other):
        return Vec3(self.x + other[0], self.y + other[1], self.z + other[2])

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        self.z += other[2]
        return self

    def __sub__(self, other):
        return Vec3(self.x - other[0], self.y - other[1], self.z - other[2])

    def __isub__(self, other):
        self.x -= other[0]
        self.y -= other[1]
        self.z -= other[2]
        return self

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def __div__(self, scalar):
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __truediv__(self, scalar):
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __idiv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        return self

    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        return self

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        return functions.almost_equal(self.x, other[0]) and \
               functions.almost_equal(self.y, other[1]) and \
               functions.almost_equal(self.z, other[2])

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if functions.almost_equal(self.x, other[0]):
            if functions.almost_equal(self.y, other[1]):
                return self.z < other[2]
            return self.y < other[1]
        return self.x < other[0]

    def __gt__(self, other):
        if functions.almost_equal(self.x, other[0]):
            if functions.almost_equal(self.y, other[1]):
                return self.z > other[2]
            return self.y > other[1]
        return self.x > other[0]

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def length_squared(self):
        """Calculates squared length of a vector."""
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self):
        """Calculates length of a vector."""
        return math.sqrt(self.length_squared())

    def normalize(self):
        """Performs vector normalization. Raises VectorException in case of zero length."""
        ls = self.length_squared()
        if ls == 0.0:
            raise exceptions.VectorException("Zero-length normalization")
        l = math.sqrt(ls)
        self.x /= l
        self.y /= l
        self.z /= l

    def get_normalized(self):
        """Returns normalized copy of a vector. Raises VectorException in case of zero length."""
        c = copy.copy(self)
        c.normalize()
        return c

    def dot(self, v2):
        """Calculated dot product of current vector and vector v2."""
        return self.x * v2[0] + self.y * v2[1] + self.z * v2[2]

    def cross(self, v2):
        """Calculated cross product. The result is a vector perpendicular to the current
        vector and vector v2."""
        return Vec3(self.y * v2[2] - self.z * v2[1],
                    self.z * v2[0] - self.x * v2[2],
                    self.x * v2[1] - self.y * v2[0])
