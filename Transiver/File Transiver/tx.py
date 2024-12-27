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
    end_sequence = b'end'  # Sequence to detect end of file

    # AES encryption
    key = b'Sixteen byte key'  # AES key must be either 16, 24, or 32 bytes long
    iv = b'This is an IV456'  # AES IV must be 16 bytes long
    encrypted_plaintext = encrypt_data(plaintext, key, iv)
    
    with open('src/tx.tmp', 'wb') as output_file:
        output_file.write(preamble + detect_sequence + file_name + b'|||' + encrypted_plaintext + end_sequence + preamble)

#Adds the preamble
add_preamble()
