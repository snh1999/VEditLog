# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from WelcomeScreen import EditorCreateWindow

class MainWindow():
    def __init__(self):
        self.project_location = ''
        self.temp_location = ''
        
        self.handle_welcome_screen()
        
        
    def handle_welcome_screen(self):
        def get_filepaths(project_location, temp_location):
            self.project_location = project_location
            self.temp_location = temp_location
            print(self.project_location, self.temp_location)
      
        app = QApplication(sys.argv)
        create_open_window = EditorCreateWindow()
        create_open_window.set_result_callback(get_filepaths)
        available_geometry = create_open_window.screen().availableGeometry()
        create_open_window.resize(available_geometry.width() / 3, available_geometry.height() / 2)
        create_open_window.show()  
        sys.exit(app.exec()) 
        
        
    
        
        

if __name__ == '__main__':
    main_win = MainWindow()
    
    # available_geometry = main_win.screen().availableGeometry()
    # main_win.resize(available_geometry.width() / 3, available_geometry.height() / 2)
    # main_win.show()
    # sys.exit(app.exec()) 


