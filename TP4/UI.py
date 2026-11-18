from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QPushButton, QGroupBox, QSpinBox, QSlider, QCheckBox
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui
from PySide6.QtCore import Qt

import animator
import importlib
importlib.reload(animator)


# Get Maya main window
def maya_main_window():
    maya_main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(maya_main_window), QWidget)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Bouncy Ball Generator")
        self.setMinimumWidth(300)
        self.create_ui()

    def create_ui(self):
        # -- Create Widgerts --
        self.bounce_height_spinbox, self.bounce_height_slider = self.create_param(1, 100, 10)
        self.gravity_spinbox, self.gravity_slider = self.create_param(1, 10, 1)
        self.energy_loss_spinbox, self.energy_loss_slider = self.create_param(0, 100, 20)

        self.total_frame_spinbox, self.total_frame_slider = self.create_param(1, 1000, 24)
        self.bounces_spinbox, self.bounces_slider = self.create_param(1, 20, 5)



        self.squash_stretch = QCheckBox("Enable Squash and Stretch")
        self.squash_stretch.setChecked(False)

        # Generate button
        self.generate_btn = QPushButton("Generate Bouncy Ball")
        self.generate_btn.clicked.connect( lambda: animator.ball_animation(self)) #live update


        # -- Create Layout --                   
        layout = QVBoxLayout(self)

        physics_group = QGroupBox("Physics Settings")
        physics_layout = QFormLayout(physics_group)

        physics_layout.addRow("Bounce height", self.bounce_height_spinbox)
        physics_layout.addRow("", self.bounce_height_slider)

        physics_layout.addRow("Gravity", self.gravity_spinbox)
        physics_layout.addRow("", self.gravity_slider)

        physics_layout.addRow("Energy loss", self.energy_loss_spinbox)
        physics_layout.addRow("", self.energy_loss_slider)


        # Animation settings
        animation_group = QGroupBox("Animation Settings")
        animation_layout = QFormLayout(animation_group)

        animation_layout.addRow("Total frames", self.total_frame_spinbox)
        animation_layout.addRow("", self.total_frame_slider)

        animation_layout.addRow("Number of bounces", self.bounces_spinbox)
        animation_layout.addRow("", self.bounces_slider)

        # Add everything to main layout
        layout.addWidget(physics_group)
        layout.addWidget(animation_group)
        layout.addWidget(self.generate_btn)


    def create_param(self, rangemin, rangemax, default):
        self.spinbox = QSpinBox()
        self.spinbox.setRange(rangemin, rangemax)
        self.spinbox.setValue(default)
        #self.spinbox.valueChanged.connect(self.update_values(factor)) #live update

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setRange(rangemin, rangemax)
        self.slider.setValue(default)

        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spinbox.setValue)

        return self.spinbox, self.slider

