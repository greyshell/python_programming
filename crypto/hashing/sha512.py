#!/usr/bin/env python3

import hashlib

if __name__ == '__main__':
    message = "hello world"
    # convert the message into byte format
    msg_bytes = message.encode()

    msg_digest = hashlib.sha512(msg_bytes)
    # convert digest in hex format
    hex_digest = msg_digest.hexdigest()

    print(f"message: {message}")
    print(f"sha512 digest: {hex_digest}")
    print(f"digest length {msg_digest.digest_size} bytes")

    msg_digest_256 = hashlib.sha256(msg_bytes)
    # convert digest in hex format
    hex_digest = msg_digest_256.hexdigest()

    print(f"message: {message}")
    print(f"sha256 digest: {hex_digest}")
    print(f"digest length {msg_digest_256.digest_size} bytes")




