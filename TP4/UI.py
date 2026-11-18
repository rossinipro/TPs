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
        self.initial_height_spinbox, self.initial_height_slider = self.create_param(1, 100, 10)
        self.ball_weight_spinbox, self.ball_weight_slider = self.create_param(1, 10, 1)

        self.total_frame_spinbox, self.total_frame_slider = self.create_param(1, 1000, 24)

        self.squash_stretch = QCheckBox("Enable Squash and Stretch")
        self.squash_stretch.setChecked(False)

        # Generate button
        self.generate_btn = QPushButton("Generate Bouncy Ball")
        self.generate_btn.clicked.connect(lambda: animator.ball_animation(self))

        # -- Create Layout --
        layout = QVBoxLayout(self)

        settings_group = QGroupBox("Ball Properties")
        settings_layout = QFormLayout(settings_group)

        settings_layout.addRow("Initial Height", self.initial_height_spinbox)
        settings_layout.addRow("", self.initial_height_slider)

        settings_layout.addRow("Ball Weight", self.ball_weight_spinbox)
        settings_layout.addRow("", self.ball_weight_slider)

        # Animation settings
        animation_group = QGroupBox("Animation Settings")
        animation_layout = QFormLayout(animation_group)

        animation_layout.addRow("Total frames", self.total_frame_spinbox)
        animation_layout.addRow("", self.total_frame_slider)

        animation_layout.addRow(self.squash_stretch)

        # Add everything to main layout
        layout.addWidget(settings_group)
        layout.addWidget(animation_group)
        layout.addWidget(self.generate_btn)


    def create_param(self, rangemin, rangemax, default):

        spinbox = QSpinBox()
        spinbox.setRange(rangemin, rangemax)
        spinbox.setValue(default)

        slider = QSlider(Qt.Horizontal)
        slider.setRange(rangemin, rangemax)
        slider.setValue(default)

        # Synchronize slider and spinbox
        spinbox.valueChanged.connect(slider.setValue)
        slider.valueChanged.connect(spinbox.setValue)

        return spinbox, slider
