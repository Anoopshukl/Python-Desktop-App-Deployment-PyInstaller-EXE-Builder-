import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class GamingCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🎮 CyberCalc Pro")
        self.setFixedSize(420, 650)

        self.setStyleSheet("""
            QWidget{
                background-color:#0d1117;
            }

            QLineEdit{
                background:#161b22;
                color:#00ff99;
                border:2px solid #00ff99;
                border-radius:15px;
                padding:15px;
                font-size:28px;
                font-weight:bold;
            }

            QPushButton{
                background:#161b22;
                color:white;
                border:2px solid #00ffff;
                border-radius:15px;
                font-size:22px;
                font-weight:bold;
                min-height:70px;
            }

            QPushButton:hover{
                background:#00ffff;
                color:black;
            }

            QPushButton:pressed{
                background:#00ff99;
                color:black;
            }
        """)

        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFont(QFont("Consolas", 24))

        layout.addWidget(self.display)

        grid = QGridLayout()

        buttons = [
            ('7',0,0), ('8',0,1), ('9',0,2), ('/',0,3),
            ('4',1,0), ('5',1,1), ('6',1,2), ('*',1,3),
            ('1',2,0), ('2',2,1), ('3',2,2), ('-',2,3),
            ('0',3,0), ('.',3,1), ('=',3,2), ('+',3,3),
            ('C',4,0)
        ]

        for text,row,col in buttons:
            btn = QPushButton(text)

            if text == "=":
                btn.clicked.connect(self.calculate)
            elif text == "C":
                btn.clicked.connect(self.clear)
            else:
                btn.clicked.connect(lambda checked, t=text: self.add_text(t))

            grid.addWidget(btn,row,col)

        layout.addLayout(grid)

        self.setLayout(layout)

    def add_text(self,text):
        self.display.setText(self.display.text() + text)

    def clear(self):
        self.display.clear()

    def calculate(self):
        try:
            result = str(eval(self.display.text()))
            self.display.setText(result)
        except:
            self.display.setText("ERROR")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = GamingCalculator()
    window.show()

    sys.exit(app.exec())