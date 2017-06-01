import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
font_path = 'C:\\Windows\\fonts\\msyh.ttc'

s1 = """ 在克鲁伊夫时代，巴萨联赛中完成了四连冠，后三个冠军都是在末轮逆袭获得的。
在91/92赛季，巴萨末轮前落后皇马1分，结果皇马客场不敌特内里费使得巴萨逆转。
一年之后，巴萨用几乎相同的方式逆袭，皇马还是末轮输给了特内里费。
在93/94赛季中，巴萨末轮前落后拉科1分。
巴萨末轮5比2屠杀塞维利亚，拉科则0比0战平瓦伦西亚，巴萨最终在积分相同的情况下靠直接交锋时的战绩优势夺冠。
神奇的是，拉科球员久基奇在终场前踢丢点球，这才有了巴萨的逆袭。"""

s2 = """ like me who are you"""


# mylist = [s1, s2, s3]
# word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
word_list = jieba.cut(s1)
new_text = ' '.join(word_list)
wordcloud = WordCloud(
    font_path=font_path,
    background_color="black")
wordcloud.generate(new_text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

