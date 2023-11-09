#!/usr/bin/env python3

import hashlib

if __name__ == '__main__':
    file_name = "msg.txt"

    BLOCK_SIZE = 65536  # The size of each read from the file
    msg_digest = hashlib.sha3_512()  # create the hash object, algo used sha3_512

    with open(file_name, 'rb') as handle:  # open the file to read its bytes
        fb = handle.read(BLOCK_SIZE)  # read bytes from the file. take in the amount declared in BLOCK_SIZE
        while len(fb) > 0:  # while there is still data being read from the file
            msg_digest.update(fb)  # update the hash
            fb = handle.read(BLOCK_SIZE)  # read the next block from the file
    hex_digest = msg_digest.hexdigest()
    print(f"sha3_512 hash of {file_name}: {hex_digest}")
    print(f"digest length {msg_digest.digest_size}")
