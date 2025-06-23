from PySide6.QtWidgets import QDialog,QDialogButtonBox
from UI.py.create_folder_ui import Ui_CreateFolderDialog
from UI.py.rename_dialog_ui import Ui_RenameDialog
from UI.py.properties_dialog_ui import Ui_PropertiesDialog
from UI.py.delete_dialog_ui import Ui_DeleteDialog
from Utils.icons import get_icon, get_file_type
from Utils.formatters import format_size
from datetime import datetime
import os

class CreateFolderDialog(QDialog, Ui_CreateFolderDialog):
    """Dialog for creating new folders"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.folder_name_input.textChanged.connect(self.validate_input)
        self.ok_button = self.button_box.button(QDialogButtonBox.StandardButton.Ok)
        self.ok_button.setEnabled(False)
        self.folder_name_input.setFocus()
    
    def validate_input(self):
        self.ok_button.setEnabled(bool(self.folder_name_input.text().strip()))
    
    def get_folder_name(self):
        return self.folder_name_input.text().strip()

class RenameDialog(QDialog, Ui_RenameDialog):
    """Dialog for renaming files/folders"""
    def __init__(self, current_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.nameInput.setText(current_name)
        self.nameInput.selectAll()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.nameInput.setFocus()
    
    def get_new_name(self):
        return self.nameInput.text().strip()

class PropertiesDialog(QDialog, Ui_PropertiesDialog):
    """Dialog for displaying file/folder properties"""
    def __init__(self, file_info, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.file_info = file_info
        self.populate_data()
    
    def populate_data(self):
        
        self.name_label.setText(self.file_info['name'])
        self.icon_label.setPixmap(get_icon(self.file_info).pixmap(48, 48))
        
        
        file_type = "Folder" if self.file_info['isDirectory'] else get_file_type(self.file_info)
        self.type_value.setText(file_type)
        
       
        location = os.path.dirname(self.file_info['path'])
        self.location_value.setText(location)
        
        if not self.file_info['isDirectory']:
            self.size_value.setText(format_size(self.file_info['size']))
        else:
            self.size_label.hide()
            self.size_value.hide()
        
        # Set dates
        try:
            modified_time = datetime.fromtimestamp(
                self.file_info['modified'] / 1000 
                if self.file_info['modified'] > 1e10 
                else self.file_info['modified']
            )
            self.modified_value.setText(modified_time.strftime("%Y-%m-%d %H:%M:%S"))
            
            if 'created' in self.file_info:
                created_time = datetime.fromtimestamp(
                    self.file_info['created'] / 1000 
                    if self.file_info['created'] > 1e10 
                    else self.file_info['created']
                )
                self.created_value.setText(created_time.strftime("%Y-%m-%d %H:%M:%S"))
            
            if 'accessed' in self.file_info:
                accessed_time = datetime.fromtimestamp(
                    self.file_info['accessed'] / 1000 
                    if self.file_info['accessed'] > 1e10 
                    else self.file_info['accessed']
                )
                self.accessed_value.setText(accessed_time.strftime("%Y-%m-%d %H:%M:%S"))
        except:
            pass
        
        # Hide attributes group for now
        self.attributes_group.hide()

class DeleteDialog(QDialog, Ui_DeleteDialog):
    """Dialog for confirming file/folder deletion"""
    def __init__(self, item_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.messageLabel.setText(
            f"Are you sure you want to delete \"{item_name}\"?\n\n"
            "This action cannot be undone."
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)