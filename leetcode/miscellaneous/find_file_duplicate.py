#!/usr/bin/env python

import os
import hashlib
from collections import defaultdict

BLOCKSIZE = 65536


def hash_file(filename):
    hasher = hashlib.sha1()

    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()


def main():
    """
    dropbox question:
    list out all the duplicates in group and other files inside a given directory
    the directory can contain sub directory and files
    :return:
    """
    dir_name = "/root/pentest/lab/dhaval"

    lookup = defaultdict(list)

    for root, dirs, files in os.walk(dir_name):
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
