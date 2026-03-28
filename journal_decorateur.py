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


@log_call
def addition(a, b):
    return a + b


if __name__ == "__main__":
    print(addition(4, 5))
