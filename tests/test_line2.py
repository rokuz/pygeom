import pytest
import copy
from line2 import Line2
from vec2 import Vec2
from functions import almost_equal


def test_projections():
    line = Line2(Vec2(0.0, 0.0), Vec2(5.0, 0.0))
    assert almost_equal(line.projection_coef(Vec2(5.0, -1.0)), 1.0)
    assert almost_equal(line.projection_coef(Vec2(2.0, 1.0)), 0.4)
    assert almost_equal(line.projection_coef(Vec2(0.0, 1.0)), 0.0)
    assert line.projection_coef(Vec2(-1.0, 1.0)) < 0.0
    assert line.projection_coef(Vec2(7.0, 1.0)) > 1.0
    line2 = Line2(Vec2(5.0, 0.0), Vec2(5.0, 0.0))
    assert almost_equal(line2.projection_coef(Vec2(5.0, 0.0)), 0.0)
    assert line2.projection_coef(Vec2(4.0, 0.0)) < 0.0

    line = Line2(Vec2(0.0, 0.0), Vec2(5.0, 0.0))
    assert line.project(line.projection_coef(Vec2(2.0, 1.0))) == Vec2(2.0, 0.0)
    assert line.project(line.projection_coef(Vec2(0.0, 1.0))) == Vec2(0.0, 0.0)
    assert line.project(line.projection_coef(Vec2(5.0, 1.0))) == Vec2(5.0, 0.0)
    with pytest.raises(ValueError):
        line.project(-1.0)
    with pytest.raises(ValueError):
        line.project(2.0)

    assert line.project_point(Vec2(2.0, 1.0)) == Vec2(2.0, 0.0)
    assert line.project_point(Vec2(0.0, 1.0)) == Vec2(0.0, 0.0)
    assert line.project_point(Vec2(5.0, 1.0)) == Vec2(5.0, 0.0)
    assert line.project_point(Vec2(7.0, 1.0)) is None


def test_copy():
    l = Line2(Vec2(2.0, 1.0), Vec2(3.0, 5.0))
    l2 = copy.copy(l)
    assert l2[0] == [2.0, 1.0] and l2[1] == [3.0, 5.0]
    l3 = copy.deepcopy(l2)
    assert l2 == l3


def test_compare_negation():
    l = Line2(Vec2(2.0, 1.0), Vec2(3.0, 5.0))
    assert l != Line2(Vec2(3.0, 1.0), Vec2(3.0, 5.0))
    assert l == Line2(Vec2(2.0, 1.0), Vec2(3.0, 5.0))
    assert -l == Line2(Vec2(3.0, 5.0), Vec2(2.0, 1.0))
