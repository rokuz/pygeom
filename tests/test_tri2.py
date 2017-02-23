import pytest
import copy
from tri2 import Tri2
from vec2 import Vec2


def test_construction():
    t = Tri2(Vec2(0.0, 0.0), Vec2(0.0, 2.0), Vec2(2.0, 0.0))
    assert t.points[0] == Vec2(0.0, 0.0) and t.points[1] == Vec2(0.0, 2.0) and t.points[2] == Vec2(2.0, 0.0)
    with pytest.raises(ValueError):
        t2 = Tri2([0.0, 0.0], [0.0, 2.0], [2.0])
    assert len(t) == 3
    print(t)


def test_copy():
    t = Tri2(Vec2(2.0, 1.0), Vec2(3.0, 5.0), Vec2(0.0, 0.0))
    t2 = copy.copy(t)
    assert t2[0] == [2.0, 1.0] and t2[1] == [3.0, 5.0] and t2[2] == [0.0, 0.0]
    t3 = copy.deepcopy(t2)
    assert t2 == t3


def test_compare():
    t = Tri2(Vec2(2.0, 1.0), Vec2(3.0, 5.0), Vec2(0.0, 0.0))
    assert t != Tri2(Vec2(3.0, 1.0), Vec2(3.0, 5.0), Vec2(0.0, 0.0))
    assert t == Tri2(Vec2(2.0, 1.0), Vec2(3.0, 5.0), Vec2(0.0, 0.0))


def test_set_get():
    t = Tri2(Vec2(2.0, 1.0), Vec2(3.0, 5.0), Vec2(0.0, 0.0))
    assert t[0] == Vec2(2.0, 1.0)
    assert t[1] == Vec2(3.0, 5.0)
    assert t[2] == Vec2(0.0, 0.0)
    with pytest.raises(ValueError):
        t[0] = [2.0]
    with pytest.raises(ValueError):
        t[3] = Vec2(2.0, 2.0)
    with pytest.raises(ValueError):
        k = t[3]
    t[1] = [2.0, 2.0]
    assert t[1] == Vec2(2.0, 2.0)


def test_degeneration():
    t = Tri2(Vec2(2.0, 1.0), Vec2(3.0, 5.0), Vec2(0.0, 0.0))
    assert not t.is_degenerate()
    t2 = Tri2(Vec2(2.0, 1.0), Vec2(3.0, 1.0), Vec2(5.0, 1.0))
    assert t2.is_degenerate()
    t2 = Tri2(Vec2(0.0, 1.0), Vec2(0.0, 3.0), Vec2(0.0, 5.0))
    assert t2.is_degenerate()


def test_point_inside():
    t = Tri2(Vec2(0.0, 0.0), Vec2(0.0, 5.0), Vec2(5.0, 0.0))
    assert t.is_point_inside([1.0, 1.0])
    assert t.is_point_inside([0.0, 3.0])
    assert t.is_point_inside([3.0, 0.0])
    assert t.is_point_inside([2.5, 2.5])
    assert not t.is_point_inside([0.0, -1.0])
    assert not t.is_point_inside([-1.0, 1.0])
    assert not t.is_point_inside([4.0, 4.0])
    assert not t.is_point_inside([2.0, 6.0])
    assert not t.is_point_inside([-1.0, -1.0])
    assert not t.is_point_inside([6.0, 6.0])
    assert not t.is_point_inside([6.0, -1.0])
    assert not t.is_point_inside([-1.0, 7.0])
    with pytest.raises(ValueError):
        t.is_point_inside([4.0])
    assert t.is_point_strict_inside([1.0, 1.0])
    assert not t.is_point_strict_inside([0.0, 3.0])
    assert not t.is_point_strict_inside([3.0, 0.0])
    assert not t.is_point_strict_inside([2.5, 2.5])
    assert not t.is_point_strict_inside([0.0, -1.0])
    assert not t.is_point_strict_inside([-1.0, 1.0])
    assert not t.is_point_strict_inside([4.0, 4.0])
    with pytest.raises(ValueError):
        t.is_point_strict_inside([4.0])
    t2 = Tri2(Vec2(2.0, 1.0), Vec2(3.0, 1.0), Vec2(5.0, 1.0))
    assert t2.is_point_inside([4.0, 1.0])
    assert not t2.is_point_strict_inside([4.0, 1.0])

