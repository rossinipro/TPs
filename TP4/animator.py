from PySide6.QtWidgets import QMessageBox
import maya.cmds as cmds
import random

import importlib
import UI
importlib.reload(UI)

def ball_animation(UI):

    # set total animation time
    end_frame = 60
    cmds.playbackOptions(minTime=1, maxTime=end_frame,
                    animationStartTime=1, animationEndTime=end_frame)

    # get tselected, return error if nothing is selected
    selected = cmds.ls(selection=True, transforms=True)
    if not selected:
        QMessageBox.warning(UI, "Ball Animation", "Select a polySphere first.")
        return
    
    # get values from UI
    initial_height = UI.initial_height_spinbox.value()
    ball_weight = UI.ball_weight_spinbox.value()
    initial_speed = UI.initial_speed_spinbox.value()
    use_horizontal_movement = UI.horizontal_movement_checkbox.isChecked()
    use_strech_squash = UI.squash_stretch_checkbox.isChecked()

    # delete previous keyframes
    cmds.cutKey(selected, clear=True) 

    cmds.undoInfo(openChunk=True)
    try:
        keys = make_keys(initial_height, ball_weight, initial_speed)

        if use_horizontal_movement:
            set_translate_keys(selected, keys)

        if use_strech_squash:
              set_strech_squash_keys(selected, keys)

    finally:
        cmds.undoInfo(closeChunk=True) #close chunk for ctrl+z implementation

    # play from frame 1
    cmds.play(forward=True)

    def make_keys(height, weight, speed):
        """ I want a list of frame time, height, kind, strength for the important keys.
        kind = "start", "peak", "impact", "end"
        strength = 0.1, how hard the ball hits the floor (used for squash)
        """

        # how much height is kept after each bounce
        #weight 1 keeps 85% of the height, weight 10 keeps only 22%
        keep = 0.85 - (weight - 1) * 0.07
    
        # how many frames the first fall takes.
        # speed 1 -> 13 frames (slow), speed 10 -> 4 frames (fast)
        half_time = 14 - speed
        frame = 1
        peak = height - keep

        # initial height keyframe
        cmds.setKeyframe(selected, attribute="translateY", time=frame, value=height)


    def set_translate_keys(selected, keys):
        print ("horizontal checked")
        
    def set_strech_squash_keys(selected, keys):
        print ("stretch checked")