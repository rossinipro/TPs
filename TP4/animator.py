from PySide6.QtWidgets import QMessageBox
import maya.cmds as cmds
import random

import importlib
import UI
importlib.reload(UI)

def ball_animation(UI):
    #cmds.undo() #undo anything that was done before making it again
    selection = cmds.ls(selection=True, transforms=True)
    if not selection:
        QMessageBox.warning(UI, "Scatter", "Select an object first.")
        return
    source = selection[0]

    cmds.undoInfo(openChunk=True)
    try:
        print("yay!")

    finally:
        cmds.undoInfo(closeChunk=True) #close chunk for ctrl+z implementation