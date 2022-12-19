import re

def word_mining(word_line):
	global word_list
	global flag
	
	# コメント
	if("//" in word_line):
		word_line = ''
	
	if("/*" in word_line):
		flag = 1
		word_line = ''
	
	if("*/" in word_line):
		flag = 0
		word_line = ''
		
	if flag == 1:
		word_line = ''
	
	# #define, printf などの定義
	if  '#' in word_line :
		word_line = ''
	
	elif "printf" in word_line :
		word_line = ''
	
	# main関数
	elif re.compile(r'(int|void|) main\(').search(word_line) != None :
		word_line = ''
	
	# 配列の要素の初期値 x = {1,2,3};
	elif re.compile(r'( *} *; *)$').search(word_line) != None :
		word_line = word_line[:word_line.find('{')]
	
	# 文字列 ("Canada", "America", "Brazil")
	elif ( '"' in word_line ) and ("scanf" not in word_line):
		word_line = word_line.replace(word_line[word_line.find('"'):word_line.rfind('"')+1],'')
	
	symbol_line = word_line
	word_line   = word_line\
	.replace('0',' ')\
	.replace('1',' ')\
	.replace('2',' ')\
	.replace('3',' ')\
	.replace('4',' ')\
	.replace('5',' ')\
	.replace('6',' ')\
	.replace('7',' ')\
	.replace('8',' ')\
	.replace('9',' ')\
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
	.replace("if",' ')\
	.replace("for",' ')\
	.replace("while",' ')
	
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


#main
s_list = [                                            \
	          "<=", ">=", "==", "!=",                   \
	          "+=", "-=", "*=", "/=", "%=", "++", "--", \
	          "&&", "||",                               \
	          "->",                                     \
	          '*', '+', '-', '/', '%',                  \
	          '<', '>',                                 \
	          '.', '&', '|', '?',                       \
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
path1       = "data/ans.c"
path2       = "data/wakachi_1.txt"
path3       = "data/wakachi_2.txt"
f           = open(path1, 'r', encoding="utf-8")
line        = f.readline()

while line:
	pos_mining(word_mining(line))
	line = f.readline()

write_list(word_list, symbol_list)
#print_list(pos_list)
f.close()
