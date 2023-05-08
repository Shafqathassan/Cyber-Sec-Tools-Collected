from cryptography.fernet import Fernet
#The cryptography.hazmat.primitives.ciphers module in Python is part of the Cryptography library and provides a low-level interface for working with symmetric encryption algorithms.
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Generate a random 128-bit key
key = Fernet.generate_key()

# Create an AES-128 cipher object
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

# Define a plaintext message
message = b"This is a secret message."

# Pad the message to a multiple of 16 bytes (the block size for AES-128)
padded_message = message + b"\0" * (16 - len(message) % 16)

# Create an encryptor object and encrypt the padded message
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_message) + encryptor.finalize()

# Print the key and ciphertext
print("Key:", key)
print("Ciphertext:", ciphertext)
