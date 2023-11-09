#!/usr/bin/env python3
import base64
import hashlib

if __name__ == '__main__':
    message = "hello world"
    # convert the message into byte format
    msg_bytes = message.encode()

    # default usedforsecurity=True
    # set usedforsecurity = False when the algo is not used in the security context
    # It allows the use of insecure and blocked hashing algorithms in restricted environments.
    msg_digest = hashlib.md5(msg_bytes, usedforsecurity=True)

    # convert digest into byte format
    byte_digest = msg_digest.digest()
    # convert digest in base64
    base64_digest = base64.b64encode(byte_digest).decode()
    # convert digest in hex format
    hex_digest = msg_digest.hexdigest()

    print(f"message: {message}")
    print(f"md5 digest in byte format: {byte_digest}")
    print(f"md5 digest in base64 encoded format: {base64_digest}")
    print(f"md5 digest in hex format: {hex_digest}")
    print(f"digest length {msg_digest.digest_size} bytes")
    print("")

    # Alternate: using update() method, useful in loop and taking data chunk by chunk
    msg_digest_alt = hashlib.md5()
    for ch in message:
        ch_bytes = ch.encode()
        msg_digest_alt.update(ch_bytes)

    # convert digest into byte format
    byte_digest = msg_digest_alt.digest()
    # convert digest in base64
    base64_digest = base64.b64encode(byte_digest).decode()
    # convert digest in hex format
    hex_digest = msg_digest_alt.hexdigest()

    print(f"message: {message}")
    print(f"md5 digest in byte format: {byte_digest}")
    print(f"md5 digest in base64 encoded format: {base64_digest}")
    print(f"md5 digest in hex format: {hex_digest}")
    print(f"digest length {msg_digest_alt.digest_size} bytes")
    print("")
