import hashlib
import binascii

if __name__ == '__main__':
    # convert the message into byte format
    password = "hellow world"
    msg_bytes = password.encode()
    salt_bytes = "greyshell".encode()

    pass_digest = hashlib.pbkdf2_hmac(hash_name='sha256',
                                      password=msg_bytes,
                                      salt=salt_bytes,
                                      iterations=100000,
                                      dklen=32)

    print(f"password: {password}")
    print(f"pbfkdf2 digest: {pass_digest}")
    print(f"proper hex format: {binascii.hexlify(pass_digest)}")
