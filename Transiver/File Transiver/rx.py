from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import time

def decrypt_data(encrypted_data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_data), AES.block_size)

# Function to remove both front and back preambles and sequence from file
def remove_preamble(file_path):
    global content
    
    detect_sequence = b'sts'
    preamble = bytes([0b10101010]) * 3000

    '''def rx():
            global content
            
            while(True):
                with open('rx src/rx.tmp', 'rb') as file:

                    content = file.read()
                    if(len(content)>10):print('conncted')
                    time.sleep(1)

                    start= content.find(b'sts')
                    if start!= -1:
                            print('file recieving')
                            end_name= content.rfind(b'sts')
                            name=content[start+3:end_name]
                            print(name)
                            end_index = content.rfind(b'end')
                            if end_index != -1:
                                start= content.find(b'sts')
                                content = content[start+3:end_index]
                                path='rx src/'+name.decode()
                                with open(path,'wb') as output:
                                    output.write(content)
                                    with open('rx src/rx.tmp','wb') as output:pass
                                       # open_file(path)
                                break'''

    with open(file_path, 'rb') as file:
        content = file.read()

    start_index = content.find(detect_sequence)
    if start_index != -1:
        content = content[start_index + len(detect_sequence):]

    second_detect_index = content.find(detect_sequence)
    file_name = content[:second_detect_index]
    content = content[second_detect_index + len(detect_sequence):]

    end_index = content.rfind(detect_sequence)
    if end_index != -1:
        content = content[:end_index]

    preamble_length = len(preamble)
    while True:
        start_index = content.find(preamble)
        if start_index == -1:
            break
        else:
            content = content[start_index + preamble_length:]

    while True:
        end_index = content.rfind(preamble)
        if end_index == -1:
            break
        else:
            content = content[:end_index]

    return file_name

# AES decryption
key = b'Sixteen byte key'  # AES key must be the same as used for encryption
iv = b'This is an IV456'  # AES IV must be the same as used for encryption

# Remove both front and back preambles and sequence from the output.tmp file
file_name = remove_preamble('src/tx.tmp')
decrypted_content = decrypt_data(content, key, iv)


# Remove both front and back preambles and sequence from the output.tmp file
output_file_path = f'rx src/{file_name.decode()}'
with open(output_file_path, 'wb') as output_file:
    output_file.write(decrypted_content)

