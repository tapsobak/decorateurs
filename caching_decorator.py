def log_call(func):
    def wrapper(*args, **kwargs):
        # Create a list of all arguments as strings
        args_repr = [repr(a) for a in args]  # e.g., ['3', '5']
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # e.g., ['c=10']

        # Join them together
        all_args = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        return result

    return wrapper


def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        # Create a unique key from arguments
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
@log_call
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(f"Result: {fibonacci(40)}")
