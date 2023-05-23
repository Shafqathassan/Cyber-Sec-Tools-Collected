#aka scytale cipher

def encrypt(message, key):
    rows, cols = key
    grid = [[''] * cols for _ in range(rows)]
    i, j = 0, 0

    for char in message:
        grid[i][j] = char
        j += 1

        if j == cols:
            i += 1
            j = 0

    ciphertext = ''
    for j in range(cols):
        for i in range(rows):
            ciphertext += grid[i][j]

    return ciphertext

def decrypt(ciphertext, key):
    rows, cols = key
    grid = [[''] * cols for _ in range(rows)]
    char_count = 0

    for j in range(cols):
        for i in range(rows):
            grid[i][j] = ciphertext[char_count]
            char_count += 1

    plaintext = ''
    i, j = 0, 0

    for _ in range(len(ciphertext)):
        plaintext += grid[i][j]
        i += 1

        if i == rows:
            j += 1
            i = 0

    return plaintext

# Example usage:
message = "HELLO WORLD"
key = (3, 4)  # Rows, Columns

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
