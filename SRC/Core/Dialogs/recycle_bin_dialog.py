from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QAbstractItemView
from UI.py.recycle_bin_dialog_ui import Ui_RecycleBinDialog
from Services.recycle_bin_service import RecycleBinService
from Utils.formatters import format_size
from Utils.delete_handler import DeleteHandler
from PySide6.QtCore import Qt

class RecycleBinDialog(QDialog, Ui_RecycleBinDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.service = RecycleBinService()
        self.delete_handler = DeleteHandler()
        
       
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
        
        self.refreshButton.clicked.connect(self.load_contents)
        self.restoreButton.clicked.connect(self.restore_selected)
        self.deleteButton.clicked.connect(self.delete_permanently)
        self.emptyButton.clicked.connect(self.empty_bin)
        
       
        self.load_contents()
    
    def load_contents(self):
        contents = self.service.get_contents()
        self.tableWidget.setRowCount(len(contents))
        
        for row, item in enumerate(contents):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item.get('originalName', '')))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item.get('originalPath', '')))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(item.get('deletedAt', '')))
            self.tableWidget.setItem(row, 3, QTableWidgetItem('Folder' if item.get('isDirectory') else 'File'))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(format_size(item.get('size', 0))))
            
            
            self.tableWidget.item(row, 0).setData(Qt.UserRole, item.get('recycledPath'))
    
    def get_selected_recycled_path(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            return self.tableWidget.item(selected_row, 0).data(Qt.UserRole)
        return None
    
    def restore_selected(self):
        recycled_path = self.get_selected_recycled_path()
        if recycled_path:
            if self.service.restore_item(recycled_path, self):
                self.load_contents()
    
    def delete_permanently(self):
        recycled_path = self.get_selected_recycled_path()
        if recycled_path:
            if self.delete_handler.delete_permanently(recycled_path, self):
                self.load_contents()
    
    def empty_bin(self):
        if self.service.empty_bin(self):
            self.load_contents()