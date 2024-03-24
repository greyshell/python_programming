#!/usr/bin/env python3

# author: greyshell

import random
import secrets
import string

# generate random token in hex
print(f"16 bytes of token in hex format => {secrets.token_bytes(nbytes=16).hex()}")

# generate a random URL safe string
print(f"16 bytes of URL safe token => {secrets.token_urlsafe(nbytes=16)}")

"""
secrets module is cryptographically secure. It is used for the following operations
    - generating random numbers,
    - Passwords and OTP.
        - generate an eight-character alphanumeric password using choice
    - random token (URL safe / hard to guess)
    - Password recovery safe URLs, and session keys.
The secrets module is based on os.urandom() and random.SystemRandom() which are the interface to the operating 
system’s best source of cryptographic randomness.
"""

print(f"return a CSPRNG random int in the range [0 to upper bound number] -> {secrets.randbelow(17)}")
# use bin() function to convert the integer to binary. number starting with '0b', indicating binary
print(f"return a CSPRNG random k nos of bits -> {bin(secrets.randbits(3))}, random number = {secrets.randbits(3)}")

# generate a random number: this is not cryptographically secure
print(f"return a PRNG random number between a range: 5 to 10 -> {random.randint(5, 10)}")

print(f"different use cases of secrets functions")
# Generate an eight-character alphanumeric password:
# used to get the entire alphanumeric character set
alphabet = string.ascii_letters + string.digits  # generate the set
# need to run the choice function 8 times and concatenate the output into a string
password = ''.join(secrets.choice(alphabet) for _ in range(8))
print(f"8 char password: {password}")

# Generate a ten-character alphanumeric password with at least one lowercase character, at least one uppercase
# character, and at least three digits:
while True:
    password = ''.join(secrets.choice(alphabet) for _ in range(10))
    if (any(c.islower() for c in password)  # any() -> returns True
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
print(f"10 char complex password: {password}")

with open('words.txt') as f:  # each line containing a word but followed by a blank line
    words = [line.strip() for line in f]  # need to strip the blank line through strip() and generate a list
    password = ' '.join(secrets.choice(words) for _ in range(4))  # each time (4 times) it'll choose a random word
print(f"XKCD style password generated from the usr/share/dict/words: {password}")

# need to set an expiration for the URL / token
safe_url = 'https://mydomain.com/reset=' + secrets.token_urlsafe()
print(f"hard to guess temporary URL containing security token suitable for password recovery option: {safe_url}")

