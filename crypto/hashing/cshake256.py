#!/usr/bin/env python3

# reference: https://pycryptodome.readthedocs.io/en/v3.11.0/src/hash/cshake128.html

from Crypto.Hash import cSHAKE256

if __name__ == '__main__':
    msg_bytes = b"hello world"
    personalization_bytes = b"greyshell"

    cshake = cSHAKE256.new(custom=personalization_bytes)
    cshake.update(msg_bytes)

    msg_digest_len = 32  # length in bytes
    # convert digest in hex format
    hex_digest = cshake.read(msg_digest_len).hex()

    print(f"message: {msg_bytes.decode()}")  # byte to string conversion
    print(f"cshake256 digest: {hex_digest}")
    print(f"digest length {msg_digest_len} bytes")
