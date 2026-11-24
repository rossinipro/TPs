import os
import sys
sys.path.append( os.path.dirname(os.path.abspath(__file__)))

import importlib
import UI
importlib.reload(UI)


def main():
    
    global widget
    widget = UI.BounceBallAnimation()
    widget.show()
 
main()