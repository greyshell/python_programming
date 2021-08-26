#!/usr/bin/env python3

# author: greyshell
# description: hands-on


def main():
    # tuple: a finite ordered squence of values

    # create tuple
    # tuple literals
    tup = (1, 2, "abc")  # supports heterogeneous data types
    tup0 = 1, 2, 3  # also supports without first bracket, all values are packed into a single tuple
    print(type(tup0))

    # build in tuple function
    tup2 = tuple("abc")  # it accepts single argument of type iterable, this single parameter is optional
    tup3 = tuple()  # creates an empty tuple

    # create a tuple with exactly one element
    tup4 = (1,)  # need to include a comma after first element

    # tuple and string
    # similarities: finite length, indexing and slicing
    # differences: string can only contains chars but tuple can contain any kind of value
    values = (0, 1, 2, 3, 4)
    new_values = values[0:3]  # returns a tuple
    print(new_values)

    for n in new_values:  # tuples are iterable
        print(n)

    x, y = 10, 20  # example of tuple unpacking
    # LHS and RHS should be matched else it will raise ValueError
    # utility: returning multiple values from a function

    # check the existance of a value using in operator
    if 3 in values:
        print("found")

    # tuples are immutable like string and frozenset

    t = (1, ['a', 'b'], 'word')
    t[1][0] = 'x'  # changes the list value as it does not modify the 2nd obj - list address
    print(t)


if __name__ == '__main__':
    main()
