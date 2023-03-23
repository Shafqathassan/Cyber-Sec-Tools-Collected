#Author : Shafqat hassan
#Dated : 27th; of feb 2023
#Repo : Shafqathassan/Cyber-Sec-Tools
#Giving input the password to this program, it would depict the strength of password based on multi-parameters!

import string


password = input("Enter the password: ")

#string ascii_uppercase will give the uppercase letters ‘ABCDEFGHIJKLMNOPQRSTUVWXYZ’.
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])

#string ascii_lowercase will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])

#String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
special = any([1 if c in string.ascii_punctuation else 0 for c in password])

#In Python3, string.digits is a pre-initialized string used as string constant. In Python, string.digits will give the lowercase letters ‘0123456789’.
digits = any([1 if c in string.ascii_digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]


length =len(password)

score = 0

#File reading.
with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("password was found in common list . score : 0 / 7")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1


print(f"Password length is {str(length)}, adding { str(score)} points!")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1
print (f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) -1)} points !")

if score < 4:
    print (f"password is quite weak! Score: {str(score)} / 7")
elif score == 4:
    print(f"Password is ok ! Score: {str(score)} / 7")
elif score > 4 and score < 6 :
    print(f"Password is pretty good!  Score: {str(score)} / 7")
elif score > 6:
    print(f"Password is stro! Score: {str(score)} / 7")




print(upper_case)
