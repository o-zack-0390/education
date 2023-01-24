import os

def preprocessing(line):
    line = line.replace("\n", '')
    
    if "printf" in line:
        line = ''
    
    return line


def createtxt():
    write_f   = open('result/sorce.txt', 'w', encoding="utf-8", newline="")
    root_path = "data2/"
    files     = os.listdir("./data2")
    flag      = 0

    for filename in files:

        read_f = open(root_path + filename, 'r', encoding="utf-8")
        line   = read_f.readline()
        text   = ''
        
        while line:
            text += preprocessing(line)
            line  = read_f.readline()
            
        if flag == 1:
            write_f.write(text+"\n")
            flag = 0

        else:
            write_f.write(text)
            flag = 1

        read_f.close()
            
    write_f.close()

'''
cd reserch\education\preprocessing\create
python createtxt.py
'''
