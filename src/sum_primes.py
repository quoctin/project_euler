import numpy as np
import helper 


@helper.timing
def sum_primes(top):
    """Compute summation of primes below top"""
    bprime = 2
    maskout = dict()

    topsq = int(np.sqrt(top)) + 1
    for x in range(bprime, topsq):
        if maskout.get(x, None) is None:
            maskout.update([(i, True) for i in range(x*x, top, x) if i < top])

    ret = sum(x for x in range(bprime, top) if maskout.get(x, None) is None)

    return ret


if __name__ == '__main__':
    assert sum_primes(11) == 17
    assert sum_primes(12) == 28
    assert sum_primes(15) == 41
    print('Pass test')
    print(sum_primes(2000000))