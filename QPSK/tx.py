# Example binary string
binary_string = "1100101011110000"

# Ensure the length of the binary string is a multiple of 8
if len(binary_string) % 8 != 0:
    binary_string = binary_string.zfill(((len(binary_string) // 8) + 1) * 8)

# Convert binary string to an integer
integer_value = int(binary_string, 2)

# Convert the integer to a byte stream
# len(binary_string) // 8 gives the number of bytes needed
byte_stream = integer_value.to_bytes(len(binary_string) // 8, byteorder='big')

print("Binary string:", binary_string)
print("Byte stream:", byte_stream)
