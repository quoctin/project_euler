import time 


def memoize(f):
    """Decorator for memoized functions"""    
    memory = {}

    def f_(*args):
        if args not in memory:
            memory[args] = f(*args)
        return memory[args]

    return f_ 


def timing(f):
    """Decorator for measuring running time"""
    def f_(*args, **kwargs):
        start = time.perf_counter()
        ret = f(*args, **kwargs)
        end = time.perf_counter()
        print('Elapsed time: {} seconds'.format(end - start))
        return ret

    return f_