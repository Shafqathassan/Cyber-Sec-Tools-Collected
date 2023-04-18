#Author : ShafqatHassan
#Dated : 11th; of Apr 2023
#Repo : Shafqathassan/Cyber-Sec_Tools

#AES 256 encryption/decryption using pycrypto library.

#The Python hashlib module is an interface for hashing messages easily.
#This contains numerous methods which will handle hashing any raw message in an encrypted format. 

#The base64 module have functions which helps to encode the text or binary data into base64 format and decode the base64 data into text or binary data.

import base64
import hashlib
#https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html
from Crypto.Cipher import AES
#The random module in Python defines a series of functions for generating or manipulating random integers.
from Crypto import Random
 
 # lambda keyword is used to define an anonymous function in Python. 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
password = input("Enter encryption password: ")
 
 
def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
 
 
def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
 
 
# First let us encrypt secret message
encrypted = encrypt("This is a secret message", password)
print(encrypted)
 
# Let us decrypt using our original password
decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))
