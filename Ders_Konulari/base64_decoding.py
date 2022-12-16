import base64

# decode
string_as_base64 = b'UHl0aG9uIGlzIGF3ZXNvbWU='


string_as_binary = base64.b64decode(string_as_base64)
print(string_as_binary)  #bunu stringe çevirmemiz gerekir, şu an bytearray
# b'Python is awesome'

string = string_as_binary.decode("utf-8")
print(string)  # Python is awesome


##########################
# sayıları decoding yapma

number_as_base64 = b'cyTMWZzG'
# number = 218374823748723, aradığımız sayı

number_as_bytes = base64.b64decode(number_as_base64)
print("Sayımızın byte'ları : ", number_as_bytes)
# Sayımızın byte'ları :  b's$\xccY\x9c\xc6'

number = int.from_bytes(number_as_bytes, byteorder="little")
print(number)  # 218374823748723