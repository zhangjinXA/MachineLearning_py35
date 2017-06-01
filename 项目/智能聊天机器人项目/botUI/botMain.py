# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from 项目.智能聊天机器人项目.botUI.Ui_botMain import Ui_MainWindow
from 项目.智能聊天机器人项目.chatterbot01 import chatBot


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        self.textss = ""
        self.bot = chatBot()
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        ask = self.textBrowser.toPlainText()
        ask = ask.replace('\n','')
        anwsor = self.bot.get_response(ask)
        self.textss = self.textss + ask + '\n' + anwsor+'\n\n'
        self.textBrowser.setText('')
        self.textBrowser_2.setText(self.textss)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
