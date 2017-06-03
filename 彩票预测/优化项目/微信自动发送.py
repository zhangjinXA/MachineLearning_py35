import time
import numpy as np
import itchat
import pandas as pd
from 彩票预测.优化项目.购买推荐 import 购买推荐

#
pred = 购买推荐()
pred.跨度 = 25
pred.下分 = 5
pred.车道 = range(10)
pred.算法 = 1
#自动下注，两者必须同时为1
投注状态 = 0
实时跟踪 = 1
#
file = 'C:\\Users\\30708\\Desktop\\预测\\'
name = '历史开奖数据.csv'
pred.file = file
#
#自动登录
itchat.auto_login(hotReload=True)
#
自己 = itchat.search_friends(name='江清月近人')[0].UserName
另一个号 = itchat.search_friends(name='叫什么名字好zxw')[0].UserName
#
所有群 =  itchat.get_chatrooms()
for i in 所有群:
    print(i.NickName)
#
指定群 = itchat.search_chatrooms(name='🐯诚信天下🐯3开启')[0].UserName
执行词  = '★诚信天下3开启★【【【开始竞猜】】】'
指定执行人 = '刘安澜'
#
#读取消息
@itchat.msg_register(msgType='Text',isGroupChat=True,isFriendChat=True)
def text_reply(msg):

    global 投注状态,实时跟踪
    if msg.FromUserName == 自己:
        text = msg.text; print(text)
        if text == '预测':
            [最新期数, 最新号码, 最新时间] = pred.update_data() #更新本地记录
            投注输出 = pred.输出推荐结果(0,100)                 #读取本地记录
            itchat.send_msg(pred.output_param())
            itchat.send_msg('%s期\n%s\n号码%s\n' % (最新期数, 最新时间, str(最新号码)))
            itchat.send_msg('预测：\n%s'%投注输出)
            itchat.send_msg('预测：\n%s' % 投注输出,toUserName=另一个号)

        if text == '暂停下注':投注状态 = 0
        if text == '自动下注':投注状态 = 1
        if text == '跟踪': 实时跟踪 = 1
        if text == '取消跟踪':实时跟踪 = 0

        if text[:2] == '车道':
            pred.车道 = np.asarray(text[2:].split('/'),dtype=np.int).tolist()
            itchat.send_msg(str(pred.车道))
        if text[:2] == '下分':
            pred.下分 = int(text[2:])
            itchat.send_msg(str(pred.下分))
        if text[:2] == '跨度':
            pred.跨度 = int(text[2:])
            itchat.send_msg(str(pred.跨度))
        if text[:2] == '算法':
            pred.算法 = int(text[2:])
            itchat.send_msg(str(pred.算法))
        if text[:4] == '连续个数':
            pred.连续个数 = int(text[4:])
            itchat.send_msg(str(pred.连续个数))

        if text[:3] == '@江清':

            # itchat.send_msg(text)
            #
            胜负 = int(text.split('\n')[2].split(':')[1])
            总分 = int(text.split('\n')[1].split(':')[1])

        if text == '？':
            itchat.send_msg('%s\n\n功能性命令：\n\n预测\n暂停下注\n自动下注\n跟踪\n取消跟踪'\
            % pred.output_param())

    '''
    群消息跟踪
    '''
    if msg.FromUserName == 指定群:
        if msg.ActualNickName == 指定执行人:


            if msg.text[:3] == '@江清':
                text = msg.text;itchat.send_msg(text)
                #


            if msg.text[:len(执行词)] == 执行词:

                if 实时跟踪 == 1:

                    [最新期数, 最新号码, 最新时间] = pred.update_data()  # 更新本地记录
                    time.sleep(20)
                    投注输出 = pred.输出推荐结果(0, 100)  # 读取本地记录
                    #
                    itchat.send_msg('%s期\n%s\n号码%s\n' % (最新期数, 最新时间, str(最新号码)))
                    itchat.send_msg('预测：\n%s' % 投注输出)
                    if len(投注输出) > 1 :
                        itchat.send_msg(投注输出,toUserName=另一个号)

                    if 投注状态 == 1:
                        itchat.send_msg('查',toUserName=指定群)
                        return 投注输出

                    if 投注状态 == 0 :
                        itchat.send_msg('暂停投注了')

itchat.run()