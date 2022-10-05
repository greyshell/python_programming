#!/usr/bin/env python3

if __name__ == '__main__':
    a = 1000

    if a > 10:
        print(10)
    elif a > 50:  # this condition is not checked coz previous one is satisfied
        print(50)
    else:
        print(100)

    print()
    if a > 10:
        print(10)
    if a > 50:
        print(50)
