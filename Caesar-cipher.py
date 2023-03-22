#Author : ShafqatHassan
#Dated : 8th; of Mar 2023
#Repo : Shafqathassan/Cyber-Sec_Tools
#The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique.
#It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet.

def encrypt(text,s):
result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
     
      # Encrypt uppercase characters in plain text
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
   
#Check the function above
text = "CEASER CIPHER DEMO"
s = 4

print "Plain Text : " + text
print "Shift pattern : " + str(s)
print "Cipher: " + encrypt(text,s)
