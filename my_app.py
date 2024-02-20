from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

from instr import *  #загружаем переменные из файла instr.py
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # устанавливает, как будет выглядеть окно
        self.initUI() # создаём и настраиваем графические элементы
        self.connects() # устанавливает связи между элементами
        self.show()  # показываем окно
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.setStyleSheet("background-color: rgb(120,219,226);")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setFont(QFont("Times", 18, QFont.Bold))
        self.instruction = QLabel(txt_instruction)
        self.instruction.setFont(QFont("Times", 12, italic=True))
        self.btn_next = QPushButton(txt_next)
        self.btn_next.setFont(QFont("Times", 12, QFont.Bold))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.btn_next)
        self.setLayout(self.layout)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
mw = MainWin()
app.exec_()
