import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QComboBox, QCheckBox, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Окно")
        self.resize(400, 300)
        
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Введите текст")
        
        self.button = QPushButton("Показать текст", self)

        
        self.label = QLabel("Результат будет отображён здесь", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        self.combo = QComboBox(self)
        self.combo.addItems(["Красный", "Зелёный", "Синий"])

        
        self.checkbox = QCheckBox("Жирный шрифт", self)
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.checkbox)

        self.setLayout(layout)
        
        
        self.button.clicked.connect(self.up_label)
        self.combo.currentIndexChanged.connect(self.up_color)
        self.checkbox.stateChanged.connect(self.up_font)


    def up_label(self):
        text = self.text_input.text()
        self.label.setText(text)
        
    def up_color(self):
        color = self.combo.currentText().lower()
        if color == "красный":
            color = "red"
        elif color == "зелёный":
            color = "green"
        elif color == "синий":
            color = "blue"
            
        self.label.setStyleSheet(f"color: {color};")
        
    
    def up_font(self):
        if self.checkbox.isChecked():
            font = QFont()
            font.setBold(True)
            self.label.setFont(font)
        else:
            font = QFont()
            font.setBold(False)
            self.label.setFont(font)
        
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())