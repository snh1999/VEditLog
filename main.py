# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from WelcomeScreen import EditorCreateWindow
from EditorWindow import EditorWindow

class MainWindow():
    def __init__(self):
        self.project_location = ''
        self.temp_location = ''
        
        self.handle_welcome_screen()
        
        
        
        
    def handle_welcome_screen(self):
        def get_filepaths(project_location, temp_location):
            self.project_location = project_location
            self.temp_location = temp_location
            self.open_editor_window()
            # open editor window
      
        self.app = QApplication(sys.argv)
        create_open_window = EditorCreateWindow()
        create_open_window.set_result_callback(get_filepaths)
        available_geometry = create_open_window.screen().availableGeometry()
        create_open_window.resize(available_geometry.width() / 3, available_geometry.height() / 2)
        create_open_window.show()  
        sys.exit(self.app.exec()) 
        
    def open_editor_window(self):
        window = EditorWindow(self.project_location)
        available_geometry = window.screen().availableGeometry()
        window.resize(available_geometry.width() / 3, available_geometry.height() / 2)
        window.show()
            
        
    
        
        

if __name__ == '__main__':
    main_win = MainWindow()


