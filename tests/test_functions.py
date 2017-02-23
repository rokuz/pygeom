import pytest
import functions


def test_lerp():
    assert functions.almost_equal(functions.lerp(0.0, 2.0, 0.5), 1.0)
    with pytest.raises(ValueError):
        v = functions.lerp(0.0, 5.0, -1.0)


def test_clamp():
    assert functions.almost_equal(functions.clamp(5.0, 4.0, 7.0), 5.0)
    assert functions.almost_equal(functions.clamp(3.0, 4.0, 7.0), 4.0)
    assert functions.almost_equal(functions.clamp(8.0, 4.0, 7.0), 7.0)


def test_saturate():
    assert functions.almost_equal(functions.saturate(-1.0), 0.0)
    assert functions.almost_equal(functions.saturate(0.5), 0.5)
    assert functions.almost_equal(functions.saturate(2.0), 1.0)
