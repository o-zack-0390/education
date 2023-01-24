def read_file(f_name):
    global str_list
    
    f      = open(f_name, 'r', encoding='UTF-8', newline='')
    line   = f.readline()
    t_list = []
    
    while line:
        t_list += line.split(' ')
        line    = f.readline()
    t_size = len(t_list)
    
    for _str in t_list:
    
        if   _str == '':
            continue
        
        elif _str == "\n":
            continue
            
        else:
            str_list.append(_str)
            
    str_list.sort()
    f.close()
    
    
def count_word(f_name):
    global index_list
    global str_list
    
    f    = open(f_name, 'w', encoding='UTF-8')
    prev = ''
    w_id = 1
    
    for _str in str_list:
    
        if prev != _str:
            f.write("{} {} {}\n".format(w_id, _str, str_list.count(_str)))
            w_id += 1
            
        prev  = _str
        
    f.close()


def word_mining(path1, path2):
    read_file(path1)
    count_word(path2)
    
    
str_list   = []
index_list = []
