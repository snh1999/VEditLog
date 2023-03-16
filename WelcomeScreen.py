import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot, QTimer
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication,QPushButton, QDialog, QFileDialog, QMainWindow, QSlider, QStyle, QLabel, QMessageBox, QLineEdit, QToolBar, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtMultimedia import QAudioOutput, QMediaFormat, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from Helper.Utils import Utils


class EditorCreateWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.project_location = ''
        self.temp_location = ''


        self.setWindowTitle("VEditLog")

        icon = QIcon.fromTheme("add")
        self.open_project_button = QPushButton(icon, "Open")
        self.open_project_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.open_project_button.clicked.connect(self.find_project)

        icon = QIcon.fromTheme("emblem-package")
        self.create_project_button = QPushButton(icon, "New")
        self.create_project_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.create_project_button.clicked.connect(self.create_project)
        
        layout = QHBoxLayout()
        layout.addWidget(self.open_project_button)
        layout.addWidget(self.create_project_button)

        self.setLayout(layout)

    @Slot()
    def find_project(self):
        self.project_location = Utils.getProject(self)
        self.temp_location = Utils.createTempCopy(self.project_location)
        # open project window
        self.close_window()
        

    @Slot() 
    def create_project(self):
        # get project info
        create_project_dialogue = CreateProjectWindow()
        create_project_dialogue.exec()
        project_folder, project_name, parent_location = create_project_dialogue.getProjectInfo()

        # parent exists- just copy file
        project_location = project_folder + "/" + project_name + ".json"
        if parent_location:
            Utils.copyFile(parent_location, project_location)
            self.project_location = project_location
            self.temp_location = Utils.createTempCopy(project_location)
        # take name and create new json file
        else:
           self.project_location, self.temp_location = Utils.createProject(project_location)
        
        self.close_window()
        
           
    
    def close_window(self):
        self.close()
        self.result_callback(self.project_location, self.temp_location)
           
    def set_result_callback(self, callback):
        self.result_callback = callback

class CreateProjectWindow(QDialog):
    def __init__(self):
        super().__init__()

        icon = QIcon.fromTheme("emblem-package")

        self.project_location_label = QLabel("Location")
        self.project_location_input = QLineEdit()
        self.project_location_button = QPushButton(icon, "Browse")
        self.project_location_button.clicked.connect(self.find_folder)

        self.project_name_label = QLabel("Project Name")
        self.project_name_input = QLineEdit()
        
        self.project_parent_label = QLabel("Inherit from")
        self.project_parent_input = QLineEdit()
        self.project_parent_button = QPushButton(icon, "Select")
        self.project_parent_button.clicked.connect(self.find_project)


        self.okay_button = QPushButton("Okay")
        self.okay_button.clicked.connect(self.create_project)
        self.cancel_button = QPushButton("cancel")
        self.cancel_button.clicked.connect(self.close_window)

        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout.setSpacing(20)
        layout.addWidget(self.project_location_label, 0, 0)
        layout.addWidget(self.project_location_input, 0, 1)
        layout.addWidget(self.project_location_button, 0, 2)
        layout.addWidget(self.project_name_label, 1, 0)
        layout.addWidget(self.project_name_input, 1, 1)
        layout.addWidget(self.project_parent_label, 2, 0)
        layout.addWidget(self.project_parent_input, 2, 1)
        layout.addWidget(self.project_parent_button, 2, 2)

        selection_button_layout = QHBoxLayout()
        selection_button_layout.addWidget(self.okay_button)
        selection_button_layout.addWidget(self.cancel_button)

        layout.addLayout(selection_button_layout, 4, 1)
        self.setLayout(layout)

        

    @Slot()
    def find_folder(self):
        self.project_location_input.setText(Utils.openFolder(self))
    
    @Slot()
    def find_project(self):
        self.project_parent_input.setText(Utils.getProject(self))

    @Slot()
    def create_project(self):
        # check if input is given
        project_location, project_name, parent_location = self.getProjectInfo()        
        if self.checkInputBeforeClosing(project_location, project_name, parent_location):
            self.close()

    @Slot()
    def close_window(self):
        self.close()

    def getProjectInfo(self):
        return self.project_location_input.text(), self.project_name_input.text(), self.project_parent_input.text()

    def checkInputBeforeClosing(self, project_location, project_name, parent_location):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Invalid Input")
        if not (project_location and project_name):
            error_box.setText('Project "Directory" or "Name" can not be empty')
        elif not Utils.isDirectoryOkay(project_location):        
            error_box.setText('Invalid Directory')
        elif not Utils.isProjectNameOkay(project_location, project_name):
            error_box.setText('File Already exists in directory, Chose another project name')
        elif parent_location and not Utils.isFileOkay(parent_location):
            error_box.setText('Invalid parent project')
        else:
            return True
        # open error dialogue
        error_box.exec()
        return False
        
    

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_win = EditorCreateWindow()
#     available_geometry = main_win.screen().availableGeometry()
#     main_win.resize(available_geometry.width() / 3, available_geometry.height() / 2)
#     main_win.show()
#     sys.exit(app.exec()) 