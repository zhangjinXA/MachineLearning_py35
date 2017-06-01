import itchat

#自动登录
itchat.auto_login(hotReload=True)
另一个号 = itchat.search_friends(name='江清月近人')[0].UserName
#



#读取消息
@itchat.msg_register(msgType='Text',isFriendChat=True)
def text_reply(msg):



    itchat.send_msg(msg.User.NickName ,toUserName=另一个号)

    itchat.send_msg(msg.Content,toUserName=另一个号)

itchat.run()