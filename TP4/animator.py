from PySide6.QtWidgets import QMessageBox
import maya.cmds as cmds
import random

import importlib
import UI
importlib.reload(UI)

def ball_animation(UI):

    #set total animation time
    end_frame = 60
    cmds.playbackOptions(minTime=1, maxTime=end_frame,
                    animationStartTime=1, animationEndTime=end_frame)

    selected = cmds.ls(selection=True, transforms=True)
    if not selected:
        QMessageBox.warning(UI, "Ball Animation", "Select an object first.")
        return
    
    # Get values from UI
    initial_height = UI.initial_height_spinbox.value()
    ball_weight = UI.ball_weight_spinbox.value()
    initial_speed = UI.initial_speed_spinbox.value()
    use_horizontal_movement = UI.horizontal_movement_checkbox.isChecked()
    use_strech_squash = UI.squash_stretch_checkbox.isChecked()


    cmds.cutKey(selected, clear=True) #delete previous keyframes for selected objects
    cmds.play(forward=True)


    cmds.undoInfo(openChunk=True)
    try:
        keys = make_keys()

        if use_horizontal_movement:
            set_translate_keys()

        if use_strech_squash:
              set_strech_squash_keys()


    finally:
        cmds.undoInfo(closeChunk=True) #close chunk for ctrl+z implementation

    def make_keys():
        height = initial_height
        frame = 1


        # Initial height keyframe
        cmds.setKeyframe(selected, attribute="translateY", time=frame, value=height)


    def set_translate_keys():
        print ("horizontal checked")
        
    def set_strech_squash_keys():
        print ("stretch checked")