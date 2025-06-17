"""
File Manager API - Handles file operations using local file service
"""
import os
import sys
from file_service import file_service

class FileManagerAPI:
    """Handles file operations directly without Node.js backend"""
    
    def __init__(self, base_url=None,parent_window=None):
        # base_url parameter kept for compatibility but not used
        # All operations are now local
        self.base_url = base_url
        self.parent_window = parent_window  
        pass
    
    def read_directory(self, path):
        """Read directory contents"""
        try:

            
            # Handle Windows-specific path formatting
            if sys.platform == 'win32':
                if len(path) == 2 and path[1] == ':':
                    path = path + '\\'
                
                # Handle network paths - return network placeholder
                if path == "\\\\":
                    return [{
                        'name': 'Network',
                        'path': '\\\\',
                        'isDirectory': True,
                        'size': 0,
                        'modified': 0,
                        'created': 0,
                        'accessed': 0
                    }]
            
            # Handle drive roots on Windows
            if sys.platform == 'win32' and len(path) == 3 and path[1] == ':':
                path = path[:-1]
            
            # Get directory contents from file service
            data = file_service.read_directory(path)
            
            # Add created/accessed times for compatibility
            for item in data:
                try:
                    stats = os.stat(item['path'])
                    item['created'] = stats.st_ctime * 1000
                    item['accessed'] = stats.st_atime * 1000
                    # Convert modified time to match expected format
                    if isinstance(item['modified'], str):
                        from datetime import datetime
                        dt = datetime.fromisoformat(item['modified'].replace('Z', '+00:00'))
                        item['modified'] = dt.timestamp() * 1000
                    else:
                        item['modified'] = stats.st_mtime * 1000
                except Exception:
                    # Fallback if stat fails
                    item['created'] = item.get('modified', 0)
                    item['accessed'] = item.get('modified', 0)
            if not self.parent_window.show_hidden:  # Access parent window's state
                data = [item for item in data if not item['name'].startswith('.')]
      
            return data
            
        except Exception as e:
            raise Exception(f"Failed to read directory: {str(e)}")
    
    def search_files(self, path, term):
        """Search for files containing the term"""
        try:
            return file_service.search_files(path, term)
        except Exception as e:
            raise Exception(f"Search failed: {str(e)}")
    
    def create_folder(self, path, name):
        """Create a new folder"""
        try:
            new_path = file_service.create_folder(path, name)
            return {"path": new_path, "success": True}
        except Exception as e:
            raise Exception(f"Failed to create folder: {str(e)}")
    
    def delete_item(self, path):
        """Delete a file or folder"""
        try:
            file_service.delete_item(path)
            return {"success": True}
        except Exception as e:
            raise Exception(f"Failed to delete item: {str(e)}")
    
    def rename_item(self, old_path, new_name):
        """Rename a file or folder"""
        try:
            new_path = file_service.rename_item(old_path, new_name)
            return {"path": new_path, "success": True}
        except Exception as e:
            raise Exception(f"Failed to rename item: {str(e)}")
    
    def copy_item(self, source_path, destination_dir):
        """Copy a file or folder"""
        try:
            new_path = file_service.copy_item(source_path, destination_dir)
            return {"path": new_path, "success": True}
        except Exception as e:
            raise Exception(f"Failed to copy item: {str(e)}")
    
    def move_item(self, source_path, destination_dir):
        """Move a file or folder"""
        try:
            new_path = file_service.move_item(source_path, destination_dir)
            return {"path": new_path, "success": True}
        except Exception as e:
            raise Exception(f"Failed to move item: {str(e)}")
    
    def get_home_dir(self):
        """Get the user's home directory"""
        try:
            return file_service.get_home_directory()
        except Exception as e:
            raise Exception(f"Failed to get home directory: {str(e)}")
    
    def open_file(self, path):
        """Open a file with the default system application"""
        try:
            success = file_service.open_file(path)
            if not success:
                raise Exception("Failed to open file with default application")
        except Exception as e:
            raise Exception(f"Failed to open file: {str(e)}")
    
    # Additional methods that might be used by your GUI
    
    def bulk_operation(self, operation, sources, destination):
        """Perform bulk operations on multiple files"""
        try:
            return file_service.bulk_operation(operation, sources, destination)
        except Exception as e:
            raise Exception(f"Bulk operation failed: {str(e)}")
    
    def copy_items(self, source_paths, destination_dir):
        """Copy multiple items"""
        try:
            results = file_service.copy_items(source_paths, destination_dir)
            return {"paths": results, "success": True}
        except Exception as e:
            raise Exception(f"Failed to copy items: {str(e)}")
    
    def move_items(self, source_paths, destination_dir):
        """Move multiple items"""
        try:
            results = file_service.move_items(source_paths, destination_dir)
            return {"paths": results, "success": True}
        except Exception as e:
            raise Exception(f"Failed to move items: {str(e)}")
    
    def clipboard_operation(self, operation, items, destination=None):
        """Handle clipboard operations"""
        try:
            return file_service.clipboard_operation(operation, items, destination)
        except Exception as e:
            raise Exception(f"Clipboard operation failed: {str(e)}")
    
    def health_check(self):
        """Health check - always returns OK since we're running locally"""
        from datetime import datetime
        return {
            "status": "OK", 
            "timestamp": datetime.now().isoformat()
        }

# For backward compatibility, you can also create a function that returns the API instance
def get_api_client():
    """Get the file manager API client"""
    return FileManagerAPI()