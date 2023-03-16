#text to encrypt stored in message variable below.
message = 'This is program to explain reverse cipher.'

#ciphered text using this algorithm
translated = '' #cipher text is stored in this variable
i = len(message) - 1

while i >= 0:
   translated = translated + message[i]
   i = i - 1
print (' The cipher text is : ' ,translated)
