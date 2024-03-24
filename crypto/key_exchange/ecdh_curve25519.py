from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519

# step 1: Alice generates her private key and public key
alice_private_key = x25519.X25519PrivateKey.generate()
alice_private_key_in_bytes = alice_private_key.private_bytes(encryption_algorithm=serialization.NoEncryption(),
                                                             encoding=serialization.Encoding.Raw,
                                                             format=serialization.PrivateFormat.Raw).hex()
print(f"Alice private key(i.e x): {alice_private_key_in_bytes}")

alice_public_key = alice_private_key.public_key()
alice_pubic_key_in_bytes = alice_public_key.public_bytes(encoding=serialization.Encoding.Raw,
                                                         format=serialization.PublicFormat.Raw).hex()
print(f"Alice public key(i.e k1): {alice_pubic_key_in_bytes}")

# step 3: Bob generates his private key and public key
bob_private_key = x25519.X25519PrivateKey.generate()
bob_public_key = bob_private_key.public_key()

print("")
print(f"Bob private key(i.e y): {bob_private_key.private_bytes(encryption_algorithm=serialization.NoEncryption(), encoding=serialization.Encoding.Raw, format=serialization.PrivateFormat.Raw).hex()}")
print(f"Bob public key(i.e k2): {bob_public_key.public_bytes(encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw).hex()}")
# Alice computes the shared secret
alice_shared_secret = alice_private_key.exchange(bob_public_key)

# Bob computes the shared secret
bob_shared_secret = bob_private_key.exchange(alice_public_key)

# The shared secrets should be the same
assert alice_shared_secret == bob_shared_secret

# Convert the shared secret to bytes for further use (e.g., as an encryption key)
shared_secret_bytes = alice_shared_secret.hex()

print("")
print(f"Shared Secret: {shared_secret_bytes}")
