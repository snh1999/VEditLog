from PySide6.QtWidgets import QSplitter, QSizePolicy, QMainWindow
from PySide6.QtCore import Qt
from VideoDetails import VideoDetails
from VideoPlayer import VideoPlayerWindow


class WindowOperation(QMainWindow):
    
    
    @staticmethod
    def join_vertical(height, window1, window2):

        # # Set the minimum size for each window
        window1.setMinimumSize(100, 100)
        window2.setMinimumSize(100, 100)
        
        # Set the size policy for window1 and video_player_window
        window1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Create the vertical splitter for video_player_window and video_details_window
        splitter = QSplitter(Qt.Vertical)
        
        splitter.addWidget(window1)
        splitter.addWidget(window2)


        # Set the size of video_player_window to 70% of the available height of the total height
        height1 = int(height * 0.8)
        splitter.setSizes([height1, height - height1])
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        
        return splitter
        
        
    