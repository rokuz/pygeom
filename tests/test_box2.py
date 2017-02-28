import sys
import copy
import pytest
from box2 import Box2
from vec2 import Vec2
from functions import almost_equal


def test_construction():
    b1 = Box2()
    assert almost_equal(b1.min.x, sys.float_info.max) and \
           almost_equal(b1.min.y, sys.float_info.max) and \
           almost_equal(b1.max.x, sys.float_info.min) and \
           almost_equal(b1.max.y, sys.float_info.min)
    assert b1.is_empty()
    b2 = Box2([-10, -10], [10, 10])
    assert b2.min == Vec2(-10.0, -10.0) and b2.max == Vec2(10.0, 10.0)
    b3 = Box2([10, 10], [-10, -10])
    assert b3.min == Vec2(-10.0, -10.0) and b3.max == Vec2(10.0, 10.0)
    assert len(b3) == 2
    print(b3)


def test_copy():
    b = Box2(Vec2(2.0, 1.0), Vec2(3.0, 5.0))
    b2 = copy.copy(b)
    assert b2[0] == [2.0, 1.0] and b2[1] == [3.0, 5.0]
    b3 = copy.deepcopy(b2)
    assert b2 == b3


def test_compare():
    b = Box2(Vec2(2.0, 1.0), Vec2(3.0, 5.0))
    assert b != Box2(Vec2(3.0, 1.0), Vec2(4.0, 5.0))
    assert b == Box2(Vec2(3.0, 5.0), Vec2(2.0, 1.0))


def test_set_get():
    b = Box2(Vec2(2.0, 5.0), [3.0, 1.0])
    assert b[0] == Vec2(2.0, 1.0)
    assert b[1] == Vec2(3.0, 5.0)
    with pytest.raises(ValueError):
        b[0] = [2.0]
    with pytest.raises(ValueError):
        b[3] = Vec2(2.0, 2.0)
    with pytest.raises(ValueError):
        k = b[3]
    b[1] = [2.0, 2.0]
    assert b.min == [2.0, 1.0] and b.max == [2.0, 2.0]
    b[0] = [1, 5]
    assert b.min == [1.0, 2.0] and b.max == [2.0, 5.0]


def test_intersection():
    b = Box2(Vec2(1.0, 1.0), [5.0, 5.0])
    b2 = Box2([3.0, 3.0], [6.0, 6.0])
    assert b.is_intersect(b2)
    assert b.is_intersect(Box2([5.0, 5.0], [6.0, 6.0]))
    assert not b.is_intersect(Box2([6.0, 6.0], [7.0, 7.0]))
    assert b.is_box_inside(Box2([2.0, 2.0], [3.0, 3.0]))
    assert not b.is_box_inside(Box2([2.0, 2.0], [7.0, 7.0]))
    assert b.is_point_inside([3.0, 3.0])
    assert not b.is_point_inside([7.0, 7.0])
    assert not b.is_point_strict_inside([5.0, 5.0])
    assert b.is_point_strict_inside(Vec2(4.0, 4.0))


def test_sizes():
    b = Box2(Vec2(1.0, 1.0), [5.0, 5.0])
    assert b.size == [4.0, 4.0]
    assert b.center == Vec2(3.0, 3.0)
    assert b.left_bottom == [1.0, 1.0]
    assert b.right_top == [5.0, 5.0]
    assert b.left_top == [1.0, 5.0]
    assert b.right_bottom == [5.0, 1.0]
