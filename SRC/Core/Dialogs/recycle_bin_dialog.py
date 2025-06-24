from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QAbstractItemView
from UI.py.recycle_bin_dialog_ui import Ui_RecycleBinDialog
from Services.recycle_bin_service import RecycleBinService
from Utils.formatters import format_size
from Utils.delete_handler import DeleteHandler
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction
from Core.Dialogs.dialogs import PropertiesDialog
from Utils.icons import get_icon

class RecycleBinDialog(QDialog, Ui_RecycleBinDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.service = RecycleBinService()
        self.delete_handler = DeleteHandler()
        
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        
        # Configure column resize modes
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Interactive)  # Name (user-resizable)
        header.setSectionResizeMode(1, QHeaderView.Stretch)      # Path (expands to fill space)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # Deleted At
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)  # Type
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)  # Size
        
        # Disable word wrapping
        self.tableWidget.setWordWrap(False)
        
        # Enable text elision (truncation with "...")
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        
        self.emptyButton.clicked.connect(self.empty_bin)
        self.load_contents()
    
    def load_contents(self):
        contents = self.service.get_contents()
        self.tableWidget.setRowCount(len(contents))
        
        for row, item in enumerate(contents):
            file_info = {
                'name': item.get('originalName', ''),
                'isDirectory': item.get('isDirectory', False)
            }

            icon = get_icon(file_info)
            
            # Name column (with icon)
            name_item = QTableWidgetItem(item.get('originalName', ''))
            name_item.setIcon(icon)
            name_item.setTextAlignment(Qt.AlignCenter)  # Center horizontally and vertically
            name_item.setToolTip(item.get('originalName', ''))
            
            # Path column
            path_item = QTableWidgetItem(item.get('originalPath', ''))
            path_item.setTextAlignment(Qt.AlignCenter)
            path_item.setToolTip(item.get('originalPath', ''))
            
            # Deleted At column
            deleted_at_item = QTableWidgetItem(item.get('deletedAt', ''))
            deleted_at_item.setTextAlignment(Qt.AlignCenter)
            deleted_at_item.setToolTip(item.get('deletedAt', ''))
            
            # Type column
            type_item = QTableWidgetItem('Folder' if item.get('isDirectory') else 'File')
            type_item.setTextAlignment(Qt.AlignCenter)
            
            # Size column
            size_item = QTableWidgetItem(format_size(item.get('size', 0)))
            size_item.setTextAlignment(Qt.AlignCenter)
            
            # Set all items
            self.tableWidget.setItem(row, 0, name_item)
            self.tableWidget.setItem(row, 1, path_item)
            self.tableWidget.setItem(row, 2, deleted_at_item)
            self.tableWidget.setItem(row, 3, type_item)
            self.tableWidget.setItem(row, 4, size_item)
            
            # Store entire item data for properties dialog
            self.tableWidget.item(row, 0).setData(Qt.UserRole, item)
    
    # Rest of the class remains unchanged...
    def get_selected_item(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            return self.tableWidget.item(selected_row, 0).data(Qt.UserRole)
        return None
    def contextMenuEvent(self, event):
        item = self.tableWidget.itemAt(event.pos())
        if item:
            menu = QMenu(self)
            
            # Add Properties as first option
            properties_action = QAction("Properties", self)
            menu.addAction(properties_action)
            
            menu.addSeparator()
            
            restore_action = QAction("Restore", self)
            delete_action = QAction("Permanently Delete", self)
            
            menu.addAction(restore_action)
            menu.addAction(delete_action)
            
            action = menu.exec(event.globalPos())
            
            if action == properties_action:
                self.show_properties()
            elif action == restore_action:
                self.restore_selected()
            elif action == delete_action:
                self.delete_permanently()
    
    def show_properties(self):
        item = self.get_selected_item()
        if item:
            # Create a file_info structure that PropertiesDialog expects
            file_info = {
                'name': item.get('originalName', ''),
                'path': item.get('originalPath', ''),
                'isDirectory': item.get('isDirectory', False),
                'size': item.get('size', 0),
                'modified': item.get('deletedAtTimestamp', 0)  # Use deletion timestamp
            }
            
            # Show properties dialog
            dialog = PropertiesDialog(file_info, self)
            dialog.exec()

    def restore_selected(self):
        item = self.get_selected_item()
        if item and 'recycledPath' in item:
            if self.service.restore_item(item['recycledPath'], self):
                self.load_contents()
    
    def delete_permanently(self):
        item = self.get_selected_item()
        if item and 'recycledPath' in item:
            if self.delete_handler.delete_permanently(item['recycledPath'], self):
                self.load_contents()
    
    def empty_bin(self):
        if self.service.empty_bin(self):
            self.load_contents()