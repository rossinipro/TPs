from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QPushButton, QGroupBox, QSpinBox, QSlider, QCheckBox
from shiboken6 import wrapInstance #used to wrap tool in maya
import maya.OpenMayaUI as omui

import animator
import importlib
importlib.reload(animator)




# Get Maya main window
def maya_main_window():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window), QWidget)


class BounceBallAnimation(QWidget):

    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Bouncy Ball Generator")
        self.setMinimumWidth(300)
        self.create_ui()

    def create_ui(self):

        # -- Create Widgets --
        self.initial_height_spinbox, self.initial_height_slider = self.create_param(1, 10, 10)
        self.ball_weight_spinbox, self.ball_weight_slider = self.create_param(1, 10, 1)
        self.initial_speed_spinbox, self.initial_speed_slider = self.create_param(1, 10, 1)

        self.horizontal_movement_checkbox = QCheckBox("Add horizontal movement")
        self.horizontal_movement_checkbox.setChecked(False)
        self.horizontal_movement_checkbox.clicked.connect(lambda: animator.ball_animation(self))

        self.squash_stretch_checkbox = QCheckBox("Enable Squash and Stretch")
        self.squash_stretch_checkbox.setChecked(False)
        self.squash_stretch_checkbox.clicked.connect(lambda: animator.ball_animation(self))

        # Generate button
        self.generate_btn = QPushButton("Generate Bouncy Ball")
        self.generate_btn.clicked.connect(lambda: animator.ball_animation(self))

        # -- Create Layout --
        main_layout = QVBoxLayout(self)

        settings_group = QGroupBox("Ball Properties")
        settings_layout = QFormLayout(settings_group)

        settings_layout.addRow("Initial Height", self.initial_height_spinbox)
        settings_layout.addRow("", self.initial_height_slider)

        settings_layout.addRow("Ball Weight", self.ball_weight_spinbox)
        settings_layout.addRow("", self.ball_weight_slider)

        settings_layout.addRow("Initial Speed", self.initial_speed_spinbox)
        settings_layout.addRow("", self.initial_speed_slider)
        
        # Animation settings
        animation_group = QGroupBox("Animation Settings")
        animation_layout = QFormLayout(animation_group)

        animation_layout.addRow(self.horizontal_movement_checkbox)


        animation_layout.addRow(self.squash_stretch_checkbox)

        # Add everything to main layout
        main_layout.addWidget(settings_group)
        main_layout.addWidget(animation_group)
        main_layout.addWidget(self.generate_btn)


    def create_param(self, rangemin, rangemax, default):

        self.spinbox = QSpinBox()
        self.spinbox.setRange(rangemin, rangemax)
        self.spinbox.setValue(default)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(rangemin, rangemax)
        self.slider.setValue(default)

        # Synchronize slider and spinbox
        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.spinbox.valueChanged.connect(lambda: animator.ball_animation(self))
        self.slider.valueChanged.connect(self.spinbox.setValue)
        self.slider.valueChanged.connect(lambda: animator.ball_animation(self))

        return self.spinbox, self.slider
