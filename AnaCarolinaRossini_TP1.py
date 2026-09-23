import sys
import json
import os

from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QToolBar, QMainWindow, QInputDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

json_path = sys.argv[1] # read file as param 
# the file path needed to be hard-coded on launch.json. This variable takes the first argument as a param.

try:
    file = open(json_path, encoding="UTF-8") #open file as-is, have info such as size. encoding UTF-8 allows accents and special characters
    data = json.load(file) #interpret then load file into readeable data
except:
    print("Error: Could not open file:", json_path)
    

# Get the column names from the keys
categories = list(data[0].keys())

number_of_columns = len(categories) #set number of columns by the amount of keys
number_of_rows = len(data) #set number of rows by how many data blocks there are


app = QApplication(sys.argv) #necessary to create the app
window = QMainWindow() 
table = QTableWidget() 
window.setCentralWidget(table) 

# Set the number of rows and columns and name the columns
table.setColumnCount(number_of_columns)
table.setRowCount(number_of_rows)
table.setHorizontalHeaderLabels(categories)

#for each row and column, get the value from the data corresponding to its order on the data list and the key list, then set it in the table
for row in range(number_of_rows):

    for column in range(number_of_columns):

        value = data[row][categories[column]]

        table.setItem(
            row,
            column,
            QTableWidgetItem(str(value))
        )



# sort when clicking on the columns
table.setSortingEnabled(True)

#create function to search a term in the table
def search():
     
     text, ok = QInputDialog.getText(
        window, 
        "Search", 
        "Search:")
        
     if ok:
     
        for row in range(number_of_rows): #start found as false and check each row and column for the term
            search_found = False
            search_term = table.findItems(text, Qt.MatchFlag.MatchContains) #"MatchContains" is a PySide command that automatically do search and match

            #since Pyside already did the search, it's only necessary to highlight if its true and hide if its false
            for item in search_term: 
                    if item.row() == row:
                        search_found = True
                        item.setBackground(Qt.yellow)
                        table.setRowHidden(row, False)

            if search_found == False:
                    table.setRowHidden(row, True)

def show_file_info():
    file_name = os.path.basename(json_path)
    file_size = os.path.getsize(json_path)
    number_of_elements = len(data)
    
    QMessageBox.information(window, "File Information", ( 
         f"File name: {file_name}\n"
         f"File size: {file_size}\n"
         f"Number of elements: {number_of_elements}\n"
    ))


toolbar = QToolBar()
window.addToolBar(toolbar) #add toolbar to window

#create a search button on the toolbar
search_button = QAction("Search", window) 
toolbar.addAction(search_button)
search_button.triggered.connect(search) #call 'search'

#create info button on toolbar
info_button = QAction("File Information", window) 
toolbar.addAction(info_button)
info_button.triggered.connect(show_file_info) #call'show_file_info'


window.setWindowTitle("Ana Carolina Rossini - TP1")

#change size then show window
window.resize(800,400)
window.show()
sys.exit(app.exec())