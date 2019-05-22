#!/usr/bin/env python3

# author: greyshell

"""
dropbox question:
list out all the duplicates in group and other files inside a given directory
the directory can contain sub directory and files
"""

import os
import hashlib
from collections import defaultdict

BLOCKSIZE = 65536


def hash_file(filename):
    hasher = hashlib.sha1()

    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)  # instead of reading the entire file, read block by block
        while len(buf) > 0:
            hasher.update(buf)  # proper usage of update() method for hashing large file
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()


def main():
    test_dir_name = "/root/pentest/lab/dhaval"
    lookup = defaultdict(list)  # used to maintain the order

    for root, dirs, files in os.walk(test_dir_name):
        for filename in files:
            f = root + "/" + filename
            h = hash_file(f)
            lookup[h].append(f)

    non_dup = []
    print("duplicate files: ")
    print("")
    for key in lookup:
        values = lookup[key]
        if len(values) == 1:
            non_dup.append(values[0])
        else:
            for v in values:
                print(v)
        print("")

    print("non duplicate files: ")
    for i in non_dup:
        print(i)


if __name__ == "__main__":
    main()
