import base64


filename = "new.deneme.txt"

with open(filename, "r") as fileObject:
    file_content = fileObject.read()

new_file_content = ""
for character in file_content:
    new_character = ord(character) ^ 15
    new_file_content += chr(new_character)
print(new_file_content)


with open(f"decoded.{filename}", "w") as fileObject:
    fileObject.write(new_file_content)
