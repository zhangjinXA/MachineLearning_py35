import pandas as pd
import docx
def readDocx(docName):
    fullText = []
    doc = docx.Document(docName)
    paras = doc.paragraphs
    for p in paras:
        fullText.append(p.text)
    return fullText
    # return '\n'.join(fullText)
def get_train_data():

    doc_file = 'C:\\Users\\ZhangSSD\\Desktop\\智能聊天机器人项目\\data.docx'
    excel_file = 'C:\\Users\\ZhangSSD\\Desktop\\智能聊天机器人项目\\data.xlsx'
    csv_file = 'C:\\Users\\ZhangSSD\\Desktop\\智能聊天机器人项目\\data.csv'

    data_doc = readDocx(doc_file)
    data_Excel = pd.read_excel(excel_file,0)
    data_csv = pd.read_csv(csv_file)

    data_table = pd.concat([data_Excel,data_csv])
    for i in range(len(data_table.index)):
        data_doc.append(data_table.iloc[i,0])
        data_doc.append(data_table.iloc[i,1])

    return data_doc