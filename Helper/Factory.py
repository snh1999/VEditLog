from PySide6.QtWidgets import (QApplication, 
                               QPushButton, 
                               QDialog, 
                               QFileDialog, 
                               QMainWindow, 
                               QSlider, 
                               QStyle, 
                               QLabel, 
                               QLineEdit, 
                               QToolBar, 
                               QWidget, 
                               QSizePolicy, 
                               QHBoxLayout, 
                               QVBoxLayout, 
                               QDoubleSpinBox,
                               QComboBox)
from PySide6.QtGui import QCursor, QFont
from PySide6.QtCore import Qt
import os, shutil, json

class Factory:
    @staticmethod
    def get_spinbox(val, step = 0.01, range_low = 0, range_up = 999999, prefix= "", suffix=""):
        spinbox = QDoubleSpinBox()
        
        if prefix:
            spinbox.setPrefix(prefix+": ")
        spinbox.setValue(val)
        spinbox.setRange(range_low, range_up)  
        spinbox.setDecimals(2)
        spinbox.setSingleStep(step)
        if suffix:
            spinbox.setSuffix(" "+ suffix)
        spinbox.setButtonSymbols(QDoubleSpinBox.PlusMinus) 
        
        return spinbox
    
    @staticmethod
    def get_combo_box(option_array):
        combo_box = QComboBox()
        combo_box.addItems(option_array)
        return combo_box
    
    @staticmethod
    def get_label_as_buttonview(label_text):
        label = QLabel(label_text)
        label.setStyleSheet('''
            border-style: solid;
            border-color: #111;
            border-width: 1px;
            border-radius: 4px;
            padding: 4px;
            min-width: 64px;
            min-height: 25px;
        ''')
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Set size policy
        return label