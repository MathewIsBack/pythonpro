import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Chars: {chars}")
# print(f"Key: {key}")

# Encrypt 

plain_text = input("Enter your message: ")
ciphre_text = ""

for letter in plain_text:
    index = chars.index(letter)
    ciphre_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {ciphre_text}")


# Decrypt 

ciphre_text = input("Enter the cyphered message: ")
plain_text = ""

for letter in ciphre_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {ciphre_text}")
print(f"Original message: {plain_text}")
