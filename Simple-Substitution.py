import string
import random

def substitution_encrypt(message):
    # Create a mapping of each letter in the alphabet to a random letter
    alphabet = string.ascii_lowercase
    mapping = ''.join(random.sample(alphabet, len(alphabet)))

    # Use the mapping to encrypt the message
    encrypted_message = ''
    for letter in message.lower():
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted_message += mapping[index]
        else:
            encrypted_message += letter
    return encrypted_message
