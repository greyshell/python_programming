def myfunc(a=200):
    if a is None:
        a = 100
    print(a)


def demo_adder(a, b, c, d=4, e=5):
    """argument unpacking demo"""
    return a + b + c + d + e

# argument unpacking

# variable argument


if __name__ == '__main__':
    # argument unpacking: mixed with tuple and dict
    args = (1, 2, 3)
    kwargs = {"d": 40, "e": 50}
    print(demo_adder(*args, **kwargs))  # pattern to use * and **
