def like_prime(x):
    """Check if x is likely a prime"""
    if x > 5:
        if x & 0x1 and x % 10 in [1, 3, 7, 9]:
            return True
        else:
            return False
    return True