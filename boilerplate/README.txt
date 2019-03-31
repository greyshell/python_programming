#!/usr/bin/python
# author: greyshell

import sys

# importing my custom libs
from ds.sort import *
from ds.search import *


def code_convension():
    """
    - always use doc string
        - provide description
        - specify the argument and return data type
    :return:
    """
    """
    - used 4 spaces per indentation level in pycharm
    - limit the text per line 79 standard for open source project, use \ to break the line
        enable: settings -> code style -> python -> wrapping and brackets -> 'ensure right margin is not exceeded'
    - reformat code => ctrl + alt + l

    - avoid using import * for namespace collision
    - good habit to perform explicit relative imports instead of hardcoded imports
    - import order
        1. standard lib
        2. framework lib - Optional
        3. 3rd party app
        4. custom app imports

    - constant name should be capital and defined in module level
    - class name CapSmall, try avoid underscore
    - method name small, can use underscore
    - global variable naming convension
    - separate top level method/ class definitions with two blank lines


    - magic method starts and ends with double underscore
        __init__() => initializing the class variable with false value

        __repl__() => formal string representation of that resulting object, used during print
        __str__() => informal sting representation


    - careful check with if
        if variable:  => it just check for None, so miss the False bool return type
    - bad practice => if n < m
        good code =>  import operator
                      if operator.__lt__(n, m):
    - for object type comparisons use isinstance()

    """

    return


def dictionary_playground():
    pass
    return


def list_playground():
    pass


def string_playground():
    pass


def tuple_playground():
    pass


def test_custom_sorting():
    print CustomSort.selection_sort([5, 40, 3, 260, 1])
    # print help(CustomSort.counting_sort)
    print CustomSort.counting_sort([-5, 40, -3, -260, 1], -260, 40)
    print CustomSort.bubble_sort([5, 40, 3, 260, 1])


def main():
    # demo user input
    # code_convension()
    # dictionary_playground()
    test_custom_sorting()
    # print sys.path_hooks


if __name__ == '__main__':
    main()
