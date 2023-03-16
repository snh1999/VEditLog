import sys, json
from PySide6.QtCore import QStandardPaths, Qt, Slot, QTimer
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication,QPushButton, QDialog, QFileDialog, QMainWindow, QSlider, QStyle, QLabel, QMessageBox, QLineEdit, QToolBar, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtMultimedia import QAudioOutput, QMediaFormat, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from Helper.Utils import Utils

from VideoPlayer import VideoPlayerWindow
from detailsWindow import DetailsWindow


class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VEditLog - Editor")

        available_geometry = self.screen().availableGeometry()
        window_width, window_height = available_geometry.width(), available_geometry.height()

        # TODO - do something about this
        data = Utils.projectToArray('test.json')

        detailWindow = DetailsWindow(data)
        detailWindow.setGeometry(0, 0, window_width * 0.2, window_height * 0.7)

        playerWindow = VideoPlayerWindow()
        playerWindow.setGeometry(0, 0, window_width * 0.6, window_height * 0.7)

        layout = QHBoxLayout()
        layout.addWidget(detailWindow)
        layout.addWidget(playerWindow)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


        # combine 3 window to make one 
        # right for player
        # left for baler details from json
        # niche kothao edit window
        # ekta render button --- koi kormu chagol choda?
        # ekta save button -- project details er niche

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = EditorWindow()
    # available_geometry = main_win.screen().availableGeometry()
    # main_win.resize(available_geometry.width(), available_geometry.height())
    main_win.show()
    sys.exit(app.exec()) 