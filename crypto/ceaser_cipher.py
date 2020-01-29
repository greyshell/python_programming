#!/usr/bin/env python3

# author: greyshell


import argparse
import sys

from colorama import Fore


class UserInput:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="[+] caesar cipher")
        self.group = self.parser.add_mutually_exclusive_group()

        # below two option should be mutually exclusive
        self.group.add_argument("-e", "--encode", metavar="", help="provide the message to encode")
        self.group.add_argument("-d", "--decode", metavar="", help="provide the cipher to decode")

        self.parser.add_argument("-s", "--shift_key", metavar="", required=True, help="provide the shift key (0-25) ")


class Caesar:
    """
    implementation of caesar cipher
    """

    @staticmethod
    def encrypt(text, shift_key):
        result = ""

        # traverse text
        for i in range(len(text)):
            char = text[i]

            # encode uppercase characters
            if char.isupper():
                # return an integer representing the Unicode code point of that character.
                result += chr((ord(char) + shift_key - 65) % 26 + 65)

                # encode lowercase characters
            else:
                result += chr((ord(char) + shift_key - 97) % 26 + 97)

        return result

    @staticmethod
    def decrypt(text, shift_key):
        result = ""

        # traverse text
        for i in range(len(text)):
            char = text[i]

            # decode uppercase characters
            if char.isupper():
                # return an integer representing the Unicode code point of that character.
                result += chr((ord(char) - shift_key - 65) % 26 + 65)

                # decode lowercase characters
            else:
                result += chr((ord(char) - shift_key - 97) % 26 + 97)

        return result


def main():
    my_input = UserInput()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(1)

    caesar = Caesar()

    if args.encrypt and args.shift_key:
        result = caesar.encrypt(args.encrypt, int(args.shift_key))
        print(Fore.GREEN, f"[+] result: {result}")

    elif args.decrypt and args.shift_key:
        result = caesar.decrypt(args.decrypt, int(args.shift_key))
        print(Fore.BLUE, f"[+] result: {result}")
    else:
        my_input.parser.print_help(sys.stderr)


if __name__ == '__main__':
    main()
