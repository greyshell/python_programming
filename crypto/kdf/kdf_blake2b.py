#!/usr/bin/env python3
import base64
import hashlib
from base64 import b64decode, b64encode

if __name__ == '__main__':
    # blake KDF functionality
    seed_key = b64decode(b'Rm5EPJai72qcK3RGBpW3vPNfZy5OZothY+kHY6h21KM=')
    print(f"seed: {b64encode(seed_key)}")
    derived_key = hashlib.blake2b(key=seed_key, person=b'kEncrypt').hexdigest()
    another_derived_key = hashlib.blake2b(key=seed_key, person=b'kMAC').hexdigest()
    print(f"key derivation through blake2b key1:  {derived_key}")
    print(f"key derivation through blake2b key2: {another_derived_key}")

    # HMAC based KDF

