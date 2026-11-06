
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
        trans_min = [ui.translate_parameters["min_X"].value(), ui.translate_parameters["min_Y"].value(), ui.translate_parameters["min_Z"].value()]
        trans_max = [ui.translate_parameters["max_X"].value(), ui.translate_parameters["max_Y"].value(), ui.translate_parameters["max_Z"].value()]

        rotate_min = [ui.rotate_parameters["min_X"].value(), ui.rotate_parameters["min_Y"].value(), ui.rotate_parameters["min_Z"].value()]
        rotate_max = [ui.rotate_parameters["max_X"].value(), ui.rotate_parameters["max_Y"].value(), ui.rotate_parameters["max_Z"].value()]

        scale_min = [ui.scale_parameters["min_X"].value(), ui.scale_parameters["min_Y"].value(), ui.scale_parameters["min_Z"].value()]
        scale_max = [ui.scale_parameters["max_X"].value(), ui.scale_parameters["max_Y"].value(), ui.scale_parameters["max_Z"].value()]

        #create keyframes for each object in the selection using the random values generated.
        #take the steps between the min and max time to create keyframes at each step
        for t in range(min_time, max_time + 1, steps):
            for obj in objects:
                #make random between min and max
                trans_random = [random.uniform(trans_min[i], trans_max[i]) for i in range(3)] #for i in range (3) because we have 3 values for x, y and z
                rotate_random = [random.uniform(rotate_min[i], rotate_max[i]) for i in range(3)]
                scale_random = [random.uniform(scale_min[i], scale_max[i]) for i in range(3)]
                obj_name = obj.split("|")[-1] #get the name of the object without the path

                #get initial values of obj
                translatex_initial = cmds.getAttr(obj + ".translateX")
                translatey_initial = cmds.getAttr(obj + ".translateY")
                translatez_initial = cmds.getAttr(obj + ".translateZ")
                rotatex_initial = cmds.getAttr(obj + ".rotateX")
                rotatey_initial = cmds.getAttr(obj + ".rotateY")
                rotatez_initial = cmds.getAttr(obj + ".rotateZ")
                scalex_initial = cmds.getAttr(obj + ".scaleX")
                scaley_initial = cmds.getAttr(obj + ".scaleY")
                scalez_initial = cmds.getAttr(obj + ".scaleZ")

                #the first and last keyframes are set to the initial values of the objects, and the middle keyframe is set to the random values generated
                #set keyframe for translate/rotate/scale at min_time with initial value
                cmds.setKeyframe(obj, attribute="translateX", t=min_time, v=translatex_initial)
                cmds.setKeyframe(obj, attribute="translateY", t=min_time, v=translatey_initial)
                cmds.setKeyframe(obj, attribute="translateZ", t=min_time, v=translatez_initial)
                cmds.setKeyframe(obj, attribute="rotateX", t=min_time, v=rotatex_initial)
                cmds.setKeyframe(obj, attribute="rotateY", t=min_time, v=rotatey_initial)
                cmds.setKeyframe(obj, attribute="rotateZ", t=min_time, v=rotatez_initial)
                cmds.setKeyframe(obj, attribute="scaleX", t=min_time, v=scalex_initial)
                cmds.setKeyframe(obj, attribute="scaleY", t=min_time, v=scaley_initial)
                cmds.setKeyframe(obj, attribute="scaleZ", t=min_time, v=scalez_initial)

                #set keyframe for translate/rotate/scale at middle time with random value
                cmds.setKeyframe(obj, attribute="translateX", t=t, v=trans_random[0])
                cmds.setKeyframe(obj, attribute="translateY", t=t, v=trans_random[1])
                cmds.setKeyframe(obj, attribute="translateZ", t=t, v=trans_random[2])
                cmds.setKeyframe(obj, attribute="rotateX", t=t, v=rotate_random[0])
                cmds.setKeyframe(obj, attribute="rotateY", t=t, v=rotate_random[1])
                cmds.setKeyframe(obj, attribute="rotateZ", t=t, v=rotate_random[2])
                cmds.setKeyframe(obj, attribute="scaleX", t=t, v=scale_random[0])
                cmds.setKeyframe(obj, attribute="scaleY", t=t, v=scale_random[1])
                cmds.setKeyframe(obj, attribute="scaleZ", t=t, v=scale_random[2])

                #set keyframe for translate/rotate/scale at max_time with initial value
                cmds.setKeyframe(obj, attribute="translateX", t=max_time, v=translatex_initial)
                cmds.setKeyframe(obj, attribute="translateY", t=max_time, v=translatey_initial)
                cmds.setKeyframe(obj, attribute="translateZ", t=max_time, v=translatez_initial)
                cmds.setKeyframe(obj, attribute="rotateX", t=max_time, v=rotatex_initial)
                cmds.setKeyframe(obj, attribute="rotateY", t=max_time, v=rotatey_initial)
                cmds.setKeyframe(obj, attribute="rotateZ", t=max_time, v=rotatez_initial)
                cmds.setKeyframe(obj, attribute="scaleX", t=max_time, v=scalex_initial)
                cmds.setKeyframe(obj, attribute="scaleY", t=max_time, v=scaley_initial)
                cmds.setKeyframe(obj, attribute="scaleZ", t=max_time, v=scalez_initial) #set keyframe for scale at max_time with initial value


    finally: #try:finally: is used to ensure that the code inside the finally block is executed regardless of try block worked or not
        cmds.undoInfo(closeChunk=True) #close chunk for ctrl+z implementation