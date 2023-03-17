from PySide6.QtWidgets import QMainWindow, QApplication, QSplitter
from PySide6.QtCore import Qt, QUrl
from ProjectDetails import ProjectDetails, History
from Helper.WindowOperation import WindowOperation
from RightWindow import RightWindow
from Helper.Utils import Utils
from Helper.Render import Render


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
        self.row_to_edit = -1
        self.project_location = project_location
        self.data = Utils.projectToArray(project_location)

        self.leftwindow = LeftWindow(self.data)
        self.rightwindow = RightWindow(len(self.data[1]))
        
        self.rightwindow.video_details_window.add_button.clicked.connect(self.add_to_project)
        self.rightwindow.video_details_window.delete_button.clicked.connect(self.delete_entry)
        self.leftwindow.project_details_window.set_result_callback(self.send_to_rightwindow)
        self.leftwindow.project_details_window.save_button.clicked.connect(self.save_project)
        self.leftwindow.project_details_window.render_button.clicked.connect(self.render_project)
        
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
        
        
    def send_to_rightwindow(self, row):
        self.row_to_edit = row
        data = self.data[1][self.row_to_edit]
        file_url = QUrl.fromLocalFile(data[0])
        self.rightwindow.video_details_window.toggle_delete_button()
        self.rightwindow.video_player_window.set_media_and_play(file_url)
        self.rightwindow.open_to_source("Update")
        self.rightwindow.video_details_window.set_values(self.row_to_edit + 1, data, len(self.data[1]))
        
        
        
    def add_to_project(self):
        new_row = self.rightwindow.video_details_window.get_all_details()
        insert_place = int(new_row[0]) - 1 if new_row[0] != 'Append' else len(self.data[1])
        new_row_data = new_row[1:]
        
        # ADD TO PROJECT + append
        if self.rightwindow.video_details_window.add_button.text().startswith('A') and insert_place == len(self.data[1]):
            self.data[1].append(new_row_data)
            self.leftwindow.project_details_window.add_new_row(new_row_data)
        # UPDATE PROJECT + same location
        elif self.rightwindow.video_details_window.add_button.text().startswith('U') and self.row_to_edit == insert_place:
            self.data[1][insert_place] = new_row_data
            self.leftwindow.project_details_window.replace_row(insert_place, new_row_data)
        
        else:
            # ADD TO PROJECT BUT IN MIDDLE/ UPDATE at a different place
            if self.rightwindow.video_details_window.add_button.text().startswith('U'):
                self.data[1].remove(self.data[1][self.row_to_edit])
            
            self.data[1].insert(int(insert_place), new_row_data)
            self.leftwindow.project_details_window.replace_table(self.data[1])
            
        if self.rightwindow.video_details_window.add_button.text().startswith('U'):
            self.rightwindow.video_details_window.toggle_delete_button()
            
        self.rightwindow.video_player_window._ensure_stopped()
        self.rightwindow.video_details_window.finish_add_button_task()
        self.row_to_edit = -1
    
    def delete_entry(self):
        self.rightwindow.video_details_window.toggle_delete_button()
        self.data[1].remove(self.data[1][self.row_to_edit])
        self.leftwindow.project_details_window.replace_table(self.data[1])
        
        self.row_to_edit = -1
        self.rightwindow.video_player_window._ensure_stopped()
        self.rightwindow.video_details_window.finish_add_button_task()
        
    def save_project(self):
        Utils.saveProject(self.project_location, self.data)
        
    def render_project(self):
        path_temp = self.project_location.split('.')
        path_temp[-1] = "mp4"
        render_path = ".".join(path_temp)
        Render.render_project(self.data[1], render_path)
        
        
            
if __name__ == "__main__":
    app = QApplication([])
    window = EditorWindow('./test.json')
    window.show()
    app.exec()