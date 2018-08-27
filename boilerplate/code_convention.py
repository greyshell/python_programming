#!/usr/bin/env python

# author: greyshell
# description: practice coding guideline

# avoid using import * for namespace collision
# good habit to perform explicit relative imports instead of hardcoded imports
# example of import order
# 1. standard lib imports
import optparse
import re
from math import sqrt
from os.path import abspath

# 2. core django imports - Optional
from django.db import models

# 3. 3rd party app imports
# put a line break between group
# 4. my custom app imports

# constant / global variable, defined in module level
MAX_OVERFLOW = 8

# global variable naming convention
__author__ = 'greyshell'


# separate top level method/ class definitions with two blank lines
class DemoCode:  # CapWords convention
    """[#] demo various coding conventions"""

    def __init__(self):
        # initializing the class variable with false value
        self.radius = 0
        self.area = 0
        self.flag = False
        self.first_name = ""
        self.last_name = ""
        self.full_name = ""

    def example_loop(self):
        pass
        return

    def example_operator(self, a, b, n, m):
        """[#] demo various coding conventions"""
        if a:  # equivalent to if a is not None and value could be anything (i.e False for boolean)
            print "[+] a is not None"

        # bad practice
        if n < m:
            print "[+] n is less than m"
        else:
            print "[+] m is less than n"

        # good code
        import operator
        if operator.__lt__(n, m):
            print "[+] n is less than m"
        else:
            print "[+] m is less than n"

        # easy to match operators with operands, useful crash buffer calculation in exploit dev
        self.full_name = (self.first_name
                          + self.last_name
                          + "welcome")

        return True

    def example_exception_handling(self):
        # how to raise value error
        return

    def example_string_handling(self):
        self.first_name = "foobar"
        # use string methods instead of string slicing / module
        if self.first_name[:3] == "foo":  # bad code
            print "[+] bad code"

        if self.first_name.startswith("foo"):  # good code
            print "[+] good code"

        return

    def example_branching(self):
        # don't compare boolean values to True / False using == , is
        if self.flag:  # equivalent if self.flag == True
            print self.flag
        else:
            print self.flag
        return

    def example_annotation(self):
        # variable and function annotation
        return

    def example_indentation(self):
        # used 4 spaces per indentation level in pycharm
        # limit the text per line 79 standard for open source project, use \ to break the line
        #   enable: settings -> code style -> python -> wrapping and brackets -> 'ensure right margin is not exceeded'
        #   reformat code => ctrl + alt + l
        test_str1 = "<td class=\"confluenceTdhighlight-yellow highlight-yellow confluenceTd\" colspan=\"1\" " \
                    "data-highlight-colour=\"yellow\">6.6.6 - Splunk Enterprise/Hunk</td>"
        print test_str1

        var_one = "hello"
        var_two = "world"
        var_three = 3
        var_four = 4
        # indentation aligned with opening delimiter
        foo = self.example_operator(var_one, var_two,
                                    var_three, var_four)
        print foo

        # extra indentation for long conditional continuation line
        if (var_four != var_three
                and var_one != var_two):
            print "[+] long conditional continuation line"

        return


# separate top level method/ class definitions with two blank lines
def global_demo_function():
    """
    objective: demo various coding conventions
    :return:
    """

    print "[*] inside global_demo_function"

    # to do: take user input during run time
    return


# separate top level class definitions with two blank lines
def main():
    # start sentence in small letter, [+] =>  normal, [x] => error, [*] => note / important, [-] => negative use case
    demo = DemoCode()

    # for object type comparisons use isinstance()
    if isinstance(demo, DemoCode):
        print "[+] same object"
    # for string type object it could be unicode => if isinstance(st, basestring)

    demo.example_operator('help', 'me', 7, 5)
    demo.example_string_handling()
    demo.example_branching()
    demo.example_indentation()
    # end of main()


if __name__ == '__main__':
    # what are the other things can be done here
    main()
