from PySide6.QtWidgets import QMessageBox
import maya.cmds as cmds
import random

import importlib
import UI
importlib.reload(UI)

# set total animation time
end_frame = 60
cmds.playbackOptions(minTime=1, maxTime=end_frame,
                animationStartTime=1, animationEndTime=end_frame)

def ball_animation(UI):

    # get tselected, return error if nothing is selected
    ball = cmds.ls(selection=True, transforms=True)
    if not ball:
        QMessageBox.warning(UI, "Ball Animation", "Select a polySphere first.")
        return
    
    # get values from UI
    initial_height = UI.initial_height_spinbox.value()
    ball_weight = UI.ball_weight_spinbox.value()
    initial_speed = UI.initial_speed_spinbox.value()
    use_translate = UI.horizontal_movement_checkbox.isChecked()
    use_squash = UI.squash_stretch_checkbox.isChecked()

    # delete previous keyframes
    cmds.cutKey(ball, clear=True) 

    cmds.undoInfo(openChunk=True)
    try:
        create_bounce(ball, initial_height, ball_weight, initial_speed, use_squash, use_translate)

    finally:
        cmds.undoInfo(closeChunk=True) #close chunk for ctrl+z implementation

    # play from frame 1
    cmds.play(forward=True)

def create_bounce(ball, initial_height, ball_weight, initial_speed, use_squash, use_translate):

    # how much height is kept after each bounce
    #weight 1 keeps 85% of the height, weight 10 keeps only 22%
    height_after_bounce = 0.85 - (ball_weight - 1) * 0.07

    # how many frames the first fall takes.
    # speed 1 -> 13 frames (slow), speed 10 -> 4 frames (fast)
    impact_frame = 14
    frame = 1
    

    # initial height keyframe
    key_y(ball, frame, initial_height)

    # first impact
    frame = impact_frame
    key_y(ball, frame, 1)

    #bounce
    peak = initial_height * height_after_bounce # make bounce lower
    impact_frame = frame + (impact_frame * height_after_bounce) # make bounce shorter
    key_y(ball, impact_frame, peak)

    if frame <= end_frame:
        key_y(ball, end_frame, 1)

def key_y(ball, frame_value, height_value):
    cmds.setKeyframe(ball, attribute="translateY", time=frame_value, value=height_value,
                     inTangentType="spline", outTangentType="spline")
 
