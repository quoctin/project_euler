import math 
import helper


def like_prime(x):
    """Check if x is likely a prime"""
    if x > 5:
        if x & 0x1 and x % 10 in [1, 3, 7, 9]:
            return True
        else:
            return False
    return True


@helper.timing
def nth_prime(n):
    """Compute n-th prime number"""
    def gen(lst, top):
        for item in lst:
            if item <= top+1:
                yield item
            else:
                break

    primes = [2, 3, 5, 7, 11]
    x = max(primes)
    while len(primes) < n:
        x += 2
        xsq = int(math.sqrt(x))
        # eliminate expensive loop if possible
        if like_prime(x):
            for p in gen(primes, xsq):
                if x % p == 0:
                    break
            else:
                primes.append(x)
                
    return primes[n-1]


if __name__ == "__main__":
    assert nth_prime(2) == 3
    assert nth_prime(3) == 5
    assert nth_prime(6) == 13
    print('Pass test')
    
    print('10001st prime: ', nth_prime(10001))