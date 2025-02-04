# Python program to demonstrate
# Substitution Cipher

import string  # Import the string module to access all letters

# A list containing all characters (both uppercase and lowercase)
all_letters = string.ascii_letters

"""
Create a dictionary to store the substitution
for each letter in the plaintext based on the key
"""

dict1 = {}  # Initialize an empty dictionary for encryption
key = 4     # Set the key for shifting letters

# Populate the dictionary with substitution rules
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]

# Define the plaintext message to be encrypted
plain_txt = "Cryptanalysis is the study of methods for obtaining the meaning of encrypted information without access to the secret information that is normally required to do so. Typically this involves knowing how the system works and finding a secret key. Cryptanalysis is also referred to as codebreaking or Password cracking the code. Ciphertext is generally the easiest part of a cryptosystem to obtain and therefore is an important part of cryptanalysis. Depending on what information is available and what type of cipher is being analyzed cryptanalysts can follow one or more attack models to crack a cipher."

cipher_txt = []  # Initialize an empty list to store the ciphertext

# Encrypt the plaintext message
for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]  # Substitute the letter using dict1
        cipher_txt.append(temp)  # Append the substituted letter
    else:
        temp = char  # Keep non-letter characters unchanged
        cipher_txt.append(temp)  # Append the non-letter character

cipher_txt = "".join(cipher_txt)  # Join the list into a single string
print("Cipher Text is: ", cipher_txt)  # Output the encrypted message

"""
Create a dictionary to store the substitution
for each letter in the ciphertext to decrypt it
"""

dict2 = {}  # Initialize an empty dictionary for decryption

# Populate the dictionary with substitution rules for decryption
for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i - key) % len(all_letters)]

decrypt_txt = []  # Initialize an empty list to store the decrypted message

# Decrypt the ciphertext message
for char in cipher_txt:
    if char in all_letters:
        temp = dict2[char]  # Substitute the letter using dict2
        decrypt_txt.append(temp)  # Append the substituted letter
    else:
        temp = char  # Keep non-letter characters unchanged
        decrypt_txt.append(temp)  # Append the non-letter character

decrypt_txt = "".join(decrypt_txt)  # Join the list into a single string
print("Recovered plain text:", decrypt_txt)  # Output the decrypted message
