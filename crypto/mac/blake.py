#!/usr/bin/env python3
import base64
import hashlib
from base64 import b64decode

if __name__ == '__main__':
    # convert the message into byte format
    message = "hellow world"
    msg_bytes = message.encode()
    key_bytes = "password".encode()
    # if person and salt lengths < 16 bytes then padding(\x00) will be added
    person_bytes = "asinha".encode()
    salt_bytes = "uid001".encode()

    # use of blake2b
    signed_digest = hashlib.blake2b(msg_bytes,
                                    digest_size=32,
                                    key=key_bytes,
                                    salt=salt_bytes,
                                    person=person_bytes)

    # convert digest in hex format
    hex_digest = signed_digest.hexdigest()

    print(f"message: {message}")
    print(f"blake2b digest obj: {signed_digest}")
    # print(f"md5 digest in base64 encoded format: {base64_digest}")
    print(f"blake2b digest in hex format: {hex_digest}")
    print(f"digest length {signed_digest.digest_size} bytes")
    print("")

