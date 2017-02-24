import pytest
import copy
import math
from tri2 import Tri2
from vec2 import Vec2
from line2 import Line2
from functions import almost_equal
from geom_exceptions import TriangleException


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


def test_sides_distance():
    t = Tri2(Vec2(0.0, 0.0), Vec2(0.0, 5.0), Vec2(5.0, 0.0))
    assert t.edge(0) == Line2([0.0, 0.0], [0.0, 5.0])
    assert t.edge(1) == Line2([0.0, 5.0], [5.0, 0.0])
    assert t.edge(2) == Line2([5.0, 0.0], [0.0, 0.0])
    with pytest.raises(ValueError):
        t.edge(3)
    assert almost_equal(t.distance_squared([2.0, -2.0]), 4.0)
    assert almost_equal(t.distance_squared(Vec2(0.0, 5.0)), 0.0)
    assert almost_equal(t.distance([-3.0, 3.0]), 3.0)
    assert almost_equal(t.distance([4.0, -1.0]), 1.0)
    assert almost_equal(t.distance([2.5, 1.0]), 1.0)
    assert t.nearest_edge_index([2.0, -2.0]) == 2
    assert t.nearest_edge_index(Vec2(0.0, 5.0)) == 0
    assert t.nearest_edge_index([4.0, 4.0]) == 1


def test_square():
    t = Tri2(Vec2(0.0, 0.0), Vec2(0.0, 5.0), Vec2(5.0, 0.0))
    assert almost_equal(t.square(), 12.5)
    t2 = Tri2(Vec2(0.0, 5.0), Vec2(0.0, 5.0), Vec2(0.0, 5.0))
    assert almost_equal(t2.square(), 0.0)
    t2 = Tri2(Vec2(0.0, 0.0), Vec2(0.0, 2.0), Vec2(0.0, 5.0))
    assert almost_equal(t2.square(), 0.0)


def test_barycentric():
    t = Tri2(Vec2(0.0, 0.0), Vec2(0.0, 5.0), Vec2(5.0, 0.0))
    assert t.get_point_inside([1.0, 0.0, 0.0]) == Vec2(0.0, 0.0)
    assert t.get_point_inside([0.0, 1.0, 0.0]) == Vec2(0.0, 5.0)
    assert t.get_point_inside([0.0, 0.0, 1.0]) == Vec2(5.0, 0.0)
    with pytest.raises(ValueError):
        t.get_point_inside([1.0, 1.0, 0.0])
    assert t.get_point_inside([0.5, 0.5, 0.0]) == Vec2(0.0, 2.5)
    assert t.get_point_inside([0.0, 0.5, 0.5]) == Vec2(2.5, 2.5)
    assert t.get_point_inside([0.5, 0.0, 0.5]) == Vec2(2.5, 0.0)


def test_circles():
    t = Tri2(Vec2(0.0, 0.0), Vec2(0.0, 1.0), Vec2(1.0, 0.0))
    c = t.incenter()
    d = t.distance(c)
    r = t.incircle_radius()
    assert almost_equal(d, r)
    assert t.circumcenter() == Vec2(0.5, 0.5)
    assert almost_equal(t.circumcircle_radius(), 0.5 * math.sqrt(2.0))
    t2 = Tri2(Vec2(0.0, 1.0), Vec2(0.0, 1.0), Vec2(0.0, 1.0))
    assert t2.incenter() == Vec2(0.0, 1.0)
    assert almost_equal(t2.incircle_radius(), 0.0)
    with pytest.raises(TriangleException):
        t2.circumcenter()
    with pytest.raises(TriangleException):
        t2.circumcircle_radius()
    t3 = Tri2(Vec2(0.0, 1.0), Vec2(0.0, 3.0), Vec2(0.0, 5.0))
    assert t3.incenter() == Vec2(0.0, 3.0)
    assert almost_equal(t3.incircle_radius(), 0.0)
    with pytest.raises(TriangleException):
        t3.circumcenter()
    with pytest.raises(TriangleException):
        almost_equal(t3.circumcircle_radius(), 0.0)
    t4 = Tri2(Vec2(-0.5, -math.sqrt(3) / 6.0), Vec2(0.5, -math.sqrt(3) / 6.0), Vec2(0.0, math.sqrt(3) / 3.0))
    assert t4.incenter() == Vec2(0.0, 0.0)
    assert t4.circumcenter() == Vec2(0.0, 0.0)
    assert almost_equal(t4.incircle_radius(), math.sqrt(3) / 6.0)
    assert almost_equal(t4.circumcircle_radius(), math.sqrt(3) / 3.0)
