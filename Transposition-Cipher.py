#Author : ShafqatHassan
#Dated : 17th; of Mar 2023
#Repo : Shafqathassan/Cyber-Sec_Tools
#Transposition Cipher is a cryptographic algo in which order of alphabets in plaintext is rearranged to form cipher text. In it, the actual plain text alphabets are not included.
def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
   order = {
      int(val): num for num, val in enumerate(key)
   }
ciphertext = ''

for index in sorted(order.keys()):
   for part in split_len(plaintext, len(key)):
      try:ciphertext += part[order[index]]
         #The IndexError exception means that you are trying to access an index that doesn't exist.
         except IndexError:
            continue
   return ciphertext
print(encode('17-03-2023', 'CyberSecTools'))
