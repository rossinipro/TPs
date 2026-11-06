from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGroupBox, QHBoxLayout, QSpinBox

import animator
import importlib
importlib.reload(animator)


class MainWindow(QWidget): 
    def __init__(self): #constructeur
        super().__init__()  #constructeur Qwidget
        self.setWindowTitle("Ana Carolina Rossini - TP3 - Random Animation")
        self.create_ui()

    def create_parameter_group(self, name, default_min, default_max):

        # Create group
        group = QGroupBox(name)
        layout = QVBoxLayout()
        group.setLayout(layout)

        # Create Min and Max layouts
        min_layout = QHBoxLayout()
        max_layout = QHBoxLayout()

        layout.addLayout(min_layout)
        layout.addLayout(max_layout)

        # Store spinboxes
        parameters = {}

        # Create X, Y and Z spinboxes
        for axis in ["X", "Y", "Z"]:

            # Min
            min_label = QLabel("min " + axis + ":")
            min_layout.addWidget(min_label)

            min_spin = QSpinBox()
            min_spin.setRange(-1000, 1000)
            min_spin.setValue(default_min)
            min_layout.addWidget(min_spin)

            # Max
            max_label = QLabel("max " + axis + ":")
            max_layout.addWidget(max_label)

            max_spin = QSpinBox()
            max_spin.setRange(-1000, 1000)
            max_spin.setValue(default_max)
            max_layout.addWidget(max_spin)

            # Save spinboxes
            parameters["min_" + axis] = min_spin
            parameters["max_" + axis] = max_spin

        return group, parameters

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


        # --- Translate Parameters group ---
        self.translate_group, self.translate_parameters = self.create_parameter_group("Translate Parameters", -10, 10)
        layout.addWidget(self.translate_group)

        # --- Rotate Parameters group ---
        self.rotate_group, self.rotate_parameters = self.create_parameter_group("Rotate Parameters", -10, 10)
        layout.addWidget(self.rotate_group)

        # --- Scale Parameters group ---
        self.scale_group, self.scale_parameters = self.create_parameter_group("Scale Parameters", -10, 10)
        layout.addWidget(self.scale_group) 

        

        #Generate button
        self.button = QPushButton('Generate', self)        
        self.button.clicked.connect(self.button_onClicked)
        layout.addWidget(self.button)



    def button_onClicked(self):
        animator.random_animation(self)



