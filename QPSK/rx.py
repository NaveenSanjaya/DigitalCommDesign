# Function to remove both front and back preambles and sequence from file
def remove_preamble(file_path):
    global content
    
    detect_sequence = b'sts'
    preamble = bytes([0b10101010]) * 300

    with open(file_path, 'rb') as file:
        content = file.read()

    start_index = content.find(detect_sequence)
    if start_index != -1:
        content = content[start_index + len(detect_sequence):]

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



# Remove both front and back preambles and sequence from the output.tmp file
remove_preamble('E:\Projects\DigitalCommDesign\src\img_rx.tmp')
with open('E:\Projects\DigitalCommDesign\src\img_rx.jpg', 'wb') as file:
                file.write(content)

