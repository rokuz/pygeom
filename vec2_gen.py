import vec2


class GenVec2(object):
    """Generated by helpers/gen_swizzle.py"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def xx(self):
        return vec2.Vec2(self.x, self.x)

    @property
    def xy(self):
        return vec2.Vec2(self.x, self.y)

    @xy.setter
    def xy(self, value):
        self.x = value[0]
        self.y = value[1]

    @property
    def yx(self):
        return vec2.Vec2(self.y, self.x)

    @yx.setter
    def yx(self, value):
        self.y = value[0]
        self.x = value[1]

    @property
    def yy(self):
        return vec2.Vec2(self.y, self.y)
