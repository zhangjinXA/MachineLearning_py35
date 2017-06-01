import itchat

#自动登录
itchat.auto_login(hotReload=True)
#
群信息 = itchat.search_chatrooms(name='🐯诚信天下🐯28开启')
#读取消息
@itchat.msg_register(msgType='Text',isGroupChat=True)
def text_reply(msg):

    if msg.FromUserName == 群信息[0].UserName:
        if msg.ActualNickName == 'jqmyd':
            print(msg.text)
    # return 'This is a new one'
itchat.run()

