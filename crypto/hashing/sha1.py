#!/usr/bin/env python3

import hashlib

if __name__ == '__main__':
    message = "hello world"
    # convert the message into byte format
    msg_bytes = message.encode()

    msg_digest = hashlib.sha1(msg_bytes)
    # convert digest in hex format
    hex_digest = msg_digest.hexdigest()

    print(f"message: {message}")
    print(f"sha1 digest: {hex_digest}")
    print(f"digest length {msg_digest.digest_size} bytes")
