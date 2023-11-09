#!/usr/bin/env python3

# reference: https://pycryptodome.readthedocs.io/en/latest/src/hash/tuplehash256.html

from Crypto.Hash import TupleHash256

if __name__ == '__main__':
    # sender, receiver, amount, transaction fee
    tuple_hash = TupleHash256.new(digest_bytes=32)
    tuple_hash.update(b'alice')
    tuple_hash.update(b'bob')
    tuple_hash.update(b'1000')
    tuple_hash.update(b'90')

    hex_digest = tuple_hash.hexdigest()

    # print(f"message: {message}")
    print(f"tupleshash256 digest: {hex_digest}")
    print(f"digest length: {tuple_hash.digest_size}")

    # increase the amount field, target second pre-image resistance property
    tuple_hash2 = TupleHash256.new(digest_bytes=32)
    tuple_hash2.update(b'alice')
    tuple_hash2.update(b'bob')
    tuple_hash2.update(b'10009')  # shift the 9 from bottom
    tuple_hash2.update(b'0')

    hex_digest = tuple_hash2.hexdigest()

    print(f"tupleshash256 digest: {hex_digest}")
    print(f"digest length: {tuple_hash.digest_size}")
