from tri2 import Tri2
from vec2 import Vec2


def test_construction():
    t = Tri2(Vec2(0.0, 0.0), Vec2(0.0, 2.0), Vec2(2.0, 0.0))
    assert t.points[0] == Vec2(0.0, 0.0) and t.points[1] == Vec2(0.0, 2.0) and t.points[2] == Vec2(2.0, 0.0)
