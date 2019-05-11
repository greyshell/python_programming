#!/usr/bin/env python3

# author: greyshell


import argparse
import sys

import base64

from colorama import Fore


class UserInput:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="[+] base64 encode / decode ")
        self.group = self.parser.add_mutually_exclusive_group()

        # below two option should be mutually exclusive
        self.group.add_argument("-e", "--encode", metavar="", help="provide the message to encode")
        self.group.add_argument("-d", "--decode", metavar="", help="provide the cipher to decode")


def main():
    my_input = UserInput()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(1)

    if args.encode:
        data = args.encode
        result = base64.b64encode(data.encode())
        print(Fore.GREEN, f"[+] result: {result}")

    elif args.decode:
        data = args.decode
        result = base64.b64decode(data.encode())
        print(Fore.BLUE, f"[+] result: {result}")
    else:
        my_input.parser.print_help(sys.stderr)


if __name__ == '__main__':
    main()
