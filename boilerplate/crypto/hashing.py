#!/usr/bin/env python3

# author: greyshell

import binascii
import hashlib
import bcrypt

from colorama import Fore


def demo_hashlib():
    """
    understanding hashlib functions
    :return:
    """
    print(Fore.MAGENTA, f"[+] usage of hashlib library:")
    print(Fore.WHITE)
    print(Fore.CYAN, f"algorithms available: ")
    # hashlib.algorithms_available -> returns a set, use list() to convert it to a list

    print(hashlib.algorithms_available)
    print(Fore.MAGENTA)

    message = 'secret'

    list_of_hash = ['ripemd160', 'sha1', 'sha256', 'sha512', 'sha3_256', 'sha3_512', 'blake2b', 'blake2s']

    for h in list_of_hash:
        result = hashlib.new(h, message.encode()).hexdigest()
        print(f"{h} => {result}")

    # variable length digest
    print(Fore.WHITE)
    r = hashlib.new('shake_256', message.encode()).hexdigest(32)
    print(Fore.BLUE, f"shake_256 => {r}")

    # key derivation and stretching -> need to provide positional arguments
    print(Fore.WHITE)
    dk = hashlib.pbkdf2_hmac(hash_name='sha256', password=b'password', salt=b'salt', iterations=100000, dklen=None)
    result = binascii.hexlify(dk)
    print(Fore.LIGHTRED_EX, f"pkbf2_hmac key derivation:  {result}")

    # need to provide positional arguments
    r = hashlib.scrypt(password=b'password', salt=b'salt', n=4, r=32, p=1, maxmem=0, dklen=64)
    result = binascii.hexlify(r)
    print(Fore.GREEN, f"scrypt key derivation:  {result}")

    return


def demo_bcrypt():
    """
    understanding bcrypt functions
    :return:
    """
    print(f"\n demo bcrypt:")
    password = "abhijit"  # a string, need to convert it to byte
    salt = bcrypt.gensalt()
    # can't choose which hashing algorithm to choose
    hashed = bcrypt.hashpw(password.encode(), salt)
    print(Fore.BLUE, f"hash = {hashed.decode()}")
    print(Fore.MAGENTA, f"salt = {salt.decode()}")

    print(Fore.CYAN, f"salt is prepended with hash")

    # Check that an unencrypted password matches one that has
    # previously been hashed.
    plaintext = "abhijit"
    if bcrypt.checkpw(plaintext.encode(), hashed):
        print(Fore.GREEN, f"password matches")
    else:
        print(Fore.RED, f"password does not match")

    """
    The bcrypt algorithm only handles passwords up to 72 characters, any characters beyond that are ignored. To work 
    around this, a common approach is to hash a password with a cryptographic hash (such as sha256) and then base64 
    encode it to prevent NULL byte problems before hashing the result with bcrypt:
    """
    password = "an incredibly long password" * 10
    hash_algo = 'sha256'  # 64 characters
    # here we are using digest() instead of hexdigest() coz digest() -> return bytes
    h = hashlib.new(hash_algo, password.encode()).digest()
    hashed = bcrypt.hashpw(h, salt)  #
    print(Fore.WHITE, f"hash for long password (more than 72 chars): {hashed.decode()}")

    password = "a"
    private_key = bcrypt.kdf(password.encode(), salt, desired_key_bytes=32, rounds=100)

    print(Fore.CYAN, f"private key pbkdf2 format => {private_key}")


def main():
    """
    understanding the hashing functions
    :return:
    """
    demo_hashlib()
    # demo_bcrypt()


if __name__ == '__main__':
    main()
