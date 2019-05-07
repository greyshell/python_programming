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

        self.parser.add_argument("-e", "--encode", metavar="", help="provide the file to encode")
        self.parser.add_argument("-d", "--decode", metavar="", help="provide the base64 decoded text")
        self.parser.add_argument("-f", "--file", metavar="",
                                 help="provide the file name (i.e. sample.exe)")


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

    @staticmethod
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
                data = f.read()
                result = Base64Encoding.encode(data.decode())

        except Exception as e:
            print(Fore.RED, f"[x] {e}")
            exit(0)

        return result

    @staticmethod
    def decode_file(text, file_name):
        with open(file_name, "w+") as f:
            result = Base64Encoding.decode(text)
            f.write(result)
        print(Fore.MAGENTA, f"[+] {file_name} has been created ")


def main():
    my_input = UserInput()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(1)

    b64 = Base64Encoding()

    if args.encode:
        result = b64.encode_file(args.encode)
        print(Fore.GREEN)
        print(f"{result}")

    elif args.decode and args.file:
        b64.decode_file(args.decode, args.file)

    else:
        my_input.parser.print_help(sys.stderr)


if __name__ == '__main__':
    main()
