from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QPushButton, QGroupBox, QSpinBox, QDoubleSpinBox, QCheckBox
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui
from PySide6.QtCore import Qt


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
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.bounce_height = QDoubleSpinBox()
        self.bounce_height.setRange(1, 100)
        self.bounce_height.setValue(10)

        self.gravity = QDoubleSpinBox()
        self.gravity.setRange(0.1, 30)
        self.gravity.setValue(9.8)

        self.energy_loss = QSpinBox()
        self.energy_loss.setRange(0, 100)
        self.energy_loss.setValue(20)
        self.energy_loss.setSuffix("%")

        # Animation settings
        self.start_frame = QSpinBox()
        self.start_frame.setRange(1, 10000)
        self.start_frame.setValue(1)

        self.bounces = QSpinBox()
        self.bounces.setRange(1, 20)
        self.bounces.setValue(5)

        self.squash_stretch = QCheckBox("Enable Squash & Stretch")
        self.squash_stretch.setChecked(False)

        # Generate button
        self.generate_btn = QPushButton("Generate Bouncy Ball")

    def create_layout(self):

        layout = QVBoxLayout(self)

        physics_group = QGroupBox("Physics Settings")
        physics_layout = QFormLayout(physics_group)

        physics_layout.addRow("Bounce Height:", self.bounce_height)
        physics_layout.addRow("Gravity:", self.gravity)
        physics_layout.addRow("Energy Loss:", self.energy_loss)

        # Animation settings
        animation_group = QGroupBox("Animation Settings")
        animation_layout = QFormLayout(animation_group)

        animation_layout.addRow("Start Frame:", self.start_frame)
        animation_layout.addRow("Number of Bounces:", self.bounces)
        animation_layout.addRow(self.squash_stretch)

        # Add everything to main layout
        layout.addWidget(physics_group)
        layout.addWidget(animation_group)
        layout.addWidget(self.generate_btn)