#!/usr/bin/env python3
import hashlib
import binascii

if __name__ == '__main__':
    # convert the message into byte format
    password = "hellow world"
    msg_bytes = password.encode()
    salt_bytes = "id001".encode()

    pass_digest = hashlib.scrypt(password=msg_bytes,
                                 salt=salt_bytes,
                                 n=4,  # must be power of 2
                                 r=32,
                                 p=1,
                                 dklen=32)  # Shorter hash outputs are prefixes of longer hash outputs.

    print(f"password: {password}")
    print(f"scrypt digest: {pass_digest}")
    print(f"proper hex format: {binascii.hexlify(pass_digest)}")
