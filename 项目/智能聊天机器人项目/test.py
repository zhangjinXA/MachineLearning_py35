from 项目.智能聊天机器人项目.chatterbot01 import chatBot

bot = chatBot()
ask = 'Where can I obtain the PSA Pass Conditions, the PSA Safety Rules and Vehicle Permit Conditions??'
out = bot.get_response(ask)

