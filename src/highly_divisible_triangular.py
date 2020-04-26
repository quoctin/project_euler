import numpy as np
import helper
from common import compute_divisors


def triangular_number_gen():
    """Generate triangular numbers"""
    n = 1
    while True:
        yield n, int(n*(n+1)/2)
        n += 1


@helper.timing
def highly_divisible_triangular(bound):
    """Compute the first triangular number whose number of divisors is greater 
    than bound"""
    gen = triangular_number_gen()

    n_divisors, n_pone_divisors = {1:1}, {1:1}
    for n, x in gen:
        n_divisors = n_pone_divisors
        n_pone_divisors = compute_divisors(n+1)
        if n_pone_divisors.get(2):
            n_pone_divisors[2] -= 1
        divisors = set(list(n_divisors.keys()) + list(n_pone_divisors.keys()))
        ret = np.prod([n_divisors.get(d,0) + n_pone_divisors.get(d,0) + 1 \
                for d in divisors])
        if ret > bound:
            return x


if __name__ == '__main__':
    assert highly_divisible_triangular(3) == 6
    assert highly_divisible_triangular(5) == 28
    print('Pass test')
    
    print(highly_divisible_triangular(500))