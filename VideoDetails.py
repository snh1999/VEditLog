from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QLabel
import sys
from Helper.Factory import Factory
from Helper.Utils import Utils

essential_default = 1
effect_default = 0
time_default = 0

class VideoDetails(QWidget):
    def __init__(self, length):
        super().__init__()
        
        self.source_path = ""
        self.clip_length = 0
        self.project_length = length
        
        
        self.setWindowTitle("Details")
        
        layout = QVBoxLayout(self)
        row1_layout = QHBoxLayout()
        row2_layout = QHBoxLayout()
        row3_layout = QHBoxLayout()
        row4_layout = QHBoxLayout()
        
        self.source_path_label = Factory.get_label_as_buttonview("Source Path:")
        self.add_button = QPushButton("Add")
        Utils.adjust_component_height(self.add_button)
        self.add_button.setDisabled(True)
        self.quality_input = Factory.get_combo_box(option_array= ['default quality', '144p', '240p', '360p', '480p', '720p', '1080p'])
        self.serial_input = Factory.get_combo_box(option_array= ['Append', 'Prepend'] + [str(i) for i in range(1, self.project_length + 1)])
        self.volume_spinbox = Factory.get_spinbox(val = essential_default, prefix="Volume")
        self.speed_spinbox = Factory.get_spinbox(val = essential_default, prefix= "Speed", suffix="x")
        self.rotate_spinbox = Factory.get_spinbox(val = effect_default, step= 0.1, range_low=-180, range_up=180, prefix="Rotate", suffix="degree")
        self.fadein_spinbox = Factory.get_spinbox(val = effect_default, prefix="Fade In", suffix="s")
        self.fadeout_spinbox = Factory.get_spinbox(val = effect_default, prefix="Fade Out", suffix="s")
        
        self.trim_start_button = QPushButton("Pick Start!", self)
        Utils.adjust_component_height(self.trim_start_button)
        self.trim_end_button = QPushButton("Pick End!", self)
        Utils.adjust_component_height(self.trim_end_button)
        
        self.reverse_button = QPushButton("Normal", self)
        Utils.adjust_component_height(self.reverse_button)
        self.reverse_button.clicked.connect(self.reverse_button_click)
        
        self.reset_button = QPushButton("Reset")
        Utils.adjust_component_height(self.reset_button)
        self.reset_button.clicked.connect(self.reset_button_click)
        
        
        
        row1_layout.addWidget(self.source_path_label)
        row1_layout.addWidget(self.add_button)
        row2_layout.addWidget(self.serial_input)
        row2_layout.addWidget(self.trim_start_button)
        row2_layout.addWidget(self.trim_end_button)
        row2_layout.addWidget(self.quality_input)
        row3_layout.addWidget(self.volume_spinbox)
        row3_layout.addWidget(self.speed_spinbox)
        row3_layout.addWidget(self.reverse_button)
        row4_layout.addWidget(self.rotate_spinbox)
        row4_layout.addWidget(self.fadein_spinbox)
        row4_layout.addWidget(self.fadeout_spinbox)
        row4_layout.addWidget(self.reset_button)
        
        layout.addLayout(row1_layout)
        layout.addLayout(row2_layout)
        layout.addLayout(row3_layout)
        layout.addLayout(row4_layout)

        
    
        
    def reverse_button_click(self):
        if self.reverse_button.text() == "Normal":
            self.reverse_button.setText("Reverse Clip")
        else:
            self.reverse_button.setText("Normal")
            
    def set_source(self, source_path, clip_length):
        self.source_path = source_path
        self.clip_length = clip_length
        self.fadein_spinbox.setRange(0, clip_length/1000/60)
        self.fadeout_spinbox.setRange(0, clip_length/1000/60)
        self.source_path_label.setText("Source Path: " + source_path)
    
    def set_button_click(self, volume = essential_default, speed = essential_default, 
                           rotate = effect_default, fadein = time_default, fadeout = time_default,
                           trim_start = time_default, trim_end = time_default,
                           reverse = False):
        self.volume_spinbox.setValue(volume)
        self.speed_spinbox.setValue(speed)
        self.rotate_spinbox.setValue(rotate)
        self.fadein_spinbox.setValue(fadein)
        self.fadeout_spinbox.setValue(fadeout)
        if trim_start != time_default and self.clip_length != 0 and self.clip_length > trim_start:
            self.trim_start_button.setText("Start: " + trim_start)
        if trim_start != time_default and self.clip_length != 0 and self.clip_length > trim_end:
            self.trim_end_button.setText("End: " + trim_end)
        
        
    
    def reset_button_click(self):
        self.set_button_click()
        self.trim_start_button.setText("Pick Start!")
        self.trim_end_button.setText("Pick End!")
        
    def set_add_update_button_text(self, text):
        self.add_button.setText(text)
        self.add_button.setEnabled(True)
        
    def get_all_details(self):
        return [self.serial_input.currentText(),
                self.source_path,
                self.get_trim_time(self.trim_start_button.text()),
                self.get_trim_time(self.trim_end_button.text()),
                self.quality_input.currentText(),
                self.volume_spinbox.value(),
                self.speed_spinbox.value(),
                self.reverse_button.text(),
                self.rotate_spinbox.value(),
                self.fadein_spinbox.value(),
                self.fadeout_spinbox.value()]
    
    def get_trim_time(self, text):
        if text.startswith("Pick"):
            return 0
        else:
            return int(text.split(":")[1])

    
    

# app = QApplication(sys.argv)
# widget = VideoDetails(1)
# widget.show()
# app.exec()