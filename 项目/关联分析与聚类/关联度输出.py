from sklearn import preprocessing as pre

def output_HaveLabelEncoding(关联度,outfile,le):
    # outfile = file+'test.csv'
    f = open(outfile, 'w')
    print('A1,n,A2,支持度,置信度', file=f)
    for temp in 关联度:
        #输出到屏幕
        print(le.inverse_transform(temp[0]),
              ',->,',
              le.inverse_transform(temp[1]),
              ',支持度：',
              temp[2],',置信度：',
              temp[3]
              )
        #输出到文本
        print(le.inverse_transform(temp[0]),
              ',->,',
              le.inverse_transform(temp[1]),
              ',',
              temp[2],',',
              temp[3],
              file = f
              )
    f.close()


def output_noLabelEncoding(关联度,outfile):
    # outfile = file+'test.csv'
    f = open(outfile, 'w')
    print('A1,n,A2,支持度,置信度', file=f)
    for temp in 关联度:
        #输出到屏幕
        print(temp[0],
              ',->,',
              temp[1],
              ',支持度：',
              temp[2],',置信度：',
              temp[3]
              )
        #输出到文本
        print(temp[0],
              ',->,',
              temp[1],
              ',',
              temp[2],',',
              temp[3],
              file = f
              )
    f.close()


def output_XHaveLabelEncoding(关联度,outfile,le):
    # outfile = file+'test.csv'
    f = open(outfile, 'w')
    print('A1,n,A2,支持度,置信度', file=f)
    for temp in 关联度:
        #输出到屏幕
        print(le.inverse_transform(temp[0]),
              ',->,',
              temp[1],
              ',支持度：',
              temp[2],',置信度：',
              temp[3]
              )
        #输出到文本
        print(le.inverse_transform(temp[0]),
              ',->,',
              temp[1],
              ',',
              temp[2],',',
              temp[3],
              file = f
              )
    f.close()


def output_YHaveLabelEncoding(关联度,outfile,le):
    # outfile = file+'test.csv'
    f = open(outfile, 'w')
    print('A1,n,A2,支持度,置信度', file=f)
    for temp in 关联度:
        #输出到屏幕
        print(temp[0],
              ',->,',
              le.inverse_transform(temp[1]),
              ',支持度：',
              temp[2],',置信度：',
              temp[3]
              )
        #输出到文本
        print(temp[0],
              ',->,',
              le.inverse_transform(temp[1]),
              ',',
              temp[2],',',
              temp[3],
              file = f
              )
    f.close()

def output_Have2LabelEncoding(关联度,outfile,leX,leY):
    # outfile = file+'test.csv'
    f = open(outfile, 'w')
    print('A1,n,A2,支持度,置信度', file=f)
    for temp in 关联度:
        #输出到屏幕
        print(leX.inverse_transform(temp[0]),
              ',->,',
              leY.inverse_transform(temp[1]),
              ',支持度：',
              temp[2],',置信度：',
              temp[3]
              )
        #输出到文本
        print(leX.inverse_transform(temp[0]),
              ',->,',
              leY.inverse_transform(temp[1]),
              ',',
              temp[2],',',
              temp[3],
              file = f
              )
    f.close()