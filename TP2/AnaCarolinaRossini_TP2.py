import sys
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QLineEdit, QPushButton

 
class MainWindow(QWidget): 
    def __init__(self): #constructeur
        super().__init__()  #constructeur Qwidget
        self.setWindowTitle("Ana Carolina Rossini - TP2 - Outliner Organizer Tool")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)

        #text
        label = QLabel("Enter JSON organization rules path:")
        layout.addWidget(label)
        
        #text input
        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        #checkboxes
        checkbox_selection = QCheckBox("Apply on selection only")
        checkbox_colors = QCheckBox("Apply colors")
        checkbox_reorder = QCheckBox("Apply reorder")
        layout.addWidget(checkbox_selection)
        layout.addWidget(checkbox_colors)
        layout.addWidget(checkbox_reorder)
        

        #push buttom
        self.button_organize = QPushButton('Organize outliner', self)        
        self.button_organize.clicked.connect(self.button_onClicked)
        layout.addWidget(self.button_organize)


        self.setLayout(layout)

       
    def button_onClicked(self):
        json_path = self.text_input.text()

        try:
            file = open(json_path, encoding="UTF-8") #open file as-is, have info such as size. encoding UTF-8 allows accents and special characters
            data = json.load(file) #interpret then load file into readeable data
            print("yay!")
        except:
            print("Error: Could not open file:", json_path)

        
 
def main():
    
    global widget
    widget = MainWindow()
    widget.show()
 
main()