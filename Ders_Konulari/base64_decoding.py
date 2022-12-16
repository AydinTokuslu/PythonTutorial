import base64

# decode
string_as_base64 = b'UHl0aG9uIGlzIGF3ZXNvbWU='


string_as_binary = base64.b64decode(string_as_base64)
print(string_as_binary)  #bunu stringe çevirmemiz gerekir, şu an bytearray
# b'Python is awesome'

string = string_as_binary.decode("utf-8")
print(string)  # Python is awesome