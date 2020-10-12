#!/usr/bin/env python3

# author: greyshell
# description: a helper script / wrapper to perform all keyring operations


import argparse
import sys

import keyring


class UserInput:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                description="a helper script / wrapper to perform all keyring operations")
        self.subparsers = self.parser.add_subparsers(title="commands", help="See '[command] --help' for details")

        # set a keyring
        self.set_keyring_parser = self.subparsers.add_parser("set", description="set up a keyring",
                                                             help="set up a keyring")
        self.set_keyring_parser.add_argument("-n", "--name", metavar="",
                                             help="provide the keyring name", required=True)
        self.set_keyring_parser.add_argument("-u", "--username", metavar="",
                                             help="provide the username", required=True)
        self.set_keyring_parser.add_argument("-p", "--password", metavar="",
                                             help="provide the password", required=True)
        self.set_keyring_parser.set_defaults(cmd="set")

        # get a keyring
        self.get_keyring_parser = self.subparsers.add_parser("get", description="get credentials from a keyring",
                                                             help="get credentials from a keyring")
        self.get_keyring_parser.add_argument("-n", "--name", metavar="",
                                             help="provide the keyring name", required=True)
        self.get_keyring_parser.set_defaults(cmd="get")

        # delete a keyring
        self.del_keyring_parser = self.subparsers.add_parser("del", description="delete a keyring",
                                                             help="delete a keyring")
        self.del_keyring_parser.add_argument("-n", "--name", metavar="",
                                             help="provide the keyring name", required=True)
        self.del_keyring_parser.set_defaults(cmd="del")


def set_keyring(keyring_name, username, password):
    keyring.set_password(keyring_name, "username", username)
    keyring.set_password(keyring_name, username, password)


def get_keyring(keyring_name):
    username = keyring.get_password(keyring_name, "username")
    password = keyring.get_password(keyring_name, str(username))
    return username, password


def del_keyring(keyring_name):
    username, password = get_keyring(keyring_name)
    try:
        keyring.delete_password(keyring_name, "username")
        keyring.delete_password(keyring_name, username)
    except keyring.errors.PasswordDeleteError as e:
        print(e)
        exit(0)


if __name__ == "__main__":
    my_input = UserInput()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(0)

    if args.cmd == "set":
        set_keyring(args.name, args.username, args.password)
        print(f"credential is set !!")
    elif args.cmd == "get":
        usr, passwd = get_keyring(args.name)
        print(f"username: {usr}, password: {passwd}")
    elif args.cmd == "del":
        del_keyring(args.name)
        print(f"deleted keyring: {args.name}")
    else:
        my_input.parser.print_help(sys.stderr)
