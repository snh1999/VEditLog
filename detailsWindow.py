import sys, json
from Helper.Utils import Utils
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton, QAbstractItemView, QToolBar
from PySide6.QtCore import QAbstractTableModel, Qt

class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0])

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            return str(self._data[row][column])

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            self._data[row][column] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

class DetailsWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.table_model = MyTableModel(data)
        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.edit_button = QPushButton("Edit Row")
        self.edit_button.clicked.connect(self.edit_row)

        self.setCentralWidget(self.table_view)
        self.toolbar = QToolBar()
        self.toolbar.addWidget(self.edit_button)
        self.addToolBar(self.toolbar)

    def edit_row(self):
        selected_indexes = self.table_view.selectedIndexes()
        if selected_indexes:
            first_index = selected_indexes[0]
            self.table_view.edit(first_index)
            
        
        
        
        
            
class DetailsWindow(QMainWindow):
    def __init__(self, project_data, selected_source):
        super().__init__()
        self.project_data = project_data
        self.table_data = self.filterData(project_data, selected_source)
        
        self.table_model = MyTableModel(table_data)
        
        
    def filterData(self, selected_source):
        table_data = []
        for project_row in self.project_data:
            if project_row[0] == selected_source:
                table_data.append(project_row)
        return table_data
    
    # def update_table(self, selected_source):
        
        
                


if __name__ == '__main__':
    data = Utils.projectToArray('test.json')
    app = QApplication(sys.argv)
    window = DetailsWindow(data)
    window.show()
    sys.exit(app.exec_())
