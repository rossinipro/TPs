
import maya.cmds as cmds
import random

import importlib
import ui
importlib.reload(ui)

def random_animation(ui):

    cmds.undoInfo(openChunk=True) #open chunk for ctrl+z implementation

    objects = cmds.ls(selection=True, type="transform", long=True) or [] #Take only selected objects

    try:
        cmds.cutKey(objects, clear=True) #delete previous keyframes for selected objects
        
        min_time = 1
        max_time = ui.frames_duration.value()
        steps = ui.frames_step.value()

        #control how long the animation will be played
        cmds.playbackOptions(edit=True, min=min_time, max=max_time)
        cmds.playbackOptions(edit=True, animationEndTime=max_time)


        #create vectors for min and max values of translate, rotate and scale parameters
        trans_min = [ui.trans_min_X.value(), ui.trans_min_Y.value(), ui.trans_min_Z.value()]
        trans_max = [ui.trans_max_X.value(), ui.trans_max_Y.value(), ui.trans_max_Z.value()]
    
        rotate_min = [ui.rotate_min_X.value(), ui.rotate_min_Y.value(), ui.rotate_min_Z.value()]
        rotate_max = [ui.rotate_max_X.value(), ui.rotate_max_Y.value(), ui.rotate_max_Z.value()]

        scale_min = [ui.scale_min_X.value(), ui.scale_min_Y.value(), ui.scale_min_Z.value()]
        scale_max = [ui.scale_max_X.value(), ui.scale_max_Y.value(), ui.scale_max_Z.value()]
        
        #Get initial values for each obj
        for obj in objects:
            translate_initial = [cmds.getAttr(obj + ".translateX"), cmds.getAttr(obj + ".translateY"), cmds.getAttr(obj + ".translateZ") ]
            rotate_initial = [cmds.getAttr(obj + ".rotateX"), cmds.getAttr(obj + ".rotateY"), cmds.getAttr(obj + ".rotateZ") ]
            scale_initial = [cmds.getAttr(obj + ".scaleX"), cmds.getAttr(obj + ".scaleY"), cmds.getAttr(obj + ".scaleZ") ]

            #set keyframe for translate/rotate/scale at min_time with initial value

            #create keyframes for each object in the selection using the random values generated.
            #take the steps between the min and max time to create keyframes at each step
            for t in range(min_time + steps, max_time, steps):
                #make random between min and max
                trans_random = [random.uniform(trans_min[i], trans_max[i]) for i in range(3)] #for i in range (3) because we have 3 values for x, y and z
                rotate_random = [random.uniform(rotate_min[i], rotate_max[i]) for i in range(3)]
                scale_random = [random.uniform(scale_min[i], scale_max[i]) for i in range(3)]

                for i, axis in enumerate(["X", "Y", "Z"]):
                    cmds.setKeyframe(obj, attribute="translate" + axis, t=min_time, v=translate_initial[i])
                    cmds.setKeyframe(obj, attribute="rotate" + axis, t=min_time, v=rotate_initial[i])
                    cmds.setKeyframe(obj, attribute="scale" + axis, t=min_time, v=scale_initial[i])

                #set keyframe for translate/rotate/scale at middle time with random value
                for i, axis in enumerate(["X", "Y", "Z"]):
                    cmds.setKeyframe(obj, attribute="translate" + axis, t=t, v=trans_random[i])
                    cmds.setKeyframe(obj, attribute="rotate" + axis, t=t, v=rotate_random[i])
                    cmds.setKeyframe(obj, attribute="scale" + axis, t=t, v=scale_random[i])

                #set keyframe for translate/rotate/scale at max_time with initial value
                for i, axis in enumerate(["X", "Y", "Z"]):
                    cmds.setKeyframe(obj, attribute="translate" + axis, t=max_time, v=translate_initial[i])
                    cmds.setKeyframe(obj, attribute="rotate" + axis, t=max_time, v=rotate_initial[i])
                    cmds.setKeyframe(obj, attribute="scale" + axis, t=max_time, v=scalex_initial[i])


    finally: #try:finally: is used to ensure that the code inside the finally block is executed regardless of try block worked or not
        cmds.undoInfo(closeChunk=True) #close chunk for ctrl+z implementation