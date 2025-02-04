# Define substitution cipher mappings
plain_to_encoded = {"00": "10", "01": "11", "10": "00", "11": "01"}
encoded_to_plain = {v: k for k, v in plain_to_encoded.items()}

# Encryption function using the substitution cipher
def substitution_cipher(block, cipher_map):
    return cipher_map[block]

# XOR function for two 2-bit blocks
def xor(block1, block2):
    return format(int(block1, 2) ^ int(block2, 2), '02b')

# ECB Mode encryption
def ecb_encrypt(message, cipher_map):
    return [substitution_cipher(block, cipher_map) for block in message]

# CBC Mode encryption
def cbc_encrypt(message, cipher_map, iv):
    encrypted_message = []
    previous_block = iv
    for block in message:
        # XOR with the previous block (or IV for the first block)
        xored_block = xor(block, previous_block)
        # Encrypt using the substitution cipher
        encrypted_block = substitution_cipher(xored_block, cipher_map)
        encrypted_message.append(encrypted_block)
        # Set previous block to the current encrypted block
        previous_block = encrypted_block
    return encrypted_message

# CTR Mode encryption
def ctr_encrypt(message, cipher_map, iv):
    encrypted_message = []
    counter = int(iv, 2)
    for block in message:
        # Generate keystream block using substitution cipher
        keystream_block = substitution_cipher(format(counter, '02b'), cipher_map)
        # XOR message block with keystream block
        encrypted_block = xor(block, keystream_block)
        encrypted_message.append(encrypted_block)
        # Increment counter for next block
        counter += 1
    return encrypted_message

# Define initial values
block_size = 2  # 2-bit blocks
iv = "00"  # Initialization Vector
message = ["01", "00", "11"]  # Message to be encrypted

# Encrypt message using each mode
ecb_encrypted = ecb_encrypt(message, plain_to_encoded)
cbc_encrypted = cbc_encrypt(message, plain_to_encoded, iv)
ctr_encrypted = ctr_encrypt(message, plain_to_encoded, iv)

# Output the results
print("Message:", message)
print("ECB Encrypted:", ecb_encrypted)
print("CBC Encrypted:", cbc_encrypted)
print("CTR Encrypted:", ctr_encrypted)
