import math


def gcd(a, b):
    """Return greatest common divisor of a and b"""
    if a == 0 or b == 0:
        return a + b
    # recursive will reach maximum recursion depth
    while a != b:
        a, b = (a - b, b) if a > b else (a, b - a)
    return a


def lcm(a, b):
    """Return least common multiple"""
    if not isinstance(a, int):
        a = int(a)
    if not isinstance(b, int):
        b = int(b)
    return abs(a*b) / gcd(a, b)


def lcm_series(series):
    assert len(series) > 0, "series cannot be empty"
    ret = series[0]
    for i in series[1:]:
        ret = lcm(ret, i)
    return ret


if __name__ == "__main__":
    assert int(lcm(20, 30)) == 60
    assert int(lcm(1, 1)) == 1
    assert int(lcm(3, 0)) == 0
    print('Pass test')
    print(int(lcm_series(range(1, 20))))
