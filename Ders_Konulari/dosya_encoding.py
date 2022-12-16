filename = "deneme.txt"

with open(filename, "rb") as fileObject:
    file_content = fileObject.read()

new_file_content = ""
for byte in file_content:
    new_file_content += chr(byte ^ 15)
print(new_file_content)


with open(f"new.{filename}", "w") as fileObject:
    fileObject.write(new_file_content)