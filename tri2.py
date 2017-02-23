from vec2 import Vec2


class Tri2(object):
    def __init__(self, p1, p2, p3):
        assert isinstance(p1, Vec2) and isinstance(p2, Vec2) and isinstance(p3, Vec2)
        self.points = [p1, p2, p3]

