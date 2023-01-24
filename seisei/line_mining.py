def read_file(f_name1, f_name2):
    global word_list
    global t_list
    global str_list
    global id_list
    global f
    
    f1    = open(f_name1, 'r', encoding='UTF-8', newline='')
    f2    = open(f_name2, 'r', encoding='UTF-8', newline='')
    line1 = f1.readline()
    line2 = f2.readline()
    sorce = 0
    count = 0
    
    while line1:
        word_list.append(line1)
        line1  = f1.readline()
        sorce += 1
    f1.close()
    
    while line2:
        id_list.append(line2.split(' '))
        line2  = f2.readline()
        count += 1
    f2.close()
    
    f.write("{} {} {}\n".format(sorce, count, 1))
    
    for word in word_list:
        t_list = word.replace("\n",'').split(' ')
        
        for t_str in t_list:
    
            if   t_str == '':
                continue
            
            elif t_str == "\n":
                continue
                
            else:
                str_list.append(t_str)
            
        word_count(str_list)
        str_list.clear()
        t_list.clear()
        
    f1.close()
    
    
def word_count(str_list):
    global f
    
    str_list.sort()
    kind  = len(set(str_list))
    flag  = 0
    prev  = ''
    
    f.write("{} ".format(kind))
    
    for str in str_list:
        
        if prev != str:
            f.write("{}:{} ".format(search_id(str, len(id_list)), str_list.count(str)))
        
        prev = str
        
    f.write("\n")


def search_id(str, id_size):
    global id_list
    
    for i in range(id_size):
        if id_list[i][1] == str:
            return id_list[i][0]
    
    
def line_mining(path1, path2, path3):
    global f
    
    f = open(path3, 'w', encoding='UTF-8')
    read_file(path1, path2)
    f.close()
    
    
word_list = []
t_list    = []
str_list  = []
id_list   = []
f         = None
