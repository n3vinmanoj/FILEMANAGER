import os
from datetime import datetime
from PySide6.QtCore import Qt, QPoint,QSize
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QTableWidget, QTableWidgetItem, QHeaderView, 
    QAbstractItemView, QMenu, QApplication
)
from .dnd import DragDropMixin
from .Dialogs.dialogs import PropertiesDialog
from Utils.formatters import format_size
from Utils.icons import get_icon

class FileListWidget(DragDropMixin, QTableWidget):
    """Custom table widget for file listing with drag-and-drop support"""
    def __init__(self, parent=None,parent_window=None):
        super().__init__(parent)
        self.parent_window = parent_window
        self.setup_table()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
    
    def setup_table(self):
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Name", "Type", "Size", "Modified"])
        self.verticalHeader().setVisible(False)
        
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.setIconSize(QSize(16, 16))


        self.setSortingEnabled(True)
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setStyleSheet("QTableWidget { outline: none; } QTableWidget::item { outline: none; }")
        
        self.itemDoubleClicked.connect(self.on_double_click)
    
    def populate_files(self, files):
        self.setSortingEnabled(False)
        self.setRowCount(len(files))
        
        for row, file_info in enumerate(files):
            name_item = QTableWidgetItem(get_icon(file_info), file_info['name'])
            name_item.setData(Qt.ItemDataRole.UserRole, file_info)
            self.setItem(row, 0, name_item)
            
            file_type = "Folder" if file_info['isDirectory'] else "File"
            self.setItem(row, 1, QTableWidgetItem(file_type))
            
            if file_info['isDirectory']:
                size_text = "-"
            else:
                size_text = format_size(file_info['size'])
            self.setItem(row, 2, QTableWidgetItem(size_text))
            
            try:
                timestamp = file_info['modified']
                if isinstance(timestamp, str):
                    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                else:
                    dt = datetime.fromtimestamp(timestamp / 1000 if timestamp > 1e10 else timestamp)
                date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
            except:
                date_str = "Unknown"
            
            self.setItem(row, 3, QTableWidgetItem(date_str))
        
        self.setSortingEnabled(True)
        self.sortItems(0)
    
    def on_double_click(self, item):
        file_info = item.data(Qt.ItemDataRole.UserRole)
        if file_info:
            if file_info['isDirectory']:
                self.parent_window.navigate_to_path(file_info['path'])
            else:
                self.parent_window.open_file(file_info['path'])
    
    def keyPressEvent(self, event):
        """Add keyboard navigation by first letter"""
        if event.text().isalpha() and len(event.text()) == 1:
            letter = event.text().lower()
            current_row = self.currentRow()
            found_row = -1
        
        
            for row in range(current_row + 1, self.rowCount()):
                item = self.item(row, 0)
                if item and item.text().lower().startswith(letter):
                    found_row = row
                    break
        
        
            if found_row < 0:
                for row in range(0, current_row + 1):
                    item = self.item(row, 0)
                    if item and item.text().lower().startswith(letter):
                        found_row = row
                        break
        
            if found_row >= 0:
                self.setCurrentCell(found_row, 0)  
                self.scrollTo(self.model().index(found_row, 0))
                event.accept()  
                return
    
        super().keyPressEvent(event)
    def get_selected_files(self):
        
        """Get selected files from the table with full row selection"""
        selected_items = []
        
        selection_model = self.selectionModel()
        if not selection_model:
            return selected_items
            
        
        selected_rows = set()
        for index in selection_model.selectedIndexes():
            selected_rows.add(index.row())
        
        
        for row in selected_rows:
            name_item = self.item(row, 0)
            if name_item:
                file_info = name_item.data(Qt.ItemDataRole.UserRole)
                if file_info:
                    selected_items.append(file_info)
        return selected_items
    def get_selected_file(self):
        current_row = self.currentRow()
        if current_row >= 0:
            name_item = self.item(current_row, 0)
            if name_item:
                return name_item.data(Qt.ItemDataRole.UserRole)
        return None
    
    def show_context_menu(self, position):
        menu = QMenu(self)
        selected_files = self.get_selected_files()
        
        if selected_files:
            menu.addSeparator()
            properties_action = menu.addAction("📋  Properties")
            properties_action.setShortcut("Alt+Enter")
            properties_action.setToolTip("Properties (Alt+Enter)")
            properties_action.triggered.connect(
                lambda: self.show_properties(selected_files[0]) if len(selected_files) == 1 else None
            )
            properties_action.setEnabled(len(selected_files) == 1)
            
            cut_action = menu.addAction("✂️ Cut")
            cut_action.setShortcut(QKeySequence.StandardKey.Cut)
            cut_action.setToolTip("Cut (Ctrl+X)")
            cut_action.triggered.connect(self.parent_window.cut_selected)

            copy_action = menu.addAction("📋 Copy")
            copy_action.setShortcut(QKeySequence.StandardKey.Copy)
            copy_action.setToolTip("Copy (Ctrl+C)")
            copy_action.triggered.connect(self.parent_window.copy_selected)

            menu.addSeparator()

            rename_action = menu.addAction("✏️ Rename")
            rename_action.setShortcut(QKeySequence("F2"))
            rename_action.setToolTip("Rename (F2)")
            rename_action.triggered.connect(
                lambda: self.parent_window.rename_item(selected_files[0]) if len(selected_files) == 1 else None
            )
            rename_action.setEnabled(len(selected_files) == 1)

            delete_action = menu.addAction("🗑️ Delete")
            delete_action.setShortcut(QKeySequence.StandardKey.Delete)
            delete_action.setToolTip("Delete (Del)")
            delete_action.triggered.connect(self.parent_window.delete_selected)

        if self.parent_window.clipboard:
            if not menu.isEmpty():
                menu.addSeparator()
            paste_action = menu.addAction("📋 Paste")
            paste_action.setShortcut(QKeySequence.StandardKey.Paste)
            paste_action.setToolTip("Paste (Ctrl+V)")
            paste_action.triggered.connect(self.parent_window.paste_item)

        if not menu.isEmpty():
            menu.exec(self.mapToGlobal(position))
    
    def show_properties(self, file_info):
        dialog = PropertiesDialog(file_info, self.parent_window)
        dialog.exec()