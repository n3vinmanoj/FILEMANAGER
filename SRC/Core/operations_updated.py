# Replace your existing HTTP-based operations with these direct calls
# This assumes you have the FileService class imported as file_service

import traceback
from PySide6.QtWidgets import QMessageBox
from file_service import file_service  # Import the file service

class FileOperations:
    """
    File operations using local Python implementation instead of HTTP backend
    """
    
    @staticmethod
    def show_error(parent, title, message):
        """Show error dialog"""
        QMessageBox.critical(parent, title, message)
    
    @staticmethod
    def show_info(parent, title, message):
        """Show info dialog"""
        QMessageBox.information(parent, title, message)
    
    def read_directory(self, path, parent_widget=None):
        """Read directory contents"""
        try:
            return file_service.read_directory(path)
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to read directory: {str(e)}")
            return []
    
    def search_files(self, base_path, term, parent_widget=None):
        """Search for files"""
        try:
            return file_service.search_files(base_path, term)
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Search failed: {str(e)}")
            return []
    
    def create_folder(self, base_path, name, parent_widget=None):
        """Create a new folder"""
        try:
            new_path = file_service.create_folder(base_path, name)
            if parent_widget:
                self.show_info(parent_widget, "Success", f"Folder created: {name}")
            return new_path
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to create folder: {str(e)}")
            return None
    
    def delete_item(self, item_path, parent_widget=None):
        """Delete a file or folder"""
        try:
            file_service.delete_item(item_path)
            if parent_widget:
                self.show_info(parent_widget, "Success", "Item deleted successfully")
            return True
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to delete item: {str(e)}")
            return False
    
    def rename_item(self, old_path, new_name, parent_widget=None):
        """Rename a file or folder"""
        try:
            new_path = file_service.rename_item(old_path, new_name)
            if parent_widget:
                self.show_info(parent_widget, "Success", f"Renamed to: {new_name}")
            return new_path
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to rename item: {str(e)}")
            return None
    
    def copy_item(self, source_path, destination_dir, parent_widget=None):
        """Copy a file or folder"""
        try:
            new_path = file_service.copy_item(source_path, destination_dir)
            if parent_widget:
                self.show_info(parent_widget, "Success", "Item copied successfully")
            return new_path
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to copy item: {str(e)}")
            return None
    
    def move_item(self, source_path, destination_dir, parent_widget=None):
        """Move a file or folder"""
        try:
            new_path = file_service.move_item(source_path, destination_dir)
            if parent_widget:
                self.show_info(parent_widget, "Success", "Item moved successfully")
            return new_path
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to move item: {str(e)}")
            return None
    
    def get_home_directory(self):
        """Get home directory"""
        try:
            return file_service.get_home_directory()
        except Exception as e:
            print(f"Error getting home directory: {e}")
            return "/"  # fallback
    
    def open_file(self, file_path, parent_widget=None):
        """Open file with default application"""
        try:
            success = file_service.open_file(file_path)
            if not success and parent_widget:
                self.show_error(parent_widget, "Error", "Failed to open file")
            return success
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to open file: {str(e)}")
            return False
    
    def bulk_operation(self, operation, sources, destination, parent_widget=None):
        """Perform bulk operations"""
        try:
            result = file_service.bulk_operation(operation, sources, destination)
            
            # Show results
            if parent_widget:
                message = f"Operation completed:\n"
                message += f"Successful: {len(result['results'])}\n"
                if result['errors']:
                    message += f"Failed: {len(result['errors'])}\n"
                    message += "Errors:\n"
                    for error in result['errors'][:3]:  # Show first 3 errors
                        message += f"- {error['path']}: {error['error']}\n"
                    if len(result['errors']) > 3:
                        message += f"... and {len(result['errors']) - 3} more errors"
                
                if result['errors']:
                    self.show_error(parent_widget, "Bulk Operation", message)
                else:
                    self.show_info(parent_widget, "Success", message)
            
            return result
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Bulk operation failed: {str(e)}")
            return None
    
    def copy_items(self, source_paths, destination_dir, parent_widget=None):
        """Copy multiple items"""
        try:
            results = file_service.copy_items(source_paths, destination_dir)
            if parent_widget:
                self.show_info(parent_widget, "Success", f"Copied {len(results)} items")
            return results
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to copy items: {str(e)}")
            return None
    
    def move_items(self, source_paths, destination_dir, parent_widget=None):
        """Move multiple items"""
        try:
            results = file_service.move_items(source_paths, destination_dir)
            if parent_widget:
                self.show_info(parent_widget, "Success", f"Moved {len(results)} items")
            return results
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Failed to move items: {str(e)}")
            return None
    
    def clipboard_operation(self, operation, items, destination=None, parent_widget=None):
        """Handle clipboard operations"""
        try:
            result = file_service.clipboard_operation(operation, items, destination)
            
            if parent_widget and operation == 'paste':
                message = f"Paste completed:\n"
                message += f"Successful: {len(result['results'])}\n"
                if result['errors']:
                    message += f"Failed: {len(result['errors'])}"
                
                if result['errors']:
                    self.show_error(parent_widget, "Paste Operation", message)
                else:
                    self.show_info(parent_widget, "Success", message)
            
            return result
        except Exception as e:
            if parent_widget:
                self.show_error(parent_widget, "Error", f"Clipboard operation failed: {str(e)}")
            return None


# Example of how to update your FileManagerWindow class
class FileManagerWindow:
    def __init__(self):
        # ... your existing initialization code ...
        
        # Replace HTTP client with file operations
        self.file_ops = FileOperations()
        
        # Initialize to home directory
        self.current_path = self.file_ops.get_home_directory()
        self.refresh_directory()
    
    def refresh_directory(self):
        """Refresh the current directory listing"""
        try:
            files = self.file_ops.read_directory(self.current_path, self)
            # Update your UI with the files list
            self.update_file_list(files)
        except Exception as e:
            print(f"Error refreshing directory: {e}")
    
    def navigate_to(self, path):
        """Navigate to a specific path"""
        self.current_path = path
        self.refresh_directory()
    
    def create_folder(self, name):
        """Create a new folder"""
        new_path = self.file_ops.create_folder(self.current_path, name, self)
        if new_path:
            self.refresh_directory()
    
    def delete_selected(self):
        """Delete selected items"""
        selected_paths = self.get_selected_paths()  # Your method to get selected items
        for path in selected_paths:
            self.file_ops.delete_item(path, self)
        self.refresh_directory()
    
    def search_files(self, term):
        """Search for files"""
        results = self.file_ops.search_files(self.current_path, term, self)
        # Update your UI with search results
        self.update_search_results(results)
    
    # Add more methods as needed for your specific UI interactions
    
    def update_file_list(self, files):
        """Update the file list in your UI"""
        # Your implementation to update the UI
        pass
    
    def update_search_results(self, results):
        """Update search results in your UI"""
        # Your implementation to update search UI
        pass
    
    def get_selected_paths(self):
        """Get paths of selected items"""
        # Your implementation to get selected items
        return []
