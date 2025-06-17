from Services.api import FileManagerAPI
from PySide6.QtWidgets import QMessageBox

class DeleteHandler:
    def __init__(self):
        self.api = FileManagerAPI()
    
    def confirm_and_delete(self, item_path, item_name, parent_widget, use_recycle_bin=False):
        """
        Handle the entire delete process with confirmation and recycle bin option
        """
        # Show confirmation dialog
        if use_recycle_bin:
            message = f"Move '{item_name}' to Recycle Bin?"
            title = "Move to Recycle Bin"
        else:
            message = f"Permanently delete '{item_name}'?"
            title = "Confirm Delete"
        
        msg_box = QMessageBox(
            QMessageBox.Icon.Question,
            title,
            f"{message}\n\nThis action cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            parent_widget
        )
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        
        if msg_box.exec() != QMessageBox.StandardButton.Yes:
            return False
        
        try:
            self.api.delete_item(item_path, use_recycle_bin)
            return True
        except Exception as e:
            QMessageBox.critical(parent_widget, "Error", f"Delete failed: {str(e)}")
            return False
    
    def delete_permanently(self, path, parent_widget):
        """
        Permanently delete an item without recycle bin option
        """
        try:
            # Confirm with user
            if QMessageBox.question(
                parent_widget,
                "Confirm Permanent Deletion",
                "Are you sure you want to permanently delete this item?\n\nThis action cannot be undone.",
                QMessageBox.Yes | QMessageBox.No
            ) == QMessageBox.No:
                return False
            
            self.api.delete_item(path, False)
            return True
        except Exception as e:
            QMessageBox.critical(parent_widget, "Error", f"Delete failed: {str(e)}")
            return False