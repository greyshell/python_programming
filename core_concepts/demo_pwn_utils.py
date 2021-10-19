#!/usr/bin/env python3

# author: greyshell
# how to use: python demo_pwn_utils.py -m true local -b vuln -g true

from pwn import *
from pwn_utils import PwnUtils


def exploit(conn):
    """
    interact with the binary with some valid input
    """
    print("success")


def main():
    inp = PwnUtils()
    arguments = inp.parser.parse_args()
    connection = ""

    # run the script without any argument
    if len(sys.argv) == 1:
        inp.parser.print_help(sys.stderr)
        sys.exit(1)

    # exploiting local binary
    if arguments.command == 'local':
        binary_name = "./"
        binary_name += arguments.binary
        connection = process([binary_name])
        # attach the binary with gdb in tmux session
        if arguments.gdb == 'true':
            gdb.attach(connection)

    elif arguments.command == 'network':
        connection = remote(arguments.ip_address, arguments.port)

    if arguments.debug_mode == 'true':
        context.log_level = 'debug'

    # invoke the exploit function
    exploit(connection)


if __name__ == '__main__':
    main()
