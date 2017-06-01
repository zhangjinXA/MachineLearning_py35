import nltk
text1 = 'Moby Dick by Herman Melville 1851, where is your best data'
words = nltk.word_tokenize(text1,'english') #分词
words_type = nltk.pos_tag(words)# 词性标注
print(words_type)
#词干转换
s = nltk.stem.SnowballStemmer('english')
a = s.stem('loving')
#

