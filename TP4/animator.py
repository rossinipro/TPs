from PySide6.QtWidgets import QMessageBox
import maya.cmds as cmds
import math

import importlib
import UI
importlib.reload(UI)

# set total animation time when ball stops
end_frame = 60


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


    cmds.undoInfo(openChunk=True)
    try: 
        # clear previous keys and reset the scale
        cmds.cutKey(ball, clear=True)
        for axis in ("X", "Y", "Z"):
            cmds.setAttr(ball[0] + ".scale" + axis, 1)
            cmds.setAttr(ball[0] + ".translate" + axis, 1)
        
        stop_frame = create_bounce(ball, initial_height, ball_weight, initial_speed, use_squash, use_translate)

        cmds.playbackOptions(minTime=1, maxTime=stop_frame,
            animationStartTime=1, animationEndTime=stop_frame)

    finally:
        cmds.undoInfo(closeChunk=True) #close chunk for ctrl+z implementation

    # play from frame 1
    cmds.currentTime(1)
    cmds.play(forward=True)

def create_bounce(ball, initial_height, ball_weight, initial_speed, use_squash, use_translate):

    # how much height is kept after each bounce
    #weight 1 keeps 85% of the height, weight 10 keeps only 22%
    height_after_bounce = 0.85 - (ball_weight - 1) * 0.07

    # how many frames the first fall takes.
    # speed 1 -> 13 frames (slow), speed 10 -> 4 frames (fast)
    half_time = 14 - initial_speed
    frame = 1

    squash_amount = 0.05  - ((ball_weight - 1)-(initial_height - 1)) * 0.05
    translate_x = 0

    # initial height keyframe
    if use_translate:
        key_movement(ball, frame, translate_x)
    key_peak(ball, frame, initial_height, use_squash)

    # first impact
    frame = frame + half_time
    key_impact(ball, frame, squash_amount, use_squash, half_time)

    peak = initial_height
    translate_x = initial_speed

    # bounce loop until bounce is too low or too short
    while True:
        peak = peak * height_after_bounce - .23 # make bounce lower
        half_time = half_time * height_after_bounce # make bounce shorter
        squash_amount = squash_amount * height_after_bounce
        steps_to_peak = int(round(half_time))

        

        if peak < .5 or steps_to_peak < 2:
            break

        key_peak(ball, frame + steps_to_peak, peak, use_squash)

        frame = frame + 2 * steps_to_peak

        key_impact(ball, frame, squash_amount, use_squash, steps_to_peak)

        stop_frame = max(frame + 2, end_frame)

    translate_x = translate_x + 10
    if use_translate:
        key_movement(ball, frame + 2, translate_x)
    return stop_frame



def key_y(ball, frame_value, height_value, intangent):
    cmds.setKeyframe(ball, attribute="translateY", time=frame_value, value=height_value,
                     inTangentType=intangent, outTangentType=intangent)


def key_peak(ball, frame, y, use_squash):
    key_y(ball, frame, y, "flat")
    if use_squash:
        key_scale(ball, frame, 1.0)


def key_scale(ball, frame, scale_y):
    cmds.setKeyframe(ball, attribute="scaleY", time=frame, value=scale_y,
                     inTangentType="flat", outTangentType="flat")
 
def key_movement(ball, frame, translate_x):
    cmds.setKeyframe(ball, attribute="translateX", time=frame, value=translate_x,
                    inTangentType="linear", outTangentType="linear")
 
def key_impact(ball, frame, squash_amount, use_squash, peak):
    key_y(ball, frame, 0, "linear")
 
    if use_squash:
        #if squash_amount > .1:

        offset = min(4, peak // 2) # // is used to floor the result. in this case, if peak / 2 returns a decimal, it will be rounded to the next case

        #if offset > .1:
        key_scale(ball, frame - offset, 1.0) # keep no bounce until it takes velocity

        key_scale(ball, frame - 1, 1 + max(squash_amount/2,0)) # stretch before
        key_scale(ball, frame, min(1 - squash_amount, 1))  # squash

        key_scale(ball, frame + 1,1 + max(squash_amount/2,0)) # stretch after
        if offset > 1 and frame + offset <= end_frame:
            key_scale(ball, frame + offset, 1.0) # returns to no bounce


