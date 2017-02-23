import pytest
import math
import geom_exceptions
from functions import almost_equal
from copy import copy, deepcopy
from vec2 import Vec2


def test_construction():
    v = Vec2()
    assert almost_equal(v.x, 0.0) and almost_equal(v.y, 0.0)
    v = Vec2(1.0, 2.5)
    assert almost_equal(v.x, 1.0) and almost_equal(v.y, 2.5)


def test_get_set():
    v = Vec2()
    v[0] = 1.0
    assert almost_equal(v.x, 1.0)
    v[1] = 2.0
    assert almost_equal(v.y, 2.0)
    with pytest.raises(ValueError):
        v[2] = 1.0
    with pytest.raises(ValueError):
        k = v[2]


def test_swizzle():
    v = Vec2(1.0, 2.5)
    assert almost_equal(v.xx.x, 1.0) and almost_equal(v.xx.y, 1.0)
    assert almost_equal(v.yy.x, 2.5) and almost_equal(v.yy.y, 2.5)
    v.xy = [5.0, 6.0]
    assert almost_equal(v.x, 5.0) and almost_equal(v.y, 6.0)
    assert almost_equal(v.yx.x, 6.0) and almost_equal(v.yx.y, 5.0)
    v.yx = [5.0, 6.0]
    assert almost_equal(v.x, 6.0) and almost_equal(v.y, 5.0)


def test_arithmetic():
    v = Vec2(3.0, 4.0) + Vec2(1.0, 2.0)
    assert almost_equal(v.x, 4.0) and almost_equal(v.y, 6.0)
    v += [3.0, -1.0]
    assert almost_equal(v.x, 7.0) and almost_equal(v.y, 5.0)
    v *= 2.0
    assert almost_equal(v.x, 14.0) and almost_equal(v.y, 10.0)
    v /= 4.0
    assert almost_equal(v.x, 3.5) and almost_equal(v.y, 2.5)
    with pytest.raises(ZeroDivisionError):
        v /= 0.0
    v = -v
    assert almost_equal(v.x, -3.5) and almost_equal(v.y, -2.5)


def test_copy():
    v = Vec2(2.0, 1.0)
    v2 = copy(v)
    assert almost_equal(v2.x, 2.0) and almost_equal(v2.y, 1.0)
    v3 = deepcopy(v2)
    assert almost_equal(v3.x, 2.0) and almost_equal(v3.y, 1.0)


def test_compare():
    v = Vec2(2.0, 1.0)
    assert v == [2.0, 1.0]
    assert v != [2.0, 2.0]
    assert v < Vec2(3.0, 0.0)
    assert v < Vec2(2.0, 2.0)
    assert v > Vec2(1.0, 0.0)
    assert v > Vec2(2.0, 0.0)
    assert v >= Vec2(2.0, 1.0)
    assert v <= Vec2(2.0, 1.0)


def test_length():
    v = Vec2(3.0, 4.0)
    assert almost_equal(v.length(), 5.0)
    v2 = v.get_normalized()
    assert almost_equal(v2.length_squared(), 1.0) and not almost_equal(v.length_squared(), 1.0)
    v.normalize()
    assert almost_equal(v.length(), 1.0)
    with pytest.raises(geom_exceptions.VectorException):
        Vec2().normalize()


def test_dot():
    v1 = Vec2(1.0, 0.0)
    v2 = Vec2(2.0, 2.0)
    assert almost_equal(v1.dot(v2), math.cos(math.pi / 4.0) * v1.length() * v2.length())
    v3 = Vec2(-2.0, 2.0)
    assert almost_equal(v2.dot(v3), 0.0)


def test_cross():
    v1 = Vec2(1.0, 0.0)
    v2 = Vec2(2.0, 2.0)
    assert v1.cross(v2) > 0.0
    assert v2.cross(v1) < 0.0
    assert almost_equal(Vec2(0.0).cross([0, 0]), 0.0)
    a = v1.length()
    b = v2.length()
    c = (v2 - v1).length()
    p = 0.5 * (a + b + c)
    s = 2.0 * math.sqrt(p * (p - a) * (p - b) * (p - c))
    assert almost_equal(math.fabs(v1.cross(v2)), s)


def test_normals():
    v1 = Vec2(2.0, 2.0)
    assert v1.left_normal == [-2.0, 2.0]
    assert v1.right_normal == [2.0, -2.0]
