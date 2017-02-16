import vec2
import vec3


class GenVec3(object):
    """Generated by helpers/gen_swizzle.py"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def xx(self):
        return vec2.Vec2(self.x, self.x)

    @property
    def xxx(self):
        return vec3.Vec3(self.x, self.x, self.x)

    @property
    def xxy(self):
        return vec3.Vec3(self.x, self.x, self.y)

    @property
    def xxz(self):
        return vec3.Vec3(self.x, self.x, self.z)

    @property
    def xy(self):
        return vec2.Vec2(self.x, self.y)

    @xy.setter
    def xy(self, value):
        self.x = value[0]
        self.y = value[1]

    @property
    def xyx(self):
        return vec3.Vec3(self.x, self.y, self.x)

    @property
    def xyy(self):
        return vec3.Vec3(self.x, self.y, self.y)

    @property
    def xyz(self):
        return vec3.Vec3(self.x, self.y, self.z)

    @xyz.setter
    def xyz(self, value):
        self.x = value[0]
        self.y = value[1]
        self.z = value[2]

    @property
    def xz(self):
        return vec2.Vec2(self.x, self.z)

    @xz.setter
    def xz(self, value):
        self.x = value[0]
        self.z = value[1]

    @property
    def xzx(self):
        return vec3.Vec3(self.x, self.z, self.x)

    @property
    def xzy(self):
        return vec3.Vec3(self.x, self.z, self.y)

    @xzy.setter
    def xzy(self, value):
        self.x = value[0]
        self.z = value[1]
        self.y = value[2]

    @property
    def xzz(self):
        return vec3.Vec3(self.x, self.z, self.z)

    @property
    def yx(self):
        return vec2.Vec2(self.y, self.x)

    @yx.setter
    def yx(self, value):
        self.y = value[0]
        self.x = value[1]

    @property
    def yxx(self):
        return vec3.Vec3(self.y, self.x, self.x)

    @property
    def yxy(self):
        return vec3.Vec3(self.y, self.x, self.y)

    @property
    def yxz(self):
        return vec3.Vec3(self.y, self.x, self.z)

    @yxz.setter
    def yxz(self, value):
        self.y = value[0]
        self.x = value[1]
        self.z = value[2]

    @property
    def yy(self):
        return vec2.Vec2(self.y, self.y)

    @property
    def yyx(self):
        return vec3.Vec3(self.y, self.y, self.x)

    @property
    def yyy(self):
        return vec3.Vec3(self.y, self.y, self.y)

    @property
    def yyz(self):
        return vec3.Vec3(self.y, self.y, self.z)

    @property
    def yz(self):
        return vec2.Vec2(self.y, self.z)

    @yz.setter
    def yz(self, value):
        self.y = value[0]
        self.z = value[1]

    @property
    def yzx(self):
        return vec3.Vec3(self.y, self.z, self.x)

    @yzx.setter
    def yzx(self, value):
        self.y = value[0]
        self.z = value[1]
        self.x = value[2]

    @property
    def yzy(self):
        return vec3.Vec3(self.y, self.z, self.y)

    @property
    def yzz(self):
        return vec3.Vec3(self.y, self.z, self.z)

    @property
    def zx(self):
        return vec2.Vec2(self.z, self.x)

    @zx.setter
    def zx(self, value):
        self.z = value[0]
        self.x = value[1]

    @property
    def zxx(self):
        return vec3.Vec3(self.z, self.x, self.x)

    @property
    def zxy(self):
        return vec3.Vec3(self.z, self.x, self.y)

    @zxy.setter
    def zxy(self, value):
        self.z = value[0]
        self.x = value[1]
        self.y = value[2]

    @property
    def zxz(self):
        return vec3.Vec3(self.z, self.x, self.z)

    @property
    def zy(self):
        return vec2.Vec2(self.z, self.y)

    @zy.setter
    def zy(self, value):
        self.z = value[0]
        self.y = value[1]

    @property
    def zyx(self):
        return vec3.Vec3(self.z, self.y, self.x)

    @zyx.setter
    def zyx(self, value):
        self.z = value[0]
        self.y = value[1]
        self.x = value[2]

    @property
    def zyy(self):
        return vec3.Vec3(self.z, self.y, self.y)

    @property
    def zyz(self):
        return vec3.Vec3(self.z, self.y, self.z)

    @property
    def zz(self):
        return vec2.Vec2(self.z, self.z)

    @property
    def zzx(self):
        return vec3.Vec3(self.z, self.z, self.x)

    @property
    def zzy(self):
        return vec3.Vec3(self.z, self.z, self.y)

    @property
    def zzz(self):
        return vec3.Vec3(self.z, self.z, self.z)
