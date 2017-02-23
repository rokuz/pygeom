import math


def almost_equal(v1, v2, eps=1e-5):
    """Checks equality of float numbers with epsilon."""
    return math.fabs(v1 - v2) < eps


def lerp(a, b, t):
    """Performs linear interpolation between a and b. t must be in range [0;1]."""
    if t < 0.0 or t > 1.0:
        raise ValueError("t must be in the range [0.0;1.0]")
    return a * (1.0 - t) + b * t


def clamp(v, lower_bound, upper_bound):
    """Clamps v in range [lower_bound;upper_bound]."""
    if v < lower_bound:
        v = lower_bound
    if v > upper_bound:
        v = upper_bound
    return v


def saturate(v):
    """Clamps v in range [0.0;1.0]."""
    return clamp(v, 0.0, 1.0)
