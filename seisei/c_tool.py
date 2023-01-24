import os
import importlib
import wakachi
import createtxt
import word_mining
import line_mining
import tf_idf
import write_tfidf
import sort_tfidf
import bsg
import generate

fname = input("ファイル名を入力\n")
root1 = "data/"
root2 = "data2/"
files = os.listdir("./data")

for filename in files:
  path1 = root1 + filename
  path2 = root2 + filename + "-1.txt"
  path3 = root2 + filename + "-2.txt"
  path2 = path2.replace(".c", '')
  path3 = path3.replace(".c", '')
  wakachi.wakachi(path1, path2, path3)
  importlib.reload(wakachi)

print("write : sorce.txt")
createtxt.createtxt()

path1 = "result/sorce.txt"
path2 = "result/word_id.txt"

word_mining.word_mining(path1, path2)
print("write : word_id.txt")

path1 = "result/sorce.txt"
path2 = "result/word_id.txt"
path3 = "result/line_inf.txt"

line_mining.line_mining(path1, path2, path3)
print("write : line_inf.txt")

tf_idf.tf_idf()
print("write : tf_idf.txt")

path1 = "result/tf-idf1.txt"
path2 = "result/tf-idf2.txt"
path3 = "result/generate_note.txt"
path4 = "result/uid.txt"

write_tfidf.write_tfidf(path1, path2, path3, path4, fname + "\n")
sort_tfidf.sort_tfidf(path3)
print("write : generate_note.txt")

path1 = "result/bsg1.txt"
path2 = "result/bsg2.txt"
path3 = "result/generate_note.txt"

bsg.bsg(path1, path2, path3)
print("write : bsg1.txt")
print("write : bsg2.txt")

path1 = "result/bsg1.txt"
path2 = "result/bsg2.txt"
path3 = "result/prob.c"
path4 = "data/" + fname

print("write : prob.c")
generate.generate(path4, path3, path1, path2)

print("Complete")

"""
実行パス
cd ./seisei
python c_tool.py
"""
