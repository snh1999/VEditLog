import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton, QAbstractItemView, QToolBar, QLabel, QHBoxLayout
from PySide6.QtCore import QAbstractTableModel, Qt
from Helper.Utils import Utils

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

class History(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QLabel('History', self)

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

# if __name__ == '__main__':

#     data = Utils.projectToArray('test.json')
#     app = QApplication(sys.argv)
#     window = ProjectDetails(data)
#     window.show()
#     sys.exit(app.exec())