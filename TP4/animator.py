from PySide6.QtWidgets import QMessageBox
import maya.cmds as cmds
import random

import importlib
import UI
importlib.reload(UI)

def ball_animation(UI):

    ball = cmds.ls(selection=True, transforms=True)
    if not ball:
        QMessageBox.warning(UI, "Ball Animation", "Select an object first.")
        return
    source = ball[0]

    cmds.cutKey(ball, clear=True) #delete previous keyframes for selected objects
    cmds.play(forward=True)



    cmds.undoInfo(openChunk=True)
    try:
        # Get values from UI
        initial_height = UI.initial_height_spinbox.value()
        ball_weight = UI.ball_weight_spinbox.value()
        total_frames = UI.total_frame_spinbox.value()

        height = initial_height
        frame = 1


        # Initial height keyframe
        cmds.setKeyframe(ball, attribute="translateY",
        time=frame, value=height)

        print("yay!")

    finally:
        cmds.undoInfo(closeChunk=True) #close chunk for ctrl+z implementation