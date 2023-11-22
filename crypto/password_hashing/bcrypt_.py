#!/usr/bin/env python3
# filename is the changed to bcrypt_ to resolve the conflict
import bcrypt
import binascii

if __name__ == '__main__':
    # convert the message into byte format
    password = "hellow world"

    # use system generated salt
    salt = bcrypt.gensalt()
    pass_digest = bcrypt.hashpw(password.encode(), salt)
    print(f"password: {password}")

    print(f"salt: {salt}")
    print(f"bcrypt digest: {pass_digest}")
    print(f"salt is prepended with hash")
    print("")

    print(f"salt in hex format: {binascii.hexlify(salt)}")
    print(f"bcrypt digest in hex format: {binascii.hexlify(pass_digest)}")

    print("")
    # valiadte the hash
    if bcrypt.checkpw(password.encode(), pass_digest):
        print(f"password matches")
    else:
        print(f"password does not match")

    # KDF functionality generate secret key from a password
    print("")
    password = "secret"
    private_key = bcrypt.kdf(password.encode(),
                             salt,
                             desired_key_bytes=32,
                             rounds=100)

    print(f"derived key: {binascii.hexlify(private_key)}")
