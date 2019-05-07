#!/usr/bin/env python3

# author: greyshell


import argparse
import sys
import base64
import re

from colorama import Fore


class UserInput:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="[+] base64 encode / decode ")
        self.group = self.parser.add_mutually_exclusive_group()

        # below two option should be mutually exclusive
        self.group.add_argument("-e", "--encode", metavar="", help="provide the message to encode")
        self.group.add_argument("-d", "--decode", metavar="", help="provide the cipher to decode")


class Base64Encoding:
    """
    implementation of base64 encoding / decoding
    """

    @staticmethod
    def encode(text):
        # convert the string to byte
        data = text.encode()
        # perform the base64 encoding
        temp = base64.b64encode(data)
        # convert the byte to string
        result = temp.decode()
        return result

    @staticmethod
    def decode(text):
        result = ""
        try:
            # convert the string to byte
            data = text.encode()
            # perform the base64 decoding
            temp = base64.b64decode(data)
            # convert the byte to string
            result = temp.decode()
        except Exception as e:
            print(Fore.RED, f"[x] {e}")
            exit(0)

        return result


def main():
    my_input = UserInput()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(1)

    b64 = Base64Encoding()

    if args.encode:
        result = b64.encode(args.encode)
        print(Fore.GREEN, f"[+] result: {result}")

    elif args.decode:
        result = b64.decode(args.decode)
        print(Fore.BLUE, f"[+] result: {result}")
    else:
        my_input.parser.print_help(sys.stderr)


if __name__ == '__main__':
    main()
