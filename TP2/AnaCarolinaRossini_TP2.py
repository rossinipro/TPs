import sys
import json
import maya.cmds as cmds
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
        self.checkbox_selection = QCheckBox("Apply on selection only")
        
        self.checkbox_colors = QCheckBox("Apply colors")
        self.checkbox_reorder = QCheckBox("Apply reorder")
        layout.addWidget(self.checkbox_selection)
        layout.addWidget(self.checkbox_colors)
        layout.addWidget(self.checkbox_reorder)

        #push buttom
        self.button_organize = QPushButton('Organize outliner', self)        
        self.button_organize.clicked.connect(self.button_onClicked)
        layout.addWidget(self.button_organize)


        self.setLayout(layout)

       
    def button_onClicked(self):

        # D:\University\Fall 2026\repos\TPs\TP2\rules.json

                #read JSON
        json_path = self.text_input.text()
        try:
            file = open(json_path, encoding="UTF-8") #open file as-is, have info such as size. encoding UTF-8 allows accents and special characters
            json_data = json.load(file) #interpret then load file into readeable data
            print("yay!")
        except:
            print("Error: Could not open file:", json_path)

       

        #verify if the selection checkbox is checked, if so, get the selected objects, otherwise get all objects in the outliner
        if self.checkbox_selection.isChecked():
            selected = cmds.ls(selection=True, type="transform", long=True) or []
            print("selected only")
        else:
            objects = cmds.ls(type="transform", long=True) or []
            print("all objects")

        #verify if colors checkbox is checked, apply colors from the JSON file to the outliner
        if self.checkbox_colors.isChecked():
            print("colors checked")

        #same for reorder checkbox
        if self.checkbox_reorder.isChecked():
            print("reorder checked")









                

                
                

        






        #if self.checkbox_colors.isChecked():
        #    print("colors checked")
            

        
 
def main():
    
    global widget
    widget = MainWindow()
    widget.show()
 
main()