from PySide6.QtWidgets import QApplication,QPushButton, QDialog, QFileDialog, QMainWindow, QSlider, QStyle, QLabel, QLineEdit, QToolBar, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout
import os, shutil, json

DEFAULTS = {
    "start": '-',
    "end": '-',
    "quality": "default",
    "volume": '1',
    "speed": '1',
    "is_reverse": "False", 
    "rotation(degree)": "0", 
    "fade in(s)": "0", 
    "fade out(s)": "0"
}

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
        empty_project = {"properties": ["source", "start", "end", "quality", "volume", "speed", "is_reverse", "rotation(degree)", "fade in(s)", "fade out(s)"],
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
            row = [obj[key] if key in obj else DEFAULTS[key] for key in keys]
            temp.append(row)
        
        return [keys] + [temp]
    
    @staticmethod
    def adjust_component_height(button):
        button.setStyleSheet('''
            min-height: 30px;
        ''')
        
    @staticmethod
    def arrayToObj(keys, value_array):
        obj_array = []
        for value_row in value_array:
            temp_obj = {}
            for i in range(len(value_row)):
                temp_obj[keys[i]] = value_row[i]
            obj_array.append(temp_obj)
            
        return obj_array
    
    @staticmethod
    def saveProject(project_location, data):
        keys = data[0]
        value_array = data[1]
        
        object_array = Utils.arrayToObj(keys, value_array)
        project_obj = {"properties": keys, "data": object_array}

        project_json = json.dumps(project_obj, indent=4)

        
        with open(project_location, "w") as f:
            f.write(project_json)
        
        
        

