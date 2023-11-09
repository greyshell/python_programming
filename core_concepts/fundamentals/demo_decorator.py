# demo decorator


def printlog(func):
    def wrapper(*args, **kwargs):  # decorated function: wrapper
        print(f"CALLING: {func.__name__}")  # pre-processing
        return func(*args, **kwargs)

    return wrapper


@printlog
def f(n):
    return n + 2


# another way of doing this
def f_another(n):
    return n + 2


f_another = printlog(f_another)


@printlog
def baz(a, b):
    return a + b


# example of masking
def check_id(func):
    def wrapper(*args, **kwargs):  # decorated function: wrapper
        print(f"ID of func: {id(func)}")
        return func(*args, **kwargs)

    print(f"ID of wrapper: {id(wrapper)}")
    return wrapper


@check_id
def check(x):
    return x + 3


def history(func):
    # private variable
    return_vals = set()

    def wrapper(*args, **kwargs):
        return_val = func(*args, **kwargs)
        # remember the return
        return_vals.add(return_val)
        print(f"Return Values: {return_vals}")
        return return_val

    return wrapper


@history
def foo(x):
    return x + 2


def my_add(increment):
    def factory_decorator(func):
        def wrapper(*args, **kwargs):
            # process the results
            out = func(*args, **kwargs)
            return increment + out
        return wrapper

    return factory_decorator


@my_add(2)
def bar(x):
    return 2 * x


if __name__ == '__main__':
    # print(f(2))
    # print(f_another(3))
    # print(baz(2, 4))
    # print(check(3))
    # print(id(check))
    # print(foo(1))
    # print(foo(2))
    # print(foo(3))
    print(bar(3))


