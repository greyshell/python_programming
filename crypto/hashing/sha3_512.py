#!/usr/bin/env python3

import hashlib

if __name__ == '__main__':
    message = "hello world"
    # convert the message into byte format
    msg_bytes = message.encode()

    # represents -> given a string in byte format
    # msg_digest = hashlib.HASH_ALGO(b'hello world')

    msg_digest = hashlib.sha3_512(msg_bytes)
    # convert digest in hex format
    hex_digest = msg_digest.hexdigest()

    print(f"message: {message}")
    print(f"sha3_512 digest: {hex_digest}")
    print(f"digest length {msg_digest.digest_size} bytes")

    # example of sha3_256:
    # shorter hashes are not prefixes of longer hashes
    msg_digest_256 = hashlib.sha3_256(msg_bytes)
    # convert digest in hex format
    hex_digest = msg_digest_256.hexdigest()

    print(f"message: {message}")
    print(f"sha3_256 digest: {hex_digest}")
    print(f"digest length {msg_digest_256.digest_size} bytes")




