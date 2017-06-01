import requests
import itchat

#自动登录
itchat.auto_login(hotReload=True)
#搜索指定群/朋友
朋友信息 = itchat.search_friends(name='呵呵呵呵')
朋友信息 = itchat.search_friends(wechatAccount='woaikeyan789')
群信息 = itchat.search_chatrooms(name='🐯诚信天下🐯28开启')
#结果解析，群操作类似
朋友信息[0].NickName  #朋友昵称
朋友信息[0].UserName #朋友编号
#
群主 = 群信息[0].ChatRoomOwner
群所有联系人 = 群信息[0].MemberList
#发送消息给指定
itchat.send_msg('这代表着使用PC自动发送微信的功能实现了...', toUserName=群信息[0].UserName)
#读取消息
@itchat.msg_register(msgType='Text',isGroupChat=True)
def text_reply(msg):
    msg.FromUserName          #此消息的发送者编号（个人，或 群编号）
    msg.ActualUserName        #此消息的实际发送人编号
    msg.ActualNickName        #此消息的实际发送人昵称
    msg.User.MemberList       #群所有联系人信息
    msg.text                  #消息内容

    # return 'This is a new one'   #自动回复
itchat.run()