#!/usr/bin/env python3

# author: greyshell
# how to use: python demo_pwn_utils.py -m true local -b vuln -g true

from pwn import *
import pwn_utils


def exploit(conn):
    """
    interact with the binary with some valid input
    """
    print("success")


def main():
    args = get_args()
    connection = ""

    # run the script without any argument
    if len(sys.argv) == 1:
        args.print_help(sys.stderr)
        sys.exit(1)

    # exploiting local binary
    if args.command == 'local':
        binary_name = "./"
        binary_name += args.binary
        connection = process([binary_name])
        # attach the binary with gdb in tmux session
        if args.gdb == 'true':
            gdb.attach(connection)

    elif args.command == 'network':
        connection = remote(args.ip_address, args.port)
        
    else:
        args.print_help(sys.stderr)
        sys.exit(1)

    if args.debug_mode == 'true':
        context.log_level = 'debug'

    # invoke the exploit function
    exploit(connection)


if __name__ == '__main__':
    main()
