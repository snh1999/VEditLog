# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 Multimedia player example"""

import sys, time
from PySide6.QtCore import QStandardPaths, Qt, Slot, QTimer
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow, QSlider, QStyle, QLabel, QToolBar, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout
from PySide6.QtMultimedia import QAudioOutput, QMediaFormat, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget


AVI = "video/x-msvideo"  # AVI


MP4 = 'video/mp4'


def get_supported_mime_types():
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self._playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?
        self._playlist_index = -1
        self.replay_flag = False
        self.playback_speed = 1
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        self._player.errorOccurred.connect(self._player_error)
        self.initUI()

    def initUI(self):
        ############################################# Create tool bar #################################################
        tool_bar = QToolBar()
        # self.addToolBar(tool_bar)
        self.addToolBar(Qt.BottomToolBarArea, tool_bar)

        ############################### File Menu ############################
        file_menu = self.menuBar().addMenu("&File")
        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open...", self, shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)
        tool_bar.addAction(open_action)
        icon = QIcon.fromTheme("application-exit")
        exit_action = QAction(icon, "&Exit", self, shortcut="Ctrl+Q", triggered=self.close)
        file_menu.addAction(exit_action)

        ############################### Play Menu ############################
        play_menu = self.menuBar().addMenu("&Play")
        style = self.style()
        icon = QIcon.fromTheme("media-playback-start.png", style.standardIcon(QStyle.SP_MediaPlay))
        self._play_action = tool_bar.addAction(icon, "Play")
        self._play_action.triggered.connect(self._player.play)
        play_menu.addAction(self._play_action)

        icon = QIcon.fromTheme("media-skip-backward-symbolic.svg", style.standardIcon(QStyle.SP_MediaSkipBackward))
        self._previous_action = tool_bar.addAction(icon, "Previous")
        self._previous_action.triggered.connect(self.previous_clicked)
        play_menu.addAction(self._previous_action)

        icon = QIcon.fromTheme("media-playback-pause.png", style.standardIcon(QStyle.SP_MediaPause))
        self._pause_action = tool_bar.addAction(icon, "Pause")
        self._pause_action.triggered.connect(self._player.pause)
        play_menu.addAction(self._pause_action)

        icon = QIcon.fromTheme("media-skip-forward-symbolic.svg", style.standardIcon(QStyle.SP_MediaSkipForward))
        self._next_action = tool_bar.addAction(icon, "Next")
        self._next_action.triggered.connect(self.next_clicked)
        play_menu.addAction(self._next_action)

        icon = QIcon.fromTheme("media-playback-stop.png", style.standardIcon(QStyle.SP_MediaStop))
        self._stop_action = tool_bar.addAction(icon, "Stop")
        self._stop_action.triggered.connect(self._ensure_stopped)
        play_menu.addAction(self._stop_action)

        icon = QIcon.fromTheme("add")
        self._add_queue_action = tool_bar.addAction(icon, "Queue")
        self._add_queue_action.triggered.connect(self._add_to_queue)
        play_menu.addAction(self._add_queue_action)

        icon = QIcon.fromTheme("view-refresh")
        self.replay_action = tool_bar.addAction(icon, "Replay: " + str(self.replay_flag))
        self.replay_action.triggered.connect(self.replay_video)
        play_menu.addAction(self.replay_action)

        # icon = QIcon.fromTheme("view-refresh")
        self.speed_action = tool_bar.addAction(str(self.playback_speed)+"x")
        self.speed_action.triggered.connect(self.adjust_playback_speed)
        # play_menu.addAction(self.replay_action)

        ############################### Add space ###########################
        spacer = QWidget()
        spacer.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Preferred)
        tool_bar.addWidget(spacer)
        ############################### slider ############################
        self._volume_slider = QSlider()
        self._volume_slider.setOrientation(Qt.Horizontal)
        self._volume_slider.setMinimum(0)
        self._volume_slider.setMaximum(100)
        available_width = self.screen().availableGeometry().width()
        self._volume_slider.setFixedWidth(available_width / 10)
        self._volume_slider.setValue(self._audio_output.volume())
        self._volume_slider.setTickInterval(10)
        self._volume_slider.setTickPosition(QSlider.TicksBelow)
        self._volume_slider.setToolTip("Volume")
        self._volume_slider.valueChanged.connect(self._audio_output.setVolume)
        tool_bar.addWidget(self._volume_slider)
        
        ############################### Finally Video widget ############################

        ############################### About Menu ############################
        about_menu = self.menuBar().addMenu("&About")
        about_qt_act = QAction("About &Qt", self, triggered= qApp.aboutQt)
        about_menu.addAction(about_qt_act)

        ############################### Finally Video widget ############################
        self._video_widget = QVideoWidget()

        body_widget_containter = QWidget(self)
        self.setCentralWidget(body_widget_containter)

        self.video_duration = QLabel()
        self.video_duration.setText("/ --")

        self.video_current_position = QLabel()
        self.video_current_position.setText("--")
        # creating a timer object
        timer = QTimer(self)
        timer.timeout.connect(self.updateVideoPosition)
        timer.start(1000)


        self.video_seek_slider = QSlider(Qt.Orientation.Horizontal)
        self.video_seek_slider.setRange(0, 0)
        self.video_seek_slider.sliderMoved.connect(self.setPosition)
        

        bottom_control_layout = QHBoxLayout()
        bottom_control_layout.setContentsMargins(0, 0, 0, 0)
        bottom_control_layout.addWidget(self.video_current_position)
        bottom_control_layout.addWidget(self.video_duration)
        bottom_control_layout.addWidget(self.video_seek_slider)
        # TODO- add time as well



        main_layout = QVBoxLayout()
        main_layout.addWidget(self._video_widget)
        main_layout.addLayout(bottom_control_layout)
        # main_layout.addWidget(self.errorLabel)

        body_widget_containter.setLayout(main_layout)
        
        
        # self.setCentralWidget(self._video_widget)
        self._player.playbackStateChanged.connect(self.update_buttons)
        self._player.setVideoOutput(self._video_widget)
        self._player.positionChanged.connect(self.positionChanged)
        self._player.durationChanged.connect(self.durationChanged)

        self.update_buttons(self._player.playbackState())
        self._mime_types = []




    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()


    def openDialogue(self):
        file_dialog = QFileDialog(self)
        is_windows = sys.platform == 'win32'
        if not self._mime_types:
            self._mime_types = get_supported_mime_types()
            if (is_windows and AVI not in self._mime_types):
                self._mime_types.append(AVI)
            elif MP4 not in self._mime_types:
                self._mime_types.append(MP4)

        file_dialog.setMimeTypeFilters(self._mime_types)
        default_mimetype = AVI if is_windows else MP4
        if default_mimetype in self._mime_types:
            file_dialog.selectMimeTypeFilter(default_mimetype)

        movies_location = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)

        return file_dialog

    def updateTimeWidgets(self):
        self.video_duration.setText("/" + str(self.getDurationInMins(self._player.duration())))
        self.video_current_position.setText(str(self.getDurationInMins(self._player.position())))

    def playMedia(self, url):
        self._player.setSource(url)
        self.updateTimeWidgets()
        self._player.play()

    @Slot()
    def open(self):
        self._ensure_stopped()

        file_dialog = self.openDialogue()

        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._playlist.append(url)
            self._playlist_index = len(self._playlist) - 1
            self.playMedia(url)

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    @Slot()
    def previous_clicked(self):
        # Go to previous track if we are within the first 10 seconds of playback
        # Otherwise, seek to the beginning.
        if self._player.position() <= 10000 and self._playlist_index > 0:
            self._playlist_index -= 1
            # self._playlist.previous()
            # self._player.setSource(self._playlist[self._playlist_index])
            self.playMedia(self._playlist[self._playlist_index])
        else:
            self._player.setPosition(0)

    @Slot()
    def next_clicked(self):
        if self._playlist_index < len(self._playlist) - 1:
            self._playlist_index += 1
            # self._player.setSource(self._playlist[self._playlist_index])
            self.playMedia(self._playlist[self._playlist_index])


    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        media_count = len(self._playlist)
        self._play_action.setEnabled(media_count > 0
            and state != QMediaPlayer.PlayingState)
        self._pause_action.setEnabled(state == QMediaPlayer.PlayingState)
        self._stop_action.setEnabled(state != QMediaPlayer.StoppedState)
        self._previous_action.setEnabled(self._playlist_index > 0)
        self._next_action.setEnabled(media_count > 1)


    @Slot()
    def _add_to_queue(self):
        self._ensure_stopped()

        file_dialog = self.openDialogue()
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._playlist.append(url)
        self._player.play()
            # self._playlist_index = len(self._playlist) - 1
            # self._player.setSource(url)
            # self.video_duration.setText("/" + str(self.getDurationInMins(self._player.duration())))
            # self.video_current_position.setText(str(self.getDurationInMins(self._player.position())))
            # self._player.play()

    @Slot()
    def replay_video(self):
        if self.replay_flag and self._playlist and self._player.playbackState() != QMediaPlayer.PlayingState:
            self.replay_current()
        else: 
            print("jere")
            self.replay_flag = not self.replay_flag
        self.replay_action.setToolTip("Replay: " + str(self.replay_flag))

    @Slot()
    def adjust_playback_speed(self):
        print("here")
        if self.playback_speed == 1:
            self._player.setPlaybackRate(2)
            self.playback_speed = 2
        elif self.playback_speed == 2:
            self._player.setPlaybackRate(3)
            self.playback_speed = 3
        elif self.playback_speed == 3:
            self._player.setPlaybackRate(4)
            self.playback_speed = 4
        elif self.playback_speed == 4:
            self._player.setPlaybackRate(1)
            self.playback_speed = 1
        self.speed_action.setIconText(str(self.playback_speed)+"x")
            

    

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    @Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)


    def positionChanged(self, position):
        self.video_seek_slider.setValue(position)

    def durationChanged(self, duration):
        self.video_seek_slider.setRange(0, duration)

    def setPosition(self, position):
        self._player.setPosition(position)

    def getDurationInMins(self, total_time):
        minute_converted = total_time/1000/60
        seconds_converted = (minute_converted - int(minute_converted)) * 60
        def returnString(time_num):
            if time_num < 10:
                return "0" + str(int(time_num))
            return str(int(time_num)) 
        return returnString(minute_converted) + ":" + returnString(seconds_converted)

        

    def updateVideoPosition(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self.video_current_position.setText(str(self.getDurationInMins(self._player.position())))
        elif self._playlist and (self._player.position() >= self._player.duration() - 100):
            if self.replay_flag:
                self.replay_current()
            elif  self._playlist_index < len(self._playlist) - 1:
                self.next_clicked()
    
    def replay_current(self):
        self._player.setPosition(0)
        self._player.position()
        time.sleep(1)
        self.playMedia(self._playlist[self._playlist_index])