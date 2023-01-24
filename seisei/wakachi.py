def word_mining(word_line):
	global word_list
	global flag

	if "printf" in word_line :
		word_line = word_line.replace(word_line[word_line.find('"'):word_line.rfind('"')+1],'')

	#	文字列 ("Canada", "America", "Brazil")
	elif ( '"' in word_line ) and ( '\'' in word_line ):
		word_line = word_line.replace(word_line[word_line.find('"'):word_line.rfind('"')+1],'')
	
	symbol_line = word_line
	word_line   = word_line\
	.replace(',',' ')\
	.replace(';',' ')\
	.replace('*',' ')\
	.replace('+',' ')\
	.replace('-',' ')\
	.replace('/',' ')\
	.replace('%',' ')\
	.replace('=',' ')\
	.replace('<',' ')\
	.replace('>',' ')\
	.replace('!',' ')\
	.replace('.',' ')\
	.replace('[',' ')\
	.replace(']',' ')\
	.replace('(',' ')\
	.replace(')',' ')\
	.replace('{',' ')\
	.replace('}',' ')\
	.replace('&',' ')\
	.replace('|',' ')\
	.replace('#',' ')\
	.replace('?',' ')\
	.replace('"',' ')\
	.replace('\'',' ')\
	.replace("\t",' ')\
	.replace("\n",' ')\
	.replace(' 0 ',' ')\
	.replace(' 1 ',' ')\
	.replace(' 2 ',' ')\
	.replace(' 3 ',' ')\
	.replace(' 4 ',' ')\
	.replace(' 5 ',' ')\
	.replace(' 6 ',' ')\
	.replace(' 7 ',' ')\
	.replace(' 8 ',' ')\
	.replace(' 9 ',' ')\
	
	word_list.append(word_line)
	return symbol_line
	

def pos_mining(symbol_line):
	global pos_list
	global symbol_list
	global s_list
	global flag
	s_size    = len(s_list)
	list1     = []
	list2     = ''
	
	if(flag == 0):
	
		for i in range(s_size):
		
			if s_list[i] in symbol_line:
				pos = symbol_line.find(s_list[i])
				
				if serch_same(list1, pos) == 0:
					list1.append(pos)
					list2 += s_list[i] + ' '

	pos_list.append(list1)
	symbol_list.append(list2)
	
	
def serch_same(list, pos):
	size = len(list)
	
	if size == 0:
		return 0
	
	for i in range(size):
		if list[i] == pos:
			return 1
	
	return 0

	
def write_list(word_list, symbol_list):
	global path2
	global path3
	f1    = open(path2, 'w', encoding="utf-8", newline='')
	f2    = open(path3, 'w', encoding="utf-8", newline='')
	size1 = len(word_list)
	size2 = len(symbol_list)
	
	for i in range(size1):
		f1.write(word_list[i] + "\n")
	f1.close()
	
	for j in range(size2):
		f2.write(symbol_list[j] + "\n")
	f2.close()
	

def print_list(list):
	size = len(list)
	for i in range(size):
		print("{} : {}".format(i, list[i]))


def wakachi(p1, p2, p3):
	global path1
	global path2
	global path3

	path1 = p1
	path2 = p2
	path3 = p3
	f     = open(path1, 'r', encoding="utf-8")
	line  = f.readline()
	
	while line:
		pos_mining(word_mining(line))
		line = f.readline()
		
	write_list(word_list, symbol_list)
	f.close()


#main
s_list = [                                            \
	          "<=", ">=", "==", "!=",                   \
	          "+=", "-=", "*=", "/=", "%=", "++", "--", \
			  		"&&", "||",                               \
			  		"->",                                     \
	          '*', '+', '-', '/', '%',                  \
			  		'<', '>',                                 \
			  		'&', '|', '?',                       \
			  ]
"""
'[', ']', '(', ')', '{', '}'

'#', ',', ';', '"', '\''

などは出題しないのでリストから除外する
"""

word_list   = []
pos_list    = []
symbol_list = []
flag        = 0
path1       = ''
path2       = ''
path3       = ''
