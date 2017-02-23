import pytest
import math
import geom_exceptions
from functions import almost_equal
from copy import copy, deepcopy
from vec2 import Vec2
from vec3 import Vec3


def test_construction():
    v = Vec3()
    assert almost_equal(v.x, 0.0) and almost_equal(v.y, 0.0) and almost_equal(v.z, 0.0)
    v = Vec3(1.0, 2.5, 3.0)
    assert almost_equal(v.x, 1.0) and almost_equal(v.y, 2.5) and almost_equal(v.z, 3.0)
    assert Vec3.from_vec2(Vec2(3.0, 4.0)) == [3.0, 4.0, 0.0]
    assert len(v) == 3
    print(v)


def test_swizzle():
    v = Vec3(1.0, 2.5, 3.0)
    assert almost_equal(v.xxx.x, 1.0) and almost_equal(v.xxx.y, 1.0) and almost_equal(v.xxx.z, 1.0)
    assert almost_equal(v.yyy.x, 2.5) and almost_equal(v.yyy.y, 2.5) and almost_equal(v.yyy.z, 2.5)
    v.xy = [5.0, 6.0]
    assert v == [5.0, 6.0, 3.0]
    v.yx = [6.0, 5.0]
    assert v == [5.0, 6.0, 3.0]
    assert v.xy == Vec3(5.0, 6.0)
    assert v.zx == Vec2(3.0, 5.0)
    assert v.xz == Vec2(5.0, 3.0)
    assert v.zyx == Vec3(3.0, 6.0, 5.0)
    assert v.yxx == Vec3(6.0, 5.0, 5.0)
    assert v.yxy == Vec3(6.0, 5.0, 6.0)
    assert v.yyx == Vec3(6.0, 6.0, 5.0)
    assert v.xzz == Vec3(5.0, 3.0, 3.0)
    assert v.xxz == Vec3(5.0, 5.0, 3.0)
    assert v.xyz == Vec3(5.0, 6.0, 3.0)
    assert v.xyx == Vec3(5.0, 6.0, 5.0)
    assert v.xzx == Vec3(5.0, 3.0, 5.0)
    assert v.xzy == Vec3(5.0, 3.0, 6.0)
    assert v.xyy == Vec3(5.0, 6.0, 6.0)
    assert v.yyy == Vec3(6.0, 6.0, 6.0)
    assert v.xxy == Vec3(5.0, 5.0, 6.0)
    assert v.xxx == Vec3(5.0, 5.0, 5.0)
    assert v.zzy == Vec3(3.0, 3.0, 6.0)
    assert v.zxy == Vec3(3.0, 5.0, 6.0)
    assert v.zzx == Vec3(3.0, 3.0, 5.0)
    assert v.zzz == Vec3(3.0, 3.0, 3.0)
    assert v.yxz == Vec3(6.0, 5.0, 3.0)
    assert v.yzx == Vec3(6.0, 3.0, 5.0)
    assert v.yyz == Vec3(6.0, 6.0, 3.0)
    assert v.yzy == Vec3(6.0, 3.0, 6.0)
    assert v.yzz == Vec3(6.0, 3.0, 3.0)
    assert v.zxx == Vec3(3.0, 5.0, 5.0)
    assert v.zxz == Vec3(3.0, 5.0, 3.0)
    assert v.zyy == Vec3(3.0, 6.0, 6.0)
    assert v.zyz == Vec3(3.0, 6.0, 3.0)
    assert almost_equal(v.xx.x, 5.0) and almost_equal(v.xx.y, 5.0)
    assert almost_equal(v.yy.x, 6.0) and almost_equal(v.yy.y, 6.0)
    assert almost_equal(v.yx.x, 6.0) and almost_equal(v.yx.y, 5.0)
    v.xz = [3.0, 6.0]
    assert v == [3.0, 6.0, 6.0]
    assert v.zy == Vec2(6.0, 6.0)
    v.zx = [4.0, 5.0]
    assert v == [5.0, 6.0, 4.0]
    assert v.xx == Vec2(5.0, 5.0)
    assert v.zz == Vec2(4.0, 4.0)
    v.zy = [2.0, 3.0]
    assert v == [5.0, 3.0, 2.0]
    v.zxy = [1.0, 2.0, 3.0]
    assert v == [2.0, 3.0, 1.0]
    v.yxz = [1.0, 2.0, 3.0]
    assert v == [2.0, 1.0, 3.0]
    v.yzx = [1.0, 2.0, 3.0]
    assert v == [3.0, 1.0, 2.0]
    v.zyx = [1.0, 2.0, 3.0]
    assert v == [3.0, 2.0, 1.0]
    v.xyz = [1.0, 2.0, 3.0]
    assert v == [1.0, 2.0, 3.0]
    v.xzy = [1.0, 2.0, 3.0]
    assert v == [1.0, 3.0, 2.0]


def test_get_set():
    v = Vec3()
    v[0] = 1.0
    assert almost_equal(v.x, 1.0)
    v[1] = 2.0
    assert almost_equal(v.y, 2.0)
    v[2] = 3.0
    assert almost_equal(v.z, 3.0)
    with pytest.raises(ValueError):
        v[3] = 1.0
    with pytest.raises(ValueError):
        k = v[3]


def test_arithmetic():
    v = Vec3(3.0, 4.0, 1.0) + Vec3(1.0, 2.0, 1.0)
    assert almost_equal(v.x, 4.0) and almost_equal(v.y, 6.0) and almost_equal(v.z, 2.0)
    v += [3.0, -1.0, -2.0]
    assert almost_equal(v.x, 7.0) and almost_equal(v.y, 5.0) and almost_equal(v.z, 0.0)
    v *= 2.0
    assert almost_equal(v.x, 14.0) and almost_equal(v.y, 10.0) and almost_equal(v.z, 0.0)
    v.yz += Vec2(0.0, 4.0)
    assert almost_equal(v.x, 14.0) and almost_equal(v.y, 10.0) and almost_equal(v.z, 4.0)
    v /= 4.0
    assert almost_equal(v.x, 3.5) and almost_equal(v.y, 2.5) and almost_equal(v.z, 1.0)
    with pytest.raises(ZeroDivisionError):
        v /= 0.0
    v = -v
    assert almost_equal(v.x, -3.5) and almost_equal(v.y, -2.5) and almost_equal(v.z, -1.0)
    v2 = v - [-0.5, -0.5, 0.0]
    assert almost_equal(v2.x, -3.0) and almost_equal(v2.y, -2.0) and almost_equal(v2.z, -1.0)
    v3 = v2 / 2.0
    assert almost_equal(v3.x, -1.5) and almost_equal(v3.y, -1.0) and almost_equal(v3.z, -0.5)
    v4 = v3 * 3.0
    assert almost_equal(v4.x, -4.5) and almost_equal(v4.y, -3.0) and almost_equal(v4.z, -1.5)
    v4 -= Vec3(1.5, 0.0, 1.5)
    assert almost_equal(v4.x, -6.0) and almost_equal(v4.y, -3.0) and almost_equal(v4.z, -3.0)


def test_copy():
    v = Vec3(2.0, 1.0, 3.0)
    v2 = copy(v)
    assert almost_equal(v2.x, 2.0) and almost_equal(v2.y, 1.0) and almost_equal(v2.z, 3.0)
    v3 = deepcopy(v2)
    assert almost_equal(v3.x, 2.0) and almost_equal(v3.y, 1.0) and almost_equal(v3.z, 3.0)


def test_compare():
    v = Vec3(2.0, 1.0, 3.0)
    assert v == [2.0, 1.0, 3.0]
    assert v != [2.0, 2.0, 3.0]
    assert v < Vec3(3.0, 0.0, 0.0)
    assert v < Vec3(2.0, 2.0, 0.0)
    assert v < Vec3(2.0, 2.0, 4.0)
    assert v < Vec3(2.0, 1.0, 4.0)
    assert v > Vec3(1.0, 0.0, 0.0)
    assert v > Vec3(2.0, 0.0, 0.0)
    assert v > Vec3(2.0, 1.0, 0.0)
    assert v >= Vec3(2.0, 1.0, 3.0)
    assert v <= Vec3(2.0, 1.0, 3.0)


def test_length():
    v = Vec3(3.0, 4.0, 5.0)
    assert almost_equal(v.length(), math.sqrt(50.0))
    v2 = v.get_normalized()
    assert almost_equal(v2.length_squared(), 1.0) and not almost_equal(v.length_squared(), 1.0)
    v.normalize()
    assert almost_equal(v.length(), 1.0)
    with pytest.raises(geom_exceptions.VectorException):
        Vec3().normalize()


def test_dot():
    v1 = Vec3(0.0, 1.0, 0.0)
    v2 = Vec3(2.0, 2.0, 2.0)
    assert almost_equal(v1.dot(v2) / v1.length() / v2.length(), math.cos(math.atan(math.sqrt(2))))
    v3 = Vec3(2.0, -1.0, -1.0)
    assert almost_equal(v2.dot(v3), 0.0)


def test_cross():
    v1 = Vec3(0.0, 1.0, 0.0)
    v2 = Vec3(2.0, 2.0, 2.0)
    v3 = v1.cross(v2)
    assert almost_equal(v1.dot(v3), 0.0) and almost_equal(v2.dot(v3), 0.0)
    v4 = v2.cross(v1)
    assert almost_equal(v3.dot(v4), -v3.dot(v3)) and almost_equal(v3.dot(v4), -v4.dot(v4))
    assert almost_equal(v3.length(), v1.length() * v2.length() * math.sin(math.atan(math.sqrt(2))))
