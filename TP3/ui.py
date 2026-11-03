from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGroupBox, QHBoxLayout, QSpinBox

import animator
import importlib
importlib.reload(animator)


class MainWindow(QWidget): 
    def __init__(self): #constructeur
        super().__init__()  #constructeur Qwidget
        self.setWindowTitle("Ana Carolina Rossini - TP3 - Random Animation")
        self.create_ui()

    def create_ui(self):
        #create main layout
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # --- Animation Timing group ---
        timing_group = QGroupBox("Animation Timing") #timing group layout
        timing_layout = QHBoxLayout() #horizontal box inside of timing group layout
        timing_group.setLayout(timing_layout) #add horizontal box inside the group
        layout.addWidget(timing_group) #add group to main layout


        #label inside of horizontal box in the timing group layout
        label_frames_duration = QLabel("Duration (Frames)")
        timing_layout.addWidget(label_frames_duration)
        self.frames_duration = QSpinBox()
        self.frames_duration.setRange(1, 1000)
        self.frames_duration.setValue(100)
        timing_layout.addWidget(self.frames_duration)

        label_frames_step = QLabel("Step (Frames)")
        timing_layout.addWidget(label_frames_step)
        self.frames_step = QSpinBox()
        self.frames_step.setRange(1, 1000)
        self.frames_step.setValue(10)
        timing_layout.addWidget(self.frames_step)

        """

        # --- Translate Parameters group ---
        translate_group = QGroupBox("Translate Parameters") 
        translate_layout = QVBoxLayout()  # create a vertical box
        translate_group.setLayout(translate_layout) # add vbox into the group
        self.translate_layout_min = QHBoxLayout()
        self.translate_layout_max = QHBoxLayout()
        translate_layout.addLayout(self.translate_layout_min) #add both hbox into the vbox
        translate_layout.addLayout(self.translate_layout_max)
        layout.addWidget(translate_group)

        label_trans_min_X = QLabel("min x: ")
        self.translate_layout_min.addWidget(label_trans_min_X)
        self.trans_min_X = QSpinBox()
        self.trans_min_X.setRange(-1000, 1000)
        self.trans_min_X.setValue(-10)
        self.translate_layout_min.addWidget(self.trans_min_X)

        label_trans_min_y = QLabel("min y: ")
        self.translate_layout_min.addWidget(label_trans_min_y)
        self.trans_min_y = QSpinBox()
        self.trans_min_y.setRange(-1000, 1000)
        self.trans_min_y.setValue(-10)
        self.translate_layout_min.addWidget(self.trans_min_y)

        label_trans_min_z = QLabel("min z: ")
        self.translate_layout_min.addWidget(label_trans_min_z)
        self.trans_min_z = QSpinBox()
        self.trans_min_z.setRange(-1000, 1000)
        self.trans_min_z.setValue(-10)
        self.translate_layout_min.addWidget(self.trans_min_z)

        label_trans_max_X = QLabel("max x: ")
        self.translate_layout_max.addWidget(label_trans_max_X)
        self.trans_max_X = QSpinBox()
        self.trans_max_X.setRange(-1000, 1000)
        self.trans_max_X.setValue(10)
        self.translate_layout_max.addWidget(self.trans_max_X)

        label_trans_max_y = QLabel("max y: ")
        self.translate_layout_max.addWidget(label_trans_max_y)
        self.trans_max_y = QSpinBox()
        self.trans_max_y.setRange(-1000, 1000)
        self.trans_max_y.setValue(10)
        self.translate_layout_max.addWidget(self.trans_max_y)

        label_trans_max_z = QLabel("max z: ")
        self.translate_layout_max.addWidget(label_trans_max_z)
        self.trans_max_z = QSpinBox()
        self.trans_max_z.setRange(-1000, 1000)
        self.trans_max_z.setValue(10)
        self.translate_layout_max.addWidget(self.trans_max_z)




        # --- Rotate Parameters group ---
        rotate_group = QGroupBox("Rotate Parameters")
        rotate_layout = QVBoxLayout()
        rotate_group.setLayout(rotate_layout)
        self.rotate_layout_min = QHBoxLayout()
        self.rotate_layout_max = QHBoxLayout()
        rotate_layout.addLayout(self.rotate_layout_min)
        rotate_layout.addLayout(self.rotate_layout_max)
        layout.addWidget(rotate_group)

        label_rotate_min_X = QLabel("min x: ")
        self.rotate_layout_min.addWidget(label_rotate_min_X)
        self.rotate_min_X = QSpinBox()
        self.rotate_min_X.setRange(-1000, 1000)
        self.rotate_min_X.setValue(-10)
        self.rotate_layout_min.addWidget(self.rotate_min_X)

        label_rotate_min_y = QLabel("min y: ")
        self.rotate_layout_min.addWidget(label_rotate_min_y)
        self.rotate_min_y = QSpinBox()
        self.rotate_min_y.setRange(-1000, 1000)
        self.rotate_min_y.setValue(-10)
        self.rotate_layout_min.addWidget(self.rotate_min_y)

        label_rotate_min_z = QLabel("min z: ")
        self.rotate_layout_min.addWidget(label_rotate_min_z)
        self.rotate_min_z = QSpinBox()
        self.rotate_min_z.setRange(-1000, 1000)
        self.rotate_min_z.setValue(-10)
        self.rotate_layout_min.addWidget(self.rotate_min_z)

        label_rotate_max_X = QLabel("max x: ")
        self.rotate_layout_max.addWidget(label_rotate_max_X)
        self.rotate_max_X = QSpinBox()
        self.rotate_max_X.setRange(-1000, 1000)
        self.rotate_max_X.setValue(10)
        self.rotate_layout_max.addWidget(self.rotate_max_X)

        label_rotate_max_y = QLabel("max y: ")
        self.rotate_layout_max.addWidget(label_rotate_max_y)
        self.rotate_max_y = QSpinBox()
        self.rotate_max_y.setRange(-1000, 1000)
        self.rotate_max_y.setValue(10)
        self.rotate_layout_max.addWidget(self.rotate_max_y)

        label_rotate_max_z = QLabel("max z: ")
        self.rotate_layout_max.addWidget(label_rotate_max_z)
        self.rotate_max_z = QSpinBox()
        self.rotate_max_z.setRange(-1000, 1000)
        self.rotate_max_z.setValue(10)
        self.rotate_layout_max.addWidget(self.rotate_max_z)

        # --- Scale Parameters group ---
        scale_group = QGroupBox("Scale Parameters")
        scale_layout = QVBoxLayout()
        scale_group.setLayout(scale_layout)
        self.scale_layout_min = QHBoxLayout()
        self.scale_layout_max = QHBoxLayout()
        scale_layout.addLayout(self.scale_layout_min)
        scale_layout.addLayout(self.scale_layout_max)
        layout.addWidget(scale_group)

        label_scale_min_X = QLabel("min x: ")
        self.scale_layout_min.addWidget(label_scale_min_X)
        self.scale_min_X = QSpinBox()
        self.scale_min_X.setRange(-1000, 1000)
        self.scale_min_X.setValue(-10)
        self.scale_layout_min.addWidget(self.scale_min_X)

        label_scale_min_y = QLabel("min y: ")
        self.scale_layout_min.addWidget(label_scale_min_y)
        self.scale_min_y = QSpinBox()
        self.scale_min_y.setRange(-1000, 1000)
        self.scale_min_y.setValue(-10)
        self.scale_layout_min.addWidget(self.scale_min_y)

        label_scale_min_z = QLabel("min z: ")
        self.scale_layout_min.addWidget(label_scale_min_z)
        self.scale_min_z = QSpinBox()
        self.scale_min_z.setRange(-1000, 1000)
        self.scale_min_z.setValue(-10)
        self.scale_layout_min.addWidget(self.scale_min_z)

        label_scale_max_X = QLabel("max x: ")
        self.scale_layout_max.addWidget(label_scale_max_X)
        self.scale_max_X = QSpinBox()
        self.scale_max_X.setRange(-1000, 1000)
        self.scale_max_X.setValue(10)
        self.scale_layout_max.addWidget(self.scale_max_X)

        label_scale_max_y = QLabel("max y: ")
        self.scale_layout_max.addWidget(label_scale_max_y)
        self.scale_max_y = QSpinBox()
        self.scale_max_y.setRange(-1000, 1000)
        self.scale_max_y.setValue(10)
        self.scale_layout_max.addWidget(self.scale_max_y)

        label_scale_max_z = QLabel("max z: ")
        self.scale_layout_max.addWidget(label_scale_max_z)
        self.scale_max_z = QSpinBox()
        self.scale_max_z.setRange(-1000, 1000)
        self.scale_max_z.setValue(10)
        self.scale_layout_max.addWidget(self.scale_max_z)

        """

        # --- Translate Parameters group ---
        translate_group = self.create_parameters_group("Translate Parameters", -10, 10)

        

        #Generate button
        self.button = QPushButton('Generate', self)        
        self.button.clicked.connect(self.button_onClicked)
        layout.addWidget(self.button)

    def create_parameters_group(self, title, min_values, max_values):
        group = QGroupBox(title)
        layout = QVBoxLayout()
        group.setLayout(layout)

        min_layout = QHBoxLayout()
        max_layout = QHBoxLayout()
        layout.addLayout(min_layout)
        layout.addLayout(max_layout)

        for axis in ['x', 'y', 'z']:
        label_min = QLabel(f"min {axis}: ")
        min_layout.addWidget(label_min)
        spinbox_min = QSpinBox()
        spinbox_min.setRange(-1000, 1000)
        spinbox_min.setValue(min_values[axis])
        min_layout.addWidget(spinbox_min)

        label_max = QLabel(f"max {axis}: ")
        max_layout.addWidget(label_max)
        spinbox_max = QSpinBox()
        spinbox_max.setRange(-1000, 1000)
        spinbox_max.setValue(max_values[axis])
        max_layout.addWidget(spinbox_max)

        return group

    def button_onClicked(self):
        animator.random_animation(self)



