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



        #open "chunk": records all actions so everything is undone with one CTRL+Z
        cmds.undoInfo(openChunk=True)

        try:
            #variable that stores all objects in scene
            objects = cmds.ls(type="transform", long=True) or []
            
            #verify if the selection checkbox is checked, get the selected objects
            if self.checkbox_selection.isChecked():
                objects = cmds.ls(selection=True, type="transform", long=True) or []
                print("selected only")
            else:
                print("all objects")

            #verify if colors checkbox is checked, apply colors from the JSON file to the outliner
            if self.checkbox_colors.isChecked():
                print("colors checked")

                for obj in objects:
                    obj_name = obj.split("|")[-1]

                    for key, value in json_data.items():
                        if obj_name.startswith(key):
                            cmds.setAttr(obj + ".useOutlinerColor", 1) #enable outliner
                            cmds.setAttr(obj + ".outlinerColor", value[0], value[1], value[2], type="double3") #set RGB from json
                            print(f"Applied color {value} to {obj}")
                        
            #same for reorder checkbox
            if self.checkbox_reorder.isChecked():
                print("reorder checked")
                
                #lambda is a single line function. in this case, it splits the object name by "|" and takes the last part (the actual name) 
                # and decreases it to sort the objects in ascending order based on their names. 
                # "sort" only works in python code
                objects.sort(key=lambda x: x.split("|")[-1]) 

                #rearrange objects in the outliner based on the sorted order
                for i in objects:
                    cmds.reorder(i, front= True) #reorder to front



                

                

        finally:
            cmds.undoInfo(closeChunk=True) #close chunk actions


def main():
    
    global widget
    widget = MainWindow()
    widget.show()
 
main()