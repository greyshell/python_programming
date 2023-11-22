#!/usr/bin/env python3
# To avoid the conflict change the file name to hmac_
import binascii
import hmac
import hashlib

if __name__ == '__main__':
    # convert the message into byte format
    message = "hellow world"

    # use of blake2b
    signed_digest = hmac.new(b'secret key',
                             digestmod=hashlib.sha3_256)

    signed_digest.update(message.encode())

    print(f"message: {message}")
    print(f"hmac digest obj: {signed_digest}")
    print(f"hmac digest in hex format: {signed_digest.hexdigest()}")
    print(f"digest length {signed_digest.digest_size} bytes")
    print("")

    # instead of == to prevent timing attack
    h = b"287bfd89577ed08f59e6fcbaf59a9e96a64c6d0d3d61f53a65a8d5ed50623472"

    # converting the hex digest to string then compare
    compare_result = hmac.compare_digest(str(signed_digest.hexdigest()), h)
    print(f"digest compare result: {compare_result}")
