#!/usr/bin/env python3

import hashlib

if __name__ == '__main__':
    message = "hello world"
    # convert the message into byte format
    msg_bytes = message.encode()

    msg_digest = hashlib.shake_256(msg_bytes)
    # represents -> given a string in byte format
    # msg_digest = hashlib.shake_256(b'hello world')
    # shake supports XOf - variable length output, min=0, max=no_limit
    xof_len = 64  # in byte format

    # convert digest in hex format
    hex_digest = msg_digest.hexdigest(xof_len)

    print(f"message: {message}")
    print(f"shake_256 digest: {hex_digest}")
    print(f"digest length {xof_len} bytes")
