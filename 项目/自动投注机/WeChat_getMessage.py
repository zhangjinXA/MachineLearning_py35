import itchat
import re
from 项目.自动投注机 import txt_transform
import pandas  as pd
import time
import os

file = 'C:\\Users\\30708\\Desktop\\活儿\\2017-6-4 财务机器人\\'
指定群名 = 'test0604'
# 积分数据 = 'jifen.csv'
#
# '''
# 参数初始化
# '''
#读取标识符
#必须含有群里所有联系人
#
# dict = seq.get_SeqID().get_dic_ofAllFriends();
#
# #
# #初始化积分
# if not os.path.exists(file+积分数据):
#     all_contacts = []
#     for key in dict.keys():
#         seqID = dict[key]
#         temp = [seqID,key,0,0,0,0,0,0]
#         all_contacts.append(temp)
#
#     all_contacts = pd.DataFrame(all_contacts,\
#         columns=['seqID','NickName','当前积分','当前押分','当前可用积分',	'总盈亏','今日盈亏','总流水'])
#     all_contacts.to_csv(file+积分数据,index=False)

'''****************************************************************************************************'''

itchat.auto_login(hotReload=True) #登录

#指定回馈群
#指定输出文件夹
#初始化联系人积分
群 = itchat.search_chatrooms(name=指定群名)[0]
指定群 = 群.UserName
#建立dict_group:指定回馈群人员昵称与username
dict_group = {}
for i in 群.MemberList : dict_group[i.UserName] = i.NickName


today_date = time.strftime('%Y-%m-%d',
                           time.localtime(
                               time.time()
                           ))

outFile = file + today_date+'\\'
if  not os.path.exists(outFile) : os.mkdir(outFile)





已处理msgID = []
#
#读取消息
@itchat.msg_register(msgType='Text',isGroupChat=True)
def text_reply(msg):


    global 已处理msgID,dict_group
    txt = msg.text
    msgID = msg.NewMsgId
    msgCreatTime = msg.CreateTime


    if msg.FromUserName == 指定群:
        if msgID not in 已处理msgID:

            ##############################################################################
            #转换真实昵称
            #如果不存在则更新群信息及dict_group
            t_s = True
            while t_s:
                try:
                    person_NickName = dict_group[msg.ActualUserName]
                    t_s = False
                except:
                    itchat.send_msg('用户昵称发生变更请重启程序',toUserName=指定群)

            ##############################################################################

            person_seqID = person_NickName #seqID为用户唯一标识，暂使用用户真实昵称替代。

            t_txt = txt_transform.txt_transfom(txt)#消息按规则分解
            #
            #===============================================================================================
            if t_txt[0] != -99:

                #整理输出数据
                output_recoder = []
                for i in t_txt:
                    temp = [msgCreatTime] + i
                    output_recoder.append(temp)
                output_recoder = pd.DataFrame(output_recoder,columns=['下注时间','车道','号码','押分'])

                #自动回复到群里
                temp = '@'+person_NickName+'\n下注成功\n'+msg.text+'\n'
                for i in output_recoder.values.tolist():
                    temp += str(i)+'\n'
                itchat.send_msg(temp,toUserName=msg.FromUserName)
                #输出
                #判断文件是否存在
                #若存在则更新
                #若不存在则新写
                outFileName = outFile + str(person_seqID)+'.csv'
                isExist = os.path.exists(outFileName)

                if not isExist:
                    output_recoder.to_csv(outFileName,index=False,mode='w')
                else:
                    output_recoder.to_csv(outFileName, index=False, mode='a',header=False)

            # ===============================================================================================

            #已处理id记录
            已处理msgID.append(msgID)
            if len(已处理msgID) > 200:
                已处理msgID = 已处理msgID[100:]
            # print(已处理msgID)


itchat.run()




