from PySide6.QtWidgets import QMainWindow, QApplication, QSplitter
from PySide6.QtCore import Qt
from ProjectDetails import ProjectDetails, History
from Helper.WindowOperation import WindowOperation
from RightWindow import RightWindow
from Helper.Utils import Utils


class LeftWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        
        # init windows
        self.project_details_window = ProjectDetails(data)
        self.history_window = History()

        self.splitter = WindowOperation.join_vertical(self.height(), self.project_details_window, self.history_window)
        self.splitter.setParent(self)
        self.setCentralWidget(self.splitter)
        
class EditorWindow(QMainWindow):
    def __init__(self, project_location):
        super().__init__()   

        data = Utils.projectToArray(project_location)

        self.leftwindow = LeftWindow(data)
        self.rightwindow = RightWindow(len(data) - 1)
        
        self.rightwindow.video_details_window.add_button.clicked.connect(self.add_to_project)
        self.setup_splitter()
        
        
        
    
    def setup_splitter(self):    
        self.splitter = QSplitter(Qt.Horizontal, self)
        self.setCentralWidget(self.splitter)
        
        # Add the windows to the main splitter
        self.splitter.addWidget(self.leftwindow.splitter)
        self.splitter.addWidget(self.rightwindow.splitter)

        self.fix_window_width_size()

    def fix_window_width_size(self):
        # Set the size of video_details_window to 40% of the total width and move it to the left
        width = int(self.width() * 0.4)
        self.splitter.setSizes([width, self.width() - width])
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 1)
        
    def add_to_project(self):
        # add project
        # get to positon and insert
        
        # update project
        # get the existing position (a variable maybe) and remove
        # put to the new position
        new_row = self.rightwindow.video_details_window.get_all_details()
        # disable button
            
if __name__ == "__main__":
    app = QApplication([])
    window = EditorWindow('ball.json')
    window.show()
    app.exec()
        
# if __name__ == "__main__":
#     app = QApplication([])
#     window = RightWindow()
#     window.show()
#     app.exec()
    