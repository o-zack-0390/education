# coding:shift-jis
import re


# �R�����g�Ƌ󔒕�����ǂݍ��܂Ȃ��悤�ɂ���
def delete_sorce(line):
	s_line = line
	
	# "//"�����݂��邩���ׂ�
	pos1 = s_line.find("//")
	
	# "//"�����݂���Ȃ�폜����
	if pos1 != -1:
		s_line = line[:pos1]
	
	# "/*"��"*/"�����݂��邩���ׂ�
	pos2 = s_line.find("/*")
	pos3 = s_line.find("*/")
	
	# "/*"�����݂���ꍇ
	if pos2 != -1:
	
		# "/*" �� "*/" �����݂���ꍇ
		if pos3 != -1:
			s_line = s_line[:pos2] + s_line[pos3+2:]
		
		# "/*"�݂̂����݂���ꍇ
		else:
			s_line = s_line[:pos2]


	#�󔒕������폜
	s_line = s_line.replace(' ','')
	
	#�R�����g�Ƌ󔒕������l�������\�[�X�R�[�h��ԋp����
	return s_line


def struct_check(correct, miss, p2, p3, p4):
	search_str = delete_sorce(miss)
	flag = 1
	
	# *pos=d �̌`�����Ă���\�[�X�R�[�h��T��
	p2 = p2.search(search_str)
	
	p3 = p3.search(search_str)
	print(p3)
	
	p4 = p4.search(search_str)
	print(p4)
	
	
	str = miss.split('*')
	str_len = len(str)
	
	
	if p3 != None:
		print("�l�����Z\n")
	
	
	elif p4 != None:
		print("�|�C���^\n")

	
	

	
	# *pos=d �̌`�����������ꍇ�͊ԈႦ�Ă�\��������̂Ő�����\������
	#if p != None:
		#print("\n\n\n���̉\��������ӏ�\n\n\n")
		#print("�͔̓v���O����\n\n" + correct + "\n\n")
		#print("�w�K�҂̃v���O����\n\n" + miss + "\n\n")
		#print("�����l�̐ݒ肪�ρB�z��̐擪�v�f��ݒ肵�Ă��Ȃ��B\n")
		#print("�z��̗v�f��ύX����ƕs�����ɂȂ邩������Ȃ��B\n")
		
	
def loop(correct_list, miss_list, size):

	# *pos=d (d�͔C�ӂ̐���) �̌`��Ώۂɂ���
	p1 = re.compile(r'.+pos=\d|.+=-\d')
	
	# �l�����Z (�|�C���^�͏��O)
	p2 = re.compile(r'(\(*\**[a-zA-Z0-9]+\)*)+')# (x)*(x)
	
	
	
	
	# �|���Z�̌`
	p3 = re.compile(r'(\(*[a-zA-Z0-9]+\)*\*\(*[a-zA-Z0-9]+\)*)+')# (x)*(x)
	
	# �|�C���^�̌`
	p4 = re.compile(r'\(*\*+\(*\**[a-zA-Z0-9]+\)*\)*')# (**(xx))
	
	for i in range(size):
		struct_check(correct_list[i], miss_list[i], p2, p3, p4)

# FILE *fq, char *fn1 �Ȃǂ͕ϐ��錾�ɕ��ނ���

