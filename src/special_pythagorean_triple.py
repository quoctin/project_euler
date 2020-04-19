import math


def valid(a, b, c, summation):
    assert a > 0 and int(a) > a - 1e-12
    assert b > 0 and int(b) > b - 1e-12
    assert c > 0 and int(c) > c - 1e-12
    assert a + b + c == summation
    assert a**2 + b**2 == c**2


if __name__ == '__main__':
    for c in range(1,1000):
        m = c - 1000
        delta = (c - 1000)**2 - 4 * (5 * 1e5 - 1e3 * c)
        if delta > 0:
            a = (- m - math.sqrt(delta)) / 2
            b = (- m + math.sqrt(delta)) / 2
            try:
                valid(a, b, c, 1000)
                print('a = {}, b = {}, c = {}'.format(a, b, c))
                print('a*b*c = {}'.format(a*b*c))
            except Exception:
                pass
