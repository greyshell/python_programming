#!/usr/bin/env python3

def fetch_squares(num):
    squares = list()
    for x in range(num):
        squares.append(x ** 2)
    return squares


# implement class that complies with the iterator protocol
class SequaresIterator:
    def __init__(self, max_root_value):
        self.max_root_value = max_root_value
        self.current_root_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_root_value == self.max_root_value:
            raise StopIteration
        square_value = self.current_root_value ** 2
        self.current_root_value += 1
        return square_value


if __name__ == '__main__':
    MAX = 5

    for num in fetch_squares(MAX):  # bug: what if fetch_squares() returns a list that does not fit into the memory
        print(num)

    square_obj = SequaresIterator(5)  # this object is iterable
    for num in square_obj:
        # under the hood the for loop calls iter(SequaresIterator)
        # then for each iteration num = next(iterable_object)
        # this is NOT next(iter(SequaresIterator(5))
        print(num)

    names = ["ravi", "dhaval", "soham"]  # iterable object
    name_iterator_obj = iter(names)  # names has __iter__()
    name_iterator_obj2 = iter(names)

    for name in name_iterator_obj:
        print(name)

    for name in iter(names):
        print(name)

    print("")
    for char in next(name_iterator_obj2):
        print(char, end=" ")  # r a v i
