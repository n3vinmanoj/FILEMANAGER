from Services.api import FileManagerAPI
from PySide6.QtWidgets import QMessageBox

class RecycleBinService:
    def __init__(self):
        self.api = FileManagerAPI()
    
    def get_contents(self):
        try:
            return self.api.get_recycle_bin_contents()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to load recycle bin: {str(e)}")
            return []
    
    def restore_item(self, recycled_path, parent=None):
        try:
            result = self.api.restore_from_recycle_bin(recycled_path)
            QMessageBox.information(parent, "Success", "Item restored successfully")
            return True
        except Exception as e:
            QMessageBox.critical(parent, "Error", f"Restore failed: {str(e)}")
            return False
    
    def empty_bin(self, parent=None):
        try:
            result = self.api.empty_recycle_bin()
            QMessageBox.information(parent, "Success", "Recycle bin emptied successfully")
            return True
        except Exception as e:
            QMessageBox.critical(parent, "Error", f"Empty failed: {str(e)}")
            return False