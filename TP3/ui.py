import maya.cmds as cmds
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGroupBox, QHBoxLayout, QSpinBox

import animator
import importlib
importlib.reload(animator)


class RandomAnimatorTool(QWidget): 
        def __init__(self): #constructeur
                super().__init__()  #constructeur Qwidget
                self.setWindowTitle("Ana Carolina Rossini - TP3 - Random Animation")
                self.create_ui()

        def create_ui(self):
                #create main layout
                main_layout = QVBoxLayout(self)
                
                # --- Animation Timing group ---
                timing_group = QGroupBox("Animation Timing") #timing group layout
                timing_layout = QHBoxLayout() #horizontal box inside of timing group layout
                timing_group.setLayout(timing_layout) #add horizontal box inside the group
                main_layout.addWidget(timing_group) #add group to main layout


                #label inside of horizontal box in the timing group layout
                self.create_label("Duration (Frames)", timing_layout)
                self.frames_duration = self.create_spinbox(timing_layout, 1, 1000, 100)

                self.create_label("Step (Frames)", timing_layout)
                self.frames_step = self.create_spinbox(timing_layout, 1, 1000, 10)


                # --- Translate Parameters group ---
                self.translate_layout_min, self.translate_layout_max = self.create_parameter_group("Translate Parameters", main_layout)

                # Min values
                self.create_label("min x:", self.translate_layout_min)
                self.trans_min_X = self.create_spinbox(self.translate_layout_min, -1000, 1000, -10)

                self.create_label("min y:", self.translate_layout_min)
                self.trans_min_y = self.create_spinbox(self.translate_layout_min, -1000, 1000, -10)

                self.create_label("min z:", self.translate_layout_min)
                self.trans_min_z = self.create_spinbox(self.translate_layout_min, -1000, 1000, -10)

                # Max values
                self.create_label("max x:", self.translate_layout_max)
                self.trans_max_X = self.create_spinbox(self.translate_layout_max, -1000, 1000, 10)

                self.create_label("max y:", self.translate_layout_max)
                self.trans_max_y = self.create_spinbox(self.translate_layout_max, -1000, 1000, 10)

                self.create_label("max z:", self.translate_layout_max)
                self.trans_max_z = self.create_spinbox(self.translate_layout_max, -1000, 1000, 10)




                # --- Rotate Parameters group ---
                self.rotate_layout_min, self.rotate_layout_max = self.create_parameter_group("Rotate Parameters", main_layout)

                # Min values
                self.create_label("min x:", self.rotate_layout_min)
                self.rotate_min_X = self.create_spinbox(self.rotate_layout_min, -1000, 1000, -10)

                self.create_label("min y:", self.rotate_layout_min)
                self.rotate_min_y = self.create_spinbox(self.rotate_layout_min, -1000, 1000, -10)

                self.create_label("min z:", self.rotate_layout_min)
                self.rotate_min_z = self.create_spinbox(self.rotate_layout_min, -1000, 1000, -10)

                # Max values
                self.create_label("max x:", self.rotate_layout_max)
                self.rotate_max_X = self.create_spinbox(self.rotate_layout_max, -1000, 1000, 10)

                self.create_label("max y:", self.rotate_layout_max)
                self.rotate_max_y = self.create_spinbox(self.rotate_layout_max, -1000, 1000, 10)

                self.create_label("max z:", self.rotate_layout_max)
                self.rotate_max_z = self.create_spinbox(self.rotate_layout_max, -1000, 1000, 10)

                # --- Scale Parameters group ---
                self.scale_layout_min, self.scale_layout_max = self.create_parameter_group("Scale Parameters", main_layout)

                # Min values
                self.create_label("min x:", self.scale_layout_min)
                self.scale_min_X = self.create_spinbox(self.scale_layout_min, -1000, 1000, -10)

                self.create_label("min y:", self.scale_layout_min)
                self.scale_min_y = self.create_spinbox(self.scale_layout_min, -1000, 1000, -10)

                self.create_label("min z:", self.scale_layout_min)
                self.scale_min_z = self.create_spinbox(self.scale_layout_min, -1000, 1000, -10)

                # Max values
                self.create_label("max x:", self.scale_layout_max)
                self.scale_max_X = self.create_spinbox(self.scale_layout_max, -1000, 1000, 10)

                self.create_label("max y:", self.scale_layout_max)
                self.scale_max_y = self.create_spinbox(self.scale_layout_max, -1000, 1000, 10)

                self.create_label("max z:", self.scale_layout_max)
                self.scale_max_z = self.create_spinbox(self.scale_layout_max, -1000, 1000, 10)

                #Generate button
                self.button = QPushButton('Generate', self)        
                self.button.clicked.connect(self.button_clicked)
                main_layout.addWidget(self.button)

        def create_label(self, text, layout):
                self.label = QLabel(text)
                layout.addWidget(self.label)
                return self.label

        def create_spinbox(self, layout, min_value, max_value, default_value):
                self.spinbox = QSpinBox()
                self.spinbox.setRange(min_value, max_value)
                self.spinbox.setValue(default_value)
                layout.addWidget(self.spinbox)
                return self.spinbox

        def create_parameter_group(self, title, main_layout):
                self.group = QGroupBox(title)
                self.layout = QVBoxLayout()
                self.group.setLayout(self.layout)

                layout_min = QHBoxLayout()
                layout_max = QHBoxLayout()

                self.layout.addLayout(layout_min)
                self.layout.addLayout(layout_max)
                main_layout.addWidget(self.group)

                return layout_min, layout_max

        def button_clicked(self):
                animator.random_animation(self)
