from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey
)

private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()

message = b"Hello World!"
bad_message = b"bad"
signature = private_key.sign(message)

try:
    public_key.verify(signature, message)
    # public_key.verify(signature, bad_message)
    print("valid Signature")
except Exception as e:
    print(f"invalid Signature {e}")

