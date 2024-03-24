from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os

# Example usage
salt = os.urandom(16)  # Should be a random value, usually generated once and reused
input_key_material = b"Input Key Material"
info = b"Additional Info"
length = 32  # Length of the derived key in bytes

hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=length,
    salt=salt,
    info=info,
    backend=default_backend()
)

derived_key = hkdf.derive(input_key_material)

print("Derived Key:", derived_key.hex())
