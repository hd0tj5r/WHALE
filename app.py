from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QComboBox,QPushButton, QVBoxLayout
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from  PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import shioaji as sj
from tqdm import tqdm
import matplotlib.ticker as ticker
import pandas as pd

matplotlib.use("Qt5Agg")  # 使用 Qt

#------------------------PyQt6介面--------------------------------
class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.axes = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)

class MyWidget(QWidget): # 視窗設定、顯示
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WhaleRich')  # 設定視窗標題
        self.resize(1240, 700)  # 設定視窗尺寸
        self.setUpdatesEnabled(True)  # 更新
        self.setStyleSheet('background-color:#000000;')  # 更改視窗顏色
        self.ui()
        self.ui2()

    def ui(self):  # 元件設定
        self.label1 = QLabel(self)
        self.label1.setText('商品名稱')
        self.label1.move(20, 20)    #x,y 設定位置和尺寸  
        self.label1.setStyleSheet('color: white;'
                                  'font-size:30px;')  # 選擇時的文字顏色、文字大小
        
        self.box = QtWidgets.QComboBox(self)   # 加入下拉選單
        self.box.addItems(['台指','小納'])   # 加入四個選項
        self.box.setGeometry(180,25,150,30)
        self.box.setStyleSheet('font-size:25px;'
                                'background-color:#ffffff;')  # 選擇時的文字顏色、文字大小

        
        self.label2 = QLabel(self)
        self.label2.setGeometry(10,90,250,200)
        self.label2.setStyleSheet('color: white;'
                                  'font-size:25px;')
        self.label2.setText(f'''
        日K
                     
        漲: {self.x()}
        盤: {self.y()}
        跌: {self.width()}
        ''')

        self.label3 = QLabel(self)
        self.label3.setGeometry(150,90,250,200)
        self.label3.setStyleSheet('color: white;'
                                  'font-size:25px;')
        self.label3.setText(f'''
        60K
                     
        漲: {self.y()}
        盤: {self.y()}
        跌: {self.width()}
        ''')

        self.label4 = QLabel(self)
        self.label4.setGeometry(300,90,250,200)
        self.label4.setStyleSheet('color: white;'
                                  'font-size:25px;')
        self.label4.setText(f'''
        15K
                     
        漲: {self.x()}
        盤: {self.y()}
        跌: {self.width()}
        ''')

        self.label5 = QLabel(self)
        self.label5.setGeometry(450,90,250,200)
        self.label5.setStyleSheet('color: white;'
                                  'font-size:25px;')
        self.label5.setText(f'''
        5K
                     
        漲: {self.x()}
        盤: {self.y()}
        跌: {self.width()}
        ''')

        self.label6 = QLabel(self)
        self.label6.setGeometry(600,90,250,200)
        self.label6.setStyleSheet('color: white;'
                                  'font-size:25px;')
        self.label6.setText(f'''
        1K
                     
        漲: {self.x()}
        盤: {self.y()}
        跌: {self.width()}
        ''')

        
        self.label7 = QLabel(self)
        self.label7.move(400, 23)
        self.label7.setStyleSheet('color:#FFFF93;'
                                  'font-size:25px;')
        self.label7.setText(f'''即時指數|台指:{self.x()}    小納:{self.x()}''')


    def ui2(self):
        #建立視窗中的網格
        style_box = '''
            background:	#ADADAD;
            border:3px solid #fff;
            border-radius:5px;
        '''
        box = QtWidgets.QWidget(self)
        box.setGeometry(50,300,1130,350)
        box.setStyleSheet(style_box)

if __name__ == '__main__':  # 視窗啟動與結束
    app = QApplication(sys.argv)  # 開啟
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())  # 結束