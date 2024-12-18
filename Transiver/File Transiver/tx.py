import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt_data(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(data, AES.block_size))

def add_preamble():
        # Example binary string
    binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
    file_path = 'src/tx.jpg'
    file_name = os.path.basename(file_path).encode()
    # file_extension = os.path.splitext(file_path)[1].encode()
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    preamble = binarypreamble * 3000
    detect_sequence = b'sts'  # Sequence to detect preamble

    # AES encryption
    key = b'Sixteen byte key'  # AES key must be either 16, 24, or 32 bytes long
    iv = b'This is an IV456'  # AES IV must be 16 bytes long
    encrypted_plaintext = encrypt_data(plaintext, key, iv)
    
    with open('src/tx.tmp', 'wb') as output_file:
        output_file.write(preamble + detect_sequence + file_name + detect_sequence + encrypted_plaintext + detect_sequence + preamble)




# #Encryption
# def pad(data):
#     # Padding the data to be a multiple of 16 bytes
#     return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

# def encrypt_file(file_path, key):
#     global ciphertext
    
#     plaintext = pad(plaintext)
#     cipher = AES.new(key, AES.MODE_ECB)  
#     ciphertext = cipher.encrypt(plaintext)

  



# # Encryption details

# predefined_key = b'Hello_IamMihiran'

# # Encrypt the file
# encrypt_file(file_path, predefined_key)

#Adds the preamble
add_preamble()
