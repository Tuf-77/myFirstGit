import random
import string

chars = string.ascii_letters + string.punctuation + " " + string.digits

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f" chars: {chars}")
# print(f" keys : {key}")

#encrypt

text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f" original text: {text}")

print(f" cipher text  : {cipher_text}")