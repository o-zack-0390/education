import importlib
import wakachi
import word_mining
import line_mining
import TFIDF
import generate

path1 = "data/wakachi_1.txt"
path2 = "data/word_id_1.txt"
path3 = "data/wakachi_2.txt"
path4 = "data/word_id_2.txt"

wakachi.wakachi()
print("write : wakachi.txt")

word_mining.word_mining(path1, path2)
print("write : word_id_1.txt")

importlib.reload(word_mining)
word_mining.word_mining(path3, path4)
print("write : word_id_2.txt")

path1 = "data/wakachi_1.txt"
path2 = "data/word_id_1.txt"
path3 = "data/line_inf_1.txt"
path4 = "data/wakachi_2.txt"
path5 = "data/word_id_2.txt"
path6 = "data/line_inf_2.txt"

line_mining.line_mining(path1, path2, path3)
print("write : line_inf_1.txt")

importlib.reload(line_mining)
line_mining.line_mining(path4, path5, path6)
print("write : line_inf_2.txt")

TFIDF.TFIDF(0)
print("write : bsg_1.txt")

importlib.reload(TFIDF)
TFIDF.TFIDF(1)
print("write : bsg_2.txt")

print("write : prob.c")
generate.generate()

print("\nComplete\n")
