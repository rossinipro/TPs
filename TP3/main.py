import os
import sys
sys.path.append( os.path.dirname(os.path.abspath(__file__)))

import importlib
import ui
importlib.reload(ui)




def main():
    
    global widget
    widget = ui.MainWindow()
    widget.show()
 
main()