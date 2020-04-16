def gen_fibo():
    """A generator generating fibonaci series"""
    x1, x2 = 0, 1
    while True:
        current = x1 + x2
        x1, x2 = x2, current
        yield current

def sum_even_fibo_under(max_value):
    """Sum only even Fibonacci numbers"""
    fibo_generator = gen_fibo()
    ret = 0
    for fibo in fibo_generator:
        if fibo > max_value:
            break
        if fibo & 0x1 == 0:
            ret += fibo
    return ret


if __name__ == "__main__":
    assert sum_even_fibo_under(1) == 0
    assert sum_even_fibo_under(2) == 2
    assert sum_even_fibo_under(10) == 10
    assert sum_even_fibo_under(35) == 44
    print('Pass test')

    print(sum_even_fibo_under(4e6))