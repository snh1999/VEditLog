# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from videoPlayer import MainWindow

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PlayerWindow()
#     window.show()
#     sys.exit(app.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(available_geometry.width() / 3, available_geometry.height() / 2)
    main_win.show()
    sys.exit(app.exec()) 
