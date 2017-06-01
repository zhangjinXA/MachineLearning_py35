import pandas as pd

def read_XiGua(file):
    data = pd.read_csv(file, index_col=0, encoding='utf-8')
    # 去除空格
    icolumns = data.columns.values
    num_col, num_row = len(icolumns), len(data.iloc[:, 0])
    # column去除空格
    for icol in range(num_col):    icolumns[icol] = icolumns[icol].strip()
    data.columns = icolumns
    # values去除空格
    for icol in range(num_col):
        for irow in range(num_row):
            if type(data.iloc[irow, icol]) == str:
                data.iloc[irow, icol] = (data.iloc[irow, icol]).strip()
                # 去除完成
    data.to_csv('C:\\Users\\ZhangSSD\\Desktop\\新建文件夹\\xigua.csv')
    return data