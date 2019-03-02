import cProfile
import pstats
import time
from functools import wraps


def do_cprofile(filename):
    """
    Decorator for function profiling.
    """

    def wrapper(func):
        def profiled_function(*args, **kwargs):
            DO_PROF = True  # os.getenv("PROFILING")
            if DO_PROF:
                profile = cProfile.Profile()
                profile.enable()
                result = func(*args, **kwargs)
                profile.disable()
                sortby = "tottime"
                ps = pstats.Stats(profile).sort_stats(sortby)
                ps.dump_stats(filename)
            else:
                result = func(*args, **kwargs)
            return result

        return profiled_function

    return wrapper


def timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (function.func_name, str(t1 - t0)))
        return result

    return function_timer


def cache(func):
    memo = {}

    @wraps(func)
    def _wrapper(*args, **kwargs):
        res = memo.get(args, None)
        if res is not None:
            return res
        else:
            res = func(*args, **kwargs)
            memo[args] = res
        return res

    return _wrapper
