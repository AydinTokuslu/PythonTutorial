import base64



#encoding = şifreleme
string = "Python is awesome"
string_as_bytes = string.encode("utf-8")

string_as_base64 = base64.b64encode(string_as_bytes)
print(string_as_base64)  #şu an bytearray, bunu stringe çevirmemiz gerekir
# b'UHl0aG9uIGlzIGF3ZXNvbWU='

string = string_as_base64.decode("utf-8")
print(string)  # UHl0aG9uIGlzIGF3ZXNvbWU=

