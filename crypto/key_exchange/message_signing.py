from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

# Generate an EC private key
private_key = ec.generate_private_key(ec.SECP256R1(), backend=None)

# Convert the private key to bytes (for storage or transmission, not recommended in practice)
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Message to be signed
message = b"Hello, this is the message to be signed."

# Sign the message
# signature = sign_message(private_key, message)
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Verify the signature (just to demonstrate)
public_key = private_key.public_key()
public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))

print("Private Key")
print(f"{private_key_bytes.decode()}")
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("Public Key")
print(f"{public_key_bytes.decode()}")

print("Message:", message.decode())
print("Signature:", signature.hex())

# saving the public and private keys
# Specify file paths
private_key_path = "private_key.pem"
public_key_path = "public_key.pem"

# save_keys(private_key_bytes, public_key_bytes, private_key_path, public_key_path)
# Save private key to a file
with open(private_key_path, "wb") as private_key_file:
    private_key_file.write(private_key_bytes)

# Save public key to a file
with open(public_key_path, "wb") as public_key_file:
    public_key_file.write(public_key_bytes)

print("")
print(f"Private key saved to: {private_key_path}")
print(f"Public key saved to: {public_key_path}")
