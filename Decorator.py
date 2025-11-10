import time
from functools import wraps

def timer(log_time=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            if log_time:
                print(f"{func.__name__} executed in {end - start:.4f}s")
            return result
        return wrapper
    return decorator

@timer(log_time=True)
def slow_function():
    time.sleep(1)
    return "Done"

print(slow_function())
