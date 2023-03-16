# import sys, json
# from utils import Utils

# from PySide6.QtCore import Qt, QAbstractTableModel
# from PySide6.QtGui import QColor, QBrush
# from PySide6.QtWidgets import QApplication, QTableView, QMainWindow


# class MyTableModel(QAbstractTableModel):
#     def __init__(self, data):
#         QAbstractTableModel.__init__(self)
#         # properties - header data
#         # data
#         self._data = data
#         print(self._data['employees'])
#         print(self._data['properties'])


#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             row = index.row()
#             column = index.column()
#             return str(self._data['employees'][row][column])

#     def rowCount(self, index):
#         return len(self._data)

#     def columnCount(self, index):
#         return len(self._data['properties'][0])

#     def headerData(self, section, orientation, role):
#         if role == Qt.DisplayRole and orientation == Qt.Horizontal:
#             return str(self._data['properties'][section])


# app = QApplication(sys.argv)
# window = QMainWindow()
# view = QTableView()


# object_json = {
#     "properties": ["name", "age", "position"],
#     "employees": [
#         {
#             "name": "John Doe",
#             "age": 35,
#             "position": "Manager"
#         },
#         {
#             "name": "Jane Doe",
#             "age": 28,
#             "position": "Software Engineer"
#         },
#         {
#             "name": "Bob Smith",
#             "age": 40,
#             "position": "Product Manager"
#         }
#     ]
# }
# with open('test.json') as f:
#     object_json = json.load(f)

# data = object_json['employees']
# keys= object_json['properties']

# table = [keys]

# for obj in data:
#     row = [obj[key] for key in keys]
#     table.append(row)


# model = MyTableModel(data)
# view.setModel(model)
# window.setCentralWidget(view)
# window.show()
# sys.exit(app.exec_())
# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton, QAbstractItemView, QToolBar
# from PySide6.QtCore import QAbstractTableModel, Qt
# from Helper.Utils import Utils

# class MyTableModel(QAbstractTableModel):
#     def __init__(self, data):
#         super().__init__()
#         self._data = data

#     def rowCount(self, parent=None):
#         return len(self._data)

#     def columnCount(self, parent=None):
#         return len(self._data[0])

#     def data(self, index, role=Qt.DisplayRole):
#         if role == Qt.DisplayRole:
#             row = index.row()
#             column = index.column()
#             return str(self._data[row][column])

#     def setData(self, index, value, role=Qt.EditRole):
#         if role == Qt.EditRole:
#             row = index.row()
#             column = index.column()
#             self._data[row][column] = value
#             self.dataChanged.emit(index, index)
#             return True
#         return False

#     def flags(self, index):
#         return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

# class MainWindow(QMainWindow):
#     def __init__(self, data):
#         super().__init__()

#         self.table_model = MyTableModel(data)
#         self.table_view = QTableView()
#         self.table_view.setModel(self.table_model)
#         self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
#         self.table_view.setEditTriggers(QAbstractItemView.DoubleClicked)

#         self.edit_button = QPushButton("Edit Row")
#         self.edit_button.clicked.connect(self.edit_row)

#         self.setCentralWidget(self.table_view)
#         self.toolbar = QToolBar()
#         self.toolbar.addWidget(self.edit_button)
#         self.addToolBar(self.toolbar)

#     def edit_row(self):
#         selected_indexes = self.table_view.selectedIndexes()
#         if selected_indexes:
#             first_index = selected_indexes[0]
#             self.table_view.edit(first_index)

# if __name__ == '__main__':

    # with open('test.json') as f:
    #     object_json = json.load(f)

    # data = object_json['employees']
    # keys= object_json['properties']

    # table = [keys]

    # for obj in data:
    #     row = [obj[key] for key in keys]
    #     table.append(row)
    
    # print(table)

    # data = Utils.projectToArray('test.json')
    # app = QApplication(sys.argv)
    # window = MainWindow(data)
    # window.show()
    # sys.exit(app.exec())

###########################################

# import sys
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QSizePolicy
# from PySide6.QtCore import Qt


# class ThreeWindows(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Get the screen dimensions
#         # screen_size = QDesktopWidget().screenGeometry()

#         # # Set the minimum size as a percentage of the screen size
#         # min_width = int(screen_size.width() * 0.3) # 30% of screen width
#         # min_height = int(screen_size.height() * 0.3) # 30% of screen height
#         # self.setMinimumSize(min_width, min_height)

#         # Create three windows
#         self.window1 = QWidget(self)
#         self.window2 = QWidget(self)
#         self.window3 = QWidget(self)
        
#         # Set the minimum size for each window
#         self.window1.setMinimumSize(100, 100)
#         self.window2.setMinimumSize(100, 100)
#         self.window3.setMinimumSize(100, 100)

#         # Set the background colors of the windows
#         self.window1.setStyleSheet("background-color: red;")
#         self.window2.setStyleSheet("background-color: green;")
#         self.window3.setStyleSheet("background-color: blue;")
        

#         # Create a splitter widget for the top two windows and set its orientation to Qt.Vertical
#         splitter = QSplitter(self)
#         splitter.setOrientation(Qt.Vertical)
#         splitter.addWidget(self.window1)
#         splitter.addWidget(self.window2)

#         # Create a vertical layout for the top two windows and add the splitter to it
#         top_layout = QVBoxLayout()
#         top_layout.addWidget(splitter)

#         # Create a horizontal layout for the top two windows and add the layout to the main layout
#         top_h_layout = QHBoxLayout()
#         top_h_layout.addLayout(top_layout)
#         top_h_layout.setStretchFactor(top_layout, 1)
#         self.setLayout(top_h_layout)

#         # Create a vertical layout for the bottom window and add it to the main layout
#         bottom_layout = QVBoxLayout()
#         bottom_layout.addWidget(self.window3)
#         bottom_layout.setStretchFactor(self.window3, 1)
#         self.layout().addLayout(bottom_layout)

#         # Set the size policy of the bottom window to expand vertically
#         self.window3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # Set the initial size of each widget in the splitter
#         splitter.setSizes([200, 200])

#         # Set the minimum size of each widget in the splitter
#         self.window1.setMinimumSize(100, 100)
#         self.window2.setMinimumSize(100, 100)
#         self.window3.setMinimumSize(100, 50)

#         # Connect the handleMoved signal to the handleMovedSlot method
#         splitter.splitterMoved.connect(self.handleMovedSlot)
        
#     def handleMovedSlot(self, pos, index):
#         # Get the minimum and maximum sizes for each window
#         min_sizes = [w.minimumSize() for w in self.windows]
#         max_sizes = [self.splitter.width() - self.splitter.handleWidth() - sum(min_sizes),
#                     self.splitter.height() * 0.75 - self.splitter.handleWidth() - sum(min_sizes),
#                     self.splitter.height() * 0.25 - self.splitter.handleWidth() - sum(min_sizes)]
#         # Calculate the total available space in the splitter
#         total_space = sum(max_sizes) + sum(min_sizes)

#         # Calculate the new sizes for each window based on the available space and the minimum and maximum sizes
#         sizes = []
#         for i in range(3):
#             if i != index:
#                 space_taken = sum(sizes) + min_sizes[i] + pos
#                 max_size = max_sizes[i] - (space_taken - total_space)
#                 size = max(min_sizes[i], min(max_sizes[i], max_size))
#             else:
#                 size = max(min_sizes[i], (max_sizes[i] * (total_space - pos) // total_space))
#             sizes.append(size)

#         # Adjust the sizes of the windows in the splitter
#         self.splitter.setSizes(sizes)

#     def resizeEvent(self, event):
#         # Set the minimum size of each widget in the splitter
#         self.window1.setMinimumSize(100, 100)
#         self.window2.setMinimumSize(100, 100)
#         self.window3.setMinimumSize(100, 50)

#         super().resizeEvent(event)
        
        
        
#         # # Create a splitter widget and add the three windows to it
#         # splitter = QSplitter(self)
#         # splitter.addWidget(window1)
#         # splitter.addWidget(window2)
#         # splitter.addWidget(window3)

#         # # Create a horizontal layout and add the splitter to it
#         # layout = QHBoxLayout(self)
#         # layout.addWidget(splitter)
#         # self.setLayout(layout)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = ThreeWindows()
#     ex.show()
#     sys.exit(app.exec_())



############## 4 window setup

# from PySide6 import QtCore, QtGui, QtWidgets
# from VideoDetails import VideoDetails
# from VideoPlayer import VideoPlayerWindow


# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("test")

#         self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self)
#         self.setCentralWidget(self.splitter)

#         self.init_all_windows()
        
#         # Set the background colors of the windows
#         self.window1.setStyleSheet("background-color: red;")

#         # Create the vertical splitter for video_player_window and video_details_window
#         self.rightverticalSplitter = QtWidgets.QSplitter(QtCore.Qt.Vertical, self)
#         self.rightverticalSplitter.addWidget(self.video_player_window)
#         self.rightverticalSplitter.addWidget(self.video_details_window)
        
#         self.leftverticalSplitter = QtWidgets.QSplitter(QtCore.Qt.Vertical, self)
#         self.leftverticalSplitter.addWidget(self.window1)
#         self.leftverticalSplitter.addWidget(self.window4)

#         # Add the windows to the main splitter
#         self.splitter.addWidget(self.leftverticalSplitter)
#         self.splitter.addWidget(self.rightverticalSplitter)

        
#         self.fix_window_width_size()
#         self.fix_window_height_size()
# # 
        
        
#     def init_all_windows(self):
#         self.window1 = QtWidgets.QWidget(self)
#         self.video_player_window = VideoPlayerWindow()
#         self.video_details_window = VideoDetails()
#         self.window4 = QtWidgets.QWidget(self)

#         # # Set the minimum size for each window
#         self.window1.setMinimumSize(100, 100)
#         self.video_player_window.setMinimumSize(100, 100)
#         self.video_details_window.setMinimumSize(100, 100)
#         self.window4.setMinimumSize(100, 100)
        
#         # Set the size policy for window1 and video_player_window
#         self.window1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#         self.video_player_window.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            
#     def fix_window_width_size(self):
#         # Set the size of video_details_window to 40% of the total width and move it to the left
#         width = int(self.width() * 0.4)
#         self.splitter.setSizes([width, self.width() - width])
#         self.splitter.setStretchFactor(0, 1)
#         self.splitter.setStretchFactor(1, 1)
            
#     def fix_window_height_size(self):
#         # Set the size of video_player_window to 70% of the available height of the total height
#         height = int(self.height() * 0.8)
#         self.rightverticalSplitter.setSizes([height, self.height() - height])
#         self.rightverticalSplitter.setStretchFactor(0, 1)
#         self.rightverticalSplitter.setStretchFactor(1, 1)
        
#         self.leftverticalSplitter.setSizes([height, self.height() - height])
#         self.leftverticalSplitter.setStretchFactor(0, 1)
#         self.leftverticalSplitter.setStretchFactor(1, 1)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

# from PyQt5.QtWidgets import (
#     QApplication,
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QTableWidgetItem,
#     QPushButton,
#     QHBoxLayout,
#     QLineEdit,
#     QHeaderView,
# )
# from PyQt5.QtCore import Qt
# import sys

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Set up the table
#         self.table = QTableWidget()
#         self.table.setColumnCount(2)
#         self.table.setHorizontalHeaderLabels(["Summary", ""])
#         self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
#         self.table.verticalHeader().setVisible(False)
#         self.table.setEditTriggers(QTableWidget.NoEditTriggers)

#         # Add some example rows
#         self.add_row("Input 1", "Value 1", "Value 2")
#         self.add_row("Input 2", "Value 3", "Value 4")
#         self.add_row("Input 3", "Value 5", "Value 6")

#         # Set up the layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.table)
#         self.setLayout(layout)

#     def add_row(self, summary, *input_fields):
#     # Add a new row to the table
#         row_count = self.table.rowCount()
#         self.table.insertRow(row_count)

#         # Set the summary
#         summary_item = QTableWidgetItem(summary)
#         self.table.setItem(row_count, 0, summary_item)

#         # Set up the expand button
#         expand_button = QPushButton("+")
#         expand_button.setCheckable(True)
#         expand_button.clicked.connect(lambda: self.expand_row(row_count))
        
#         # expand_button.clicked.connect(lambda: self.expand_row(expand_button))
#         self.table.setCellWidget(row_count, 1, expand_button)
        

#         # Add an empty row
#         self.table.insertRow(row_count + 1)

#         # Set up the input fields
#         input_widget = QWidget()
#         input_widget.setObjectName("input_widget")  # set the object name
#         input_widget_layout = QVBoxLayout()
#         for input_field in input_fields:
#             input_widget_row = QHBoxLayout()
#             input_widget_row.addWidget(QLineEdit(input_field))
#             input_widget_layout.addLayout(input_widget_row)
#         input_widget.setLayout(input_widget_layout)
#         input_widget.setVisible(False)
#         self.table.setCellWidget(row_count + 2, 0, input_widget)


#     def expand_row(self, row):
#         summary_widget = self.table.cellWidget(row, 1)
#         input_widget = summary_widget.parent().cellWidget(row, 0)

#         if input_widget.isVisible():
#             input_widget.setVisible(False)
#             self.table.setRowHeight(self.table.currentRow() + 1, 0)
#             button.setText("+")
#         else:
#             input_widget.setVisible(True)
#             self.table.setRowHeight(self.table.currentRow() + 1, 100)
#             button.setText("-")



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())



from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from Helper.Utils import Utils


class Table(QTableWidget):
    def __init__(self, project_array):
        super().__init__()
        header = project_array[0]
        data = project_array[1]
        
        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)
        self.populate(data)
        
    def populate(self, data):
        self.setRowCount(0)  # clear the table
        self.setRowCount(len(data))
        for row in range(len(data)):
            for col in range(len(data[row])):
                item = QTableWidgetItem(str(data[row][col]))
                self.setItem(row, col, item)

    def add_row(self, row_data):
        row = self.rowCount()
        self.setRowCount(row+1)
        for col in range(len(row_data)):
            item = QTableWidgetItem(str(row_data[col]))
            self.setItem(row, col, item)
            
    def replace_row(self, row_num, row_data):
        for col in range(len(row_data)):
            item = QTableWidgetItem(str(row_data[col]))
            self.setItem(row_num, col, item)
            
    def mouseDoubleClickEvent(self, event):
        row = self.currentRow()
        self.selectRow(row)
        event.accept()
        self.set_result_callback(row)
           
    def set_result_callback(self, callback):
        self.result_callback = callback
        

class ProjectDetails(QMainWindow):
    def __init__(self, project_array):
        super().__init__()
        self.table = Table(project_array)
        self.save_button = QPushButton('Save Project')
        self.render_button = QPushButton('Render')
        
        # self.table_view.doubleClicked.connect(self.edit_row)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.render_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(button_layout)

        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
    def add_new_row(self, new_row_data):
        self.table.add_row(new_row_data)
        print(self.get_rows())
    
    def get_rows(self):
        rows = []
        for row in range(self.table.rowCount()):
            row_values = []
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item is not None:
                    row_values.append(item.text())
                else:
                    row_values.append('')
            rows.append(row_values)
        return rows
    
    def replace_table(self, new_table_data):
        self.table.populate(new_table_data)
        
    def onReplaceRowClicked(self, row_num, new_row_data):
        self.table.replace_row(row_num, new_row_data)

if __name__ == '__main__':
    app = QApplication([])
    data = Utils.projectToArray('test.json')
    
    window = ProjectDetails(data)
    # create_open_window.set_result_callback(get_filepaths)
    window.show()
    app.exec()


# from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


# class Table(QWidget):
#     def __init__(self, num_rows, num_columns):
#         super().__init__()

#         # Create the table widget
#         self.table = QTableWidget(num_rows, num_columns, self)

#         # Set up the layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.table)
#         self.setLayout(layout)

#     def add_row(self, row_values):
#         """
#         Add a new row to the table with the given values.
#         """
#         row_position = self.table.rowCount()
#         self.table.insertRow(row_position)

#         for column, value in enumerate(row_values):
#             item = QTableWidgetItem(str(value))
#             self.table.setItem(row_position, column, item)

#     def get_rows(self):
#         """
#         Retrieve all rows from the table as a list of lists.
#         """
#         rows = []
#         for row in range(self.table.rowCount()):
#             row_values = []
#             for column in range(self.table.columnCount()):
#                 item = self.table.item(row, column)
#                 if item is not None:
#                     row_values.append(item.text())
#                 else:
#                     row_values.append('')
#             rows.append(row_values)
#         return rows


# if __name__ == '__main__':
#     app = QApplication([])
#     window = QMainWindow()
#     table = Table(3, 2)
#     window.setCentralWidget(table)

#     # Add some rows
#     table.add_row([1, 2])
#     table.add_row([3, 4])
#     table.add_row([5, 6])

#     # Retrieve all rows
#     rows = table.get_rows()
#     print(rows)

#     window.show()
#     app.exec()
