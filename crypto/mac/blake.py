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

    # KDF functionality
    seed_key = b64decode(b'Rm5EPJai72qcK3RGBpW3vPNfZy5OZothY+kHY6h21KM=')
    derived_key = hashlib.blake2b(key=seed_key, person=b'kEncrypt').hexdigest()
    another_derived_key = hashlib.blake2b(key=seed_key, person=b'kMAC').hexdigest()
    print(f"key derivation through blake2b key1:  {derived_key}")
    print(f"key derivation through blake2b key2: {another_derived_key}")
