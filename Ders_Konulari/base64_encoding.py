import base64
from math import log, ceil


#encoding = şifreleme
string = "Python is awesome"
string_as_bytes = string.encode("utf-8")

string_as_base64 = base64.b64encode(string_as_bytes)
print(string_as_base64)  #şu an bytearray, bunu stringe çevirmemiz gerekir
# b'UHl0aG9uIGlzIGF3ZXNvbWU='

string = string_as_base64.decode("utf-8")
print(string)  # UHl0aG9uIGlzIGF3ZXNvbWU=

##########################
# sayıları encoding yapma

number = 218374823748723
print("Sayımız bit olarak: ",bin(number))
# Sayımız bit olarak:  0b110001101001110001011001110011000010010001110011

number_of_byte = ceil(ceil(log(number, 2))/8) # 8 bite böleriz, ceil = numaray yukarı yuvarlama yapar

number_as_bytes = number.to_bytes(number_of_byte, byteorder="little")
print("Sayımızın byte ları : ", number_as_bytes)
# Sayımızın byte ları :  b's$\xccY\x9c\xc6'

number_as_base64 = base64.b64encode(number_as_bytes)
print("Sayımız Base64 olarak : ", number_as_base64)
# Sayımız Base64 olarak :  b'cyTMWZzG'