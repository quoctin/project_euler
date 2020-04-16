import numpy as np 
import helper

@helper.timing
def largest_prime_factor(n):
    """Compute largest prime factor of n"""
    def is_prime(x):
        """Check if x is prime"""
        for i in np.arange(2, int(np.sqrt(x))):
            if x % i == 0:
                return False
        return True

    largest_prime = -1
    sn = int(np.sqrt(n))
    mark_prime = np.ones(sn, dtype=bool)

    for p in np.arange(2, sn, dtype=int):
        if mark_prime[p]:
            mark_prime[[i for i in np.arange(p+p, sn, p, dtype=int)]] = False
            if n % p == 0:
                largest_prime = p

    if largest_prime > 0:
        # check cofactor of largest prime factor
        largest_cofactor = n / largest_prime
        if is_prime(largest_cofactor) and largest_cofactor > largest_prime:
            largest_prime = largest_cofactor
        return largest_prime

    return n


if __name__ == "__main__":
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(13) == 13
    print('Pass test')

    print(largest_prime_factor(600851475143))