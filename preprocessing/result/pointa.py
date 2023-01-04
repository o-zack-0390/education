# coding:shift-jis
import re


# コメントと空白文字を読み込まないようにする
def delete_sorce(line):
	s_line = line
	
	# "//"が存在するか調べる
	pos1 = s_line.find("//")
	
	# "//"が存在するなら削除する
	if pos1 != -1:
		s_line = line[:pos1]
	
	# "/*"と"*/"が存在するか調べる
	pos2 = s_line.find("/*")
	pos3 = s_line.find("*/")
	
	# "/*"が存在する場合
	if pos2 != -1:
	
		# "/*" と "*/" が存在する場合
		if pos3 != -1:
			s_line = s_line[:pos2] + s_line[pos3+2:]
		
		# "/*"のみが存在する場合
		else:
			s_line = s_line[:pos2]


	#空白文字を削除
	s_line = s_line.replace(' ','')
	
	#コメントと空白文字を考慮したソースコードを返却する
	return s_line


def struct_check(correct, miss, p2, p3, p4):
	search_str = delete_sorce(miss)
	flag = 1
	
	# *pos=d の形をしているソースコードを探す
	p2 = p2.search(search_str)
	
	p3 = p3.search(search_str)
	print(p3)
	
	p4 = p4.search(search_str)
	print(p4)
	
	
	str = miss.split('*')
	str_len = len(str)
	
	
	if p3 != None:
		print("四則演算\n")
	
	
	elif p4 != None:
		print("ポインタ\n")

	
	

	
	# *pos=d の形が見つかった場合は間違えてる可能性があるので説明を表示する
	#if p != None:
		#print("\n\n\n誤りの可能性がある箇所\n\n\n")
		#print("模範プログラム\n\n" + correct + "\n\n")
		#print("学習者のプログラム\n\n" + miss + "\n\n")
		#print("初期値の設定が変。配列の先頭要素を設定していない。\n")
		#print("配列の要素を変更すると不正解になるかもしれない。\n")
		
	
def loop(correct_list, miss_list, size):

	# *pos=d (dは任意の整数) の形を対象にする
	p1 = re.compile(r'.+pos=\d|.+=-\d')
	
	# 四則演算 (ポインタは除外)
	p2 = re.compile(r'(\(*\**[a-zA-Z0-9]+\)*)+')# (x)*(x)
	
	
	
	
	# 掛け算の形
	p3 = re.compile(r'(\(*[a-zA-Z0-9]+\)*\*\(*[a-zA-Z0-9]+\)*)+')# (x)*(x)
	
	# ポインタの形
	p4 = re.compile(r'\(*\*+\(*\**[a-zA-Z0-9]+\)*\)*')# (**(xx))
	
	for i in range(size):
		struct_check(correct_list[i], miss_list[i], p2, p3, p4)

# FILE *fq, char *fn1 などは変数宣言に分類する

