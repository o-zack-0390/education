import math
import random
import copy
import sys


def read_value():
	global path1
	f    = open(path1)
	line = f.readline()
	
	# 分類対象の文書数と単語数
	doc_inf    = line.split(' ')
	total_doc  = int(doc_inf[0])
	total_word = int(doc_inf[1])
	v          = doc_inf[2]
	#print(total_doc, total_word, v)
	
	list        = []
	word_list   = []
	TF_list     = []
	TF_IDF_list = []
	IDF_list    = [0] *total_word
	
	for i in range(total_doc):
		line = f.readline().split(' ')
		word_num = int(line[0])
		word_list.append(line[1:])
		word_list[i].pop()
		TF_IDF_list.append([0]*len(word_list[i]))
		
		for j in range(word_num):
			pos = word_list[i][j].find(':')
			list.append(int(word_list[i][j][pos+1:]))
			word_list[i][j] = int(word_list[i][j][:pos]) - 1
		TF_list.append(list)
	
	f.close()
	return word_list, TF_list, IDF_list, TF_IDF_list, total_doc, total_word


def TF_IDF(word_list, TF_list, IDF_list, TF_IDF_list, total_doc):
	
	# 文書数まで繰り返し
	for i in range(total_doc):
		word_num = len(word_list[i])
		
		# 一つの文書の単語数まで繰り返し
		for j in range(word_num):
			IDF_list[word_list[i][j]] += 1
	
	# 文書数まで繰り返し
	for i in range(total_doc):
		word_num = len(word_list[i])
		
		# 一つの文書の単語数まで繰り返し
		for j in range(word_num):
			IDF_list[word_list[i][j]] = math.log2(total_doc / IDF_list[word_list[i][j]] + 1)
			TF_IDF_list[i][j] = TF_list[i][j] * IDF_list[word_list[i][j]]
	
	return IDF_list, TF_IDF_list


def init_data(word_list, TF_IDF_list, total_doc, total_word):
    ID_list = [0]*total_word
	
    for i in range(total_doc):
        index_size = len(word_list[i])
        
        for j in range(index_size):
            pos          = word_list[i][j]
            ID_list[pos] = TF_IDF_list[i][j]
    
    return read_name(ID_list)


def read_name(ID_list):
	global path2
	f     = open(path2)
	line  = f.readline()
	index = 0
	
	while(line):
		text    = line.split(' ')
		ID_list[index] = (text[1], ID_list[index])
		index += 1
		line = f.readline()
	
	f.close()
	return ID_list


def word_sort(ID_list, total_word):
	ID_list = sorted(ID_list, key = lambda x:x[1], reverse = True)
	q_sum   = int(total_word / 1.5) - 1
	q_roop  = int(total_doc / 7)
	q_list  = []
	q_size  = 0
	count   = 0
	r_list  = rand_ints_nodup(0, q_sum, q_roop)

	if len(r_list) < q_roop:
		q_roop  = len(r_list)
	
	for i in range(q_roop):
		q_list.append(ID_list[r_list[i]][0])
	
	return ID_list, q_list


def symbol_sort(ID_list, total_word):
	ID_list = sorted(ID_list, key = lambda x:x[1], reverse = True)
	q_sum   = int(total_word / 2)
	q_roop  = int(total_word / 3) + 1
	q_list  = []
	q_size  = 0
	count   = 0
	r_list  = rand_ints_nodup(0, q_sum, q_roop)

	if len(r_list) < q_roop:
		q_roop  = len(r_list)
	
	for i in range(q_roop):
		q_list.append(ID_list[r_list[i]][0])
	
	return ID_list, q_list

	
def rand_ints_nodup(a, b, k):
	break_count = 0
	ns = []
  
	while len(ns) < k:
		n = random.randint(a, b)

		if 300 < break_count:
			break
	
		if not n in ns:
			ns.append(n)

		break_count += 1
	  
	return ns


def write_list(list):
	global path3
	f    = open(path3, 'w', encoding="utf-8", newline='')
	size = len(list)
	
	for i in range(size):
		f.write(list[i] + "\n")
		
	f.close()


def print_list(list):
	size = len(list)
	for i in range(size):
		print("{} : {}".format(i+1, list[i]))


order = int(input())

if order == 0:
	path1 = "data/line_inf_1.txt"
	path2 = "data/word_id_1.txt"
	path3 = "data/bsg.txt"
	
elif order == 1:
	path1 = "data/line_inf_2.txt"
	path2 = "data/word_id_2.txt"
	path3 = "data/bsg2.txt"

else:
	print("input error")
	sys.exit()

word_list, TF_list, IDF_list, TF_IDF_list, total_doc, total_word \
= read_value()

IDF_list, TF_IDF_list \
= TF_IDF(word_list, TF_list, IDF_list, TF_IDF_list, total_doc)

ID_list \
= init_data(word_list, TF_IDF_list, total_doc, total_word)

if order == 0:
	ID_list, q_list = word_sort(ID_list, total_word)

else:
	ID_list, q_list = symbol_sort(ID_list, total_word)

write_list(q_list)
print_list(ID_list)

'''
実行コマンド
python TF-IDF.py
'''
