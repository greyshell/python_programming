#!/usr/bin/env python3
# author: greyshell

"""
note:

module - a file containing python code that can be reused in other python code files.

advantage of module:
1. simplicity
2. maintainability
3. reuability
4. scoping - module has its own namespace

advantage of namesapce:
- group the names into logical containers
- prevent the clashes between the duplicate namespace
- provide context to names

- during function name clash, local / current function only gets executed.

- when the module has only one class then import that directly, for example
from datetime import datetime

best practice is the import module to keep the imported
module separated from the callings modules namespace
"""

from adder import add as myadd


def add(x, y):
    return x - y


def main():
    value = add(7, 3)
    print(value)

    value = myadd(7, 3)
    print(value)


if __name__ == '__main__':
    main()
