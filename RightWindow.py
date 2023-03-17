from PySide6.QtWidgets import QMainWindow, QApplication
from VideoDetails import VideoDetails
from VideoPlayer import VideoPlayerWindow
from Helper.WindowOperation import WindowOperation


class RightWindow(QMainWindow):
    def __init__(self, project_length):
        super().__init__()
        
         # init windows
        self.video_player_window = VideoPlayerWindow()
        self.video_details_window = VideoDetails(project_length)

        self.splitter = WindowOperation.join_vertical(self.height(), self.video_player_window, self.video_details_window)
        self.splitter.setParent(self)
        self.setCentralWidget(self.splitter)
        
        # when clip opened, update source
        self.video_player_window.open_action.triggered.connect(self.open_to_source)
        # if pick time clicked, get the current position form video
        self.video_details_window.trim_start_button.clicked.connect(self.pick_button_click)
        self.video_details_window.trim_end_button.clicked.connect(self.pick_button_click)
        
        # double click will reset
        
        
    def open_to_source(self, btn_text = "Add to Project"):
        
        source_path, clip_length = self.video_player_window.get_source()
        self.video_details_window.set_source(source_path[7:], clip_length)
        if btn_text:
            self.video_details_window.set_add_update_button_text(btn_text)
        else:
            self.video_details_window.set_add_update_button_text("Add to Project")
            
        
    def pick_button_click(self):
        if not self.video_details_window.source_path:
            return
        sender = self.sender() # the button clicked
        text = sender.text().split(' ')[1].split('!')[0]
        if text in ["Start", "End"]:
            current_time = self.video_player_window.get_player_time()
            sender.setText(text + ": " + str(current_time))
        else:
            text = sender.text().split(' ')[0].split(':')[0]
            sender.setText("Pick " + text + "!")
            
        
#window = RightWindow(0)
    