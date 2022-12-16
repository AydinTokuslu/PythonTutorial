import base64


filename = "new.deneme.txt"

with open(filename, "r") as fileObject:
    file_content = fileObject.read()

string_as_binary = base64.b64decode(file_content)
print(string_as_binary)
string = string_as_binary.decode("utf-8")

new_file_content = ""
for byte in string:
    new_file_content.encode(byte)
print(new_file_content)


with open(f"new-decode.{filename}", "w") as fileObject:
    fileObject.write(new_file_content)






# # decode
# string_as_base64 = b'UHl0aG9uIGlzIGF3ZXNvbWU='
#
#
# string_as_binary = base64.b64decode(string_as_base64)
# print(string_as_binary)  #bunu stringe çevirmemiz gerekir, şu an bytearray
# # b'Python is awesome'
#
# string = string_as_binary.decode("utf-8")
# print(string)  # Python is awesome