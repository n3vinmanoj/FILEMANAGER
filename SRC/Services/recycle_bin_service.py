# recycle_bin_service.py
import os
import stat
import shutil
from PySide6.QtWidgets import QMessageBox

SYSTEM_TRASH_PATH = os.path.expanduser("~/.local/share/Trash/files")
TRASH_INFO_PATH = os.path.expanduser("~/.local/share/Trash/info")

def parse_trash_info(filename):
    """Parse .trashinfo file and return metadata"""
    info_file = os.path.join(TRASH_INFO_PATH, filename + '.trashinfo')
    metadata = {
        'originalName': '',
        'originalPath': '',
        'deletedAt': '',
        'size': 0,
        'isDirectory': False
    }
    
    if not os.path.exists(info_file):
        return metadata
    
    with open(info_file, 'r') as f:
        for line in f:
            if line.startswith('Path='):
                metadata['originalPath'] = line.strip()[5:]
                metadata['originalName'] = os.path.basename(metadata['originalPath'])
            elif line.startswith('DeletionDate='):
                metadata['deletedAt'] = line.strip()[13:]
    
    return metadata

class RecycleBinService:
    def __init__(self):
        os.makedirs(SYSTEM_TRASH_PATH, exist_ok=True)
        os.makedirs(TRASH_INFO_PATH, exist_ok=True)

    def get_contents(self):
        try:
            contents = []
            for filename in os.listdir(SYSTEM_TRASH_PATH):
                filepath = os.path.join(SYSTEM_TRASH_PATH, filename)
                
                # Get metadata from .trashinfo file
                metadata = parse_trash_info(filename)
                
                # Get file stats
                try:
                    stat_info = os.stat(filepath)
                    metadata['size'] = stat_info.st_size
                    metadata['isDirectory'] = stat.S_ISDIR(stat_info.st_mode)
                except OSError:
                    pass
                
                # Add recycled path for operations
                metadata['recycledPath'] = filepath
                contents.append(metadata)
            
            return contents
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to load recycle bin: {str(e)}")
            return []
        
    def restore_item(self, recycled_path, parent=None):
        try:
            filename = os.path.basename(recycled_path)
            metadata = parse_trash_info(filename)
            
            if not metadata['originalPath']:
                QMessageBox.critical(parent, "Error", "Original path information missing")
                return False
            
            # Create parent directories if needed
            os.makedirs(os.path.dirname(metadata['originalPath']), exist_ok=True)
            
            # Restore to original location
            shutil.move(recycled_path, metadata['originalPath'])
            
            # Remove trash info file
            info_file = os.path.join(TRASH_INFO_PATH, filename + '.trashinfo')
            if os.path.exists(info_file):
                os.remove(info_file)
                
            QMessageBox.information(parent, "Success", "Item restored to original location")
            return True
        except Exception as e:
            QMessageBox.critical(parent, "Error", f"Restore failed: {str(e)}")
            return False