from PySide6.QtWidgets import QApplication,QPushButton, QDialog, QFileDialog, QMainWindow, QSlider, QStyle, QLabel, QLineEdit, QToolBar, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout
import os, shutil, json

class Utils:
    @staticmethod
    def getProject(arg_self):
        return QFileDialog.getOpenFileName(arg_self, "Open Project", "", "json (*.json)")[0]

    @staticmethod
    def openFolder(arg_self):
        return QFileDialog.getExistingDirectory(arg_self, "Select Location", "")

    @staticmethod
    def setSizePolicyAll(arg_layout):
        for i in range(arg_layout.count()):
            widget = arg_layout.itemAt(i).widget()
            if widget is not None:
                widget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
    @staticmethod
    def getAllJSONFilesFromdir(directory):
        filenames = os.listdir(directory)
        txt_filenames = [filename for filename in filenames if os.path.splitext(filename)[1] == ".json"]
        return txt_filenames
    
    @staticmethod
    def isProjectNameOkay(directory, project_name):
        project_name = project_name + ".json"
        if project_name in Utils.getAllJSONFilesFromdir(directory):
            return False
        return True

    @staticmethod
    def isDirectoryOkay(directory):
        return os.path.isdir(directory)

    @staticmethod
    def isFileOkay(file_path):
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == ".json":
            return True
        return False

    @staticmethod
    def copyFile(source, destination):
        if Utils.isFileOkay(destination):
            os.remove(destination)
        shutil.copy(source, destination)

    @staticmethod
    def createProject(project_location):
        empty_project = {"properties": ["source", "start", "end", "is_reverse", "speed"],
                         "employees": []
                        }
        with open(project_location, "w") as f:
            json.dump(empty_project, f)
            
        temp_location = createTempCopy(project_location)
        return project_location, temp_location
            
    @staticmethod
    def createTempCopy(project_location):
        temp = project_location.split('/')
        temp[-1] = temp[-1].split('.')[0] + "_temp." + temp[-1].split('.')[1]
        temp_location = '/'.join(temp)
        Utils.copyFile(project_location, temp_location)
        
        return temp_location
            

    @staticmethod
    def projectToArray(project_location):
        with open(project_location) as f:
            object_json = json.load(f)

        data = object_json['data']
        keys= object_json['properties']

        temp = []
        for obj in data:
            row = [obj[key] for key in keys]
            temp.append(row)
        
        return [keys] + [temp]
    
    @staticmethod
    def adjust_component_height(button):
        button.setStyleSheet('''
            min-height: 30px;
        ''')

