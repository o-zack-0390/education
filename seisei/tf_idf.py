from sklearn.feature_extraction.text import TfidfVectorizer

def tf_idf():
    path1 = "result/sorce.txt"
    path2 = "result/tf-idf1.txt"
    path3 = "result/tf-idf2.txt"
    read_file(path1)
    cal_tfidf(path2, path3)


def read_file(path):
    global docs
    
    f    = open(path, 'r', encoding="utf-8")
    line = f.readline()
    
#   記号はletterが付いてないので無視されてしまう → 文字列に置き換える
    while line:
        line = line\
        .replace("<=", "Dainariicoru")\
        .replace(">=", "Syonariicoru")\
        .replace("==", "Icoru132")\
        .replace("!=", "Noticoru")\
        .replace("+=", "Plusicoru")\
        .replace("-=", "Mainusicoru")\
        .replace("*=", "Kakeruicoru")\
        .replace("%=", "Pasenticoru")\
        .replace("++", "Plusplus")\
        .replace("--", "Mainusmainus")\
        .replace("&&", "Katukatu")\
        .replace("||", "Matawamatawa")\
        .replace("->", "Mainussyonari")\
        .replace("*","Kakeru")\
        .replace("+","Pulas132")\
        .replace("-","Mainus132")\
        .replace("/","Waru132")\
        .replace("%","Amari132")\
        .replace("=","Dainyu132")\
        .replace("<","Dainari132")\
        .replace(">","Syonari132")\
        .replace("&", "And131")\
        .replace("!","Bikxtukuri")
        
        docs.append(line)
        line = f.readline()
        
    f.close()
        

def cal_tfidf(path1, path2):
    global docs

#   モデルの生成
    vectorizer = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b', lowercase=False, smooth_idf = False)
     
#   TF-IDFの計算
    values = vectorizer.fit_transform(docs).toarray()
     
#   特徴量ラベルの取得
    words = vectorizer.get_feature_names_out()
    
#   結果を出力
    size  = len(values)
    f1    = open(path1, 'w', encoding="utf-8", newline='')
    f2    = open(path2, 'w', encoding="utf-8", newline='')
    line  = ''
    
    for value in values:
        line = str(value).replace("\n", '')
        line = line[1:len(line)-1]
        f1.write(line + "\n")
        
    f1.close()
    
    for word in words:
        line = str(word)
        f2.write(line + ' ')
        
    f2.close()
    

docs = []