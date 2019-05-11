#!/usr/bin/env python3

# author: greyshell


import argparse
import base64
import os.path
import sys
from os import path

from colorama import Fore


class UserInput:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="file base64 encode / decode ")
        self.group = self.parser.add_mutually_exclusive_group()
        self.group.add_argument("-e", "--encode", metavar="", help="provide the file to base64 encode")
        self.group.add_argument("-d", "--decode", metavar="", help="provide the base64 decoded text of a file")

        self.parser.add_argument("-f", "--file", metavar="",
                                 help="while decoding provide the file name (i.e. sample.exe)")


def encode_file(file_name):
    """
    tips: this does not encode non ascii character
    :param file_name:
    :return:
    """
    result = ""
    try:
        if os.path.isfile(file_name) is False:
            print(Fore.RED, f"[x] not a file")
            exit(0)

        if path.exists(file_name) is False \
                and os.path.isfile(file_name) is False:
            print(Fore.RED, f"[x] file not found")
            exit(0)

        with open(file_name, "rb") as f:
            data = f.read()  # returns a byte object
            result = base64.b64encode(data)

    except Exception as e:
        print(Fore.RED, f"[x] {e}")
        exit(0)

    return result


def decode_file(text, file_name):
    with open(file_name, "w+") as f:
        data = text.encode()  # convert the string into bytes
        result = base64.b64decode(data)
        f.write(result.decode())  # write in byte format
    print(Fore.MAGENTA, f"[+] {file_name} has been created ")


def main():
    my_input = UserInput()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(1)

    if args.encode:
        result = encode_file(args.encode)
        print(Fore.GREEN)
        print(f"{result}")

    elif args.decode and args.file:
        decode_file(args.decode, args.file)

    else:
        my_input.parser.print_help(sys.stderr)


if __name__ == '__main__':
    main()
