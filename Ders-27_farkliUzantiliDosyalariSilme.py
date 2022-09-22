import os

def delete_files():
    dextension=[".aux",".bb1",".lof",".lot",".out",".toc"]
    files=os.listdir()
    dfiles=[]

    for file in files:
        if file[len(file)-4:] in dextension:
            dfiles.append(file)

    for file in dfiles:
        os.remove(file)

delete_files()