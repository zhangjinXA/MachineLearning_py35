from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from 项目.智能聊天机器人项目 import get_train_data

class chatBot:

    def __init__(self):
        #存储适配器
        bot = ChatBot('QQ307080785',
                      #storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
                      #input_adapter="chatterbot.input.TerminalAdapter",
                      output_adapter="chatterbot.output.TerminalAdapter",
                      logic_adapters=["chatterbot.logic.MathematicalEvaluation",
                                      "chatterbot.logic.BestMatch"],
                      filters=['chatterbot.filters.RepetitiveResponseFilter'],#该滤波器用以消除潜在的重复响应，以避免chat bot多次重复已经的回答。
                      #database="./database.json"
                      )
        #自定义list训练
        train_date = get_train_data.get_train_data()
        bot.set_trainer(ListTrainer)
        bot.train(train_date)
        #语料库数据训练
        bot.set_trainer(ChatterBotCorpusTrainer)
        bot.train(
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations"
        )
        self.bot = bot

    '''获取答案'''
    def get_response(self,ask):
        print(ask)
        bot_input = self.bot.get_response(ask)
        # while True:
        #     try:
        #         bot_input = self.bot.get_response(None)
        #     except(KeyboardInterrupt, EOFError, SystemExit):
        #         break
        return bot_input
