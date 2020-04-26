import numpy as np


def like_prime(x):
    """Check if x is likely a prime"""
    if x > 5:
        if x & 0x1 and x % 10 in [1, 3, 7, 9]:
            return True
        else:
            return False
    return True


def compute_divisors(x):
    """Compute prime factorization of x"""
    if x <= 2: 
        return {x:1}
    
    maskout, divisors = dict(), dict()
    x_ = x
    sx = int(np.sqrt(x)) + 1
    for d in range(2, sx):
        if maskout.get(d) is None:
            power = 0
            while x_ % d == 0:
                power += 1
                x_ /= d
            if power > 0:
                divisors[d] = power
            if int(x_) == 1:
                break
            else:
                maskout.update([(i, True) for i in range(d*d, sx, d)])

    return divisors if divisors else {x:1}