import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot, QTimer
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication,QPushButton, QDialog, QFileDialog, QMainWindow, QSlider, QStyle, QLabel, QToolBar, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout
from PySide6.QtMultimedia import QAudioOutput, QMediaFormat, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget


class EditorWindow(QWidget):
    def __init__(self):
        super().__init__()

        icon = QIcon.fromTheme("add")
        self.open_project_button = QPushButton(icon, "Open Project")
        self.open_project_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.open_project_button.clicked.connect(self.find_project)
        
        layout = QHBoxLayout()
        layout.addWidget(self.open_project_button)

        self.setLayout(layout)

    def find_project(self):
        file_dialog = QFileDialog(self)
        project_location = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = EditorWindow()
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(available_geometry.width() / 3, available_geometry.height() / 2)
    main_win.show()
    sys.exit(app.exec()) 