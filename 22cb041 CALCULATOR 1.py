import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
)
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Modern Calculator')
        self.setGeometry(300, 300, 400, 400)
        self.setStyleSheet("background-color: #2d2d2d;")  # Dark background

        # Main layout
        vbox = QVBoxLayout()
        
        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            "background-color: #000000; color: white; font-size: 30px; padding: 10px;"
        )
        vbox.addWidget(self.display)

        # Grid layout for buttons
        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4)  # Clear button spanning across the row
        ]

        for btn_text, row, col, *span in buttons:
            button = QPushButton(btn_text)
            button.setStyleSheet(
                "font-size: 24px; background-color: #333; color: white; border-radius: 10px;"
            )
            button.clicked.connect(self.on_button_clicked if btn_text != '=' else self.on_equal_clicked)
            if btn_text == 'C':
                button.clicked.connect(self.on_clear_clicked)
            grid.addWidget(button, row, col, *span)

        vbox.addLayout(grid)
        self.setLayout(vbox)

        self.current_value = ''
        self.result = 0
        self.operator = ''

    def on_button_clicked(self):
        sender = self.sender()
        self.current_value += sender.text()
        self.display.setText(self.current_value)

    def on_clear_clicked(self):
        self.current_value = ''
        self.result = 0
        self.operator = ''
        self.display.setText('')

    def on_equal_clicked(self):
        try:
            self.result = eval(self.current_value)
            self.display.setText(str(self.result))
            self.current_value = str(self.result)
        except Exception as e:
            self.display.setText('Error')
            self.current_value = ''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
