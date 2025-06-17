import os
import shutil
import subprocess
import platform
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

class FileService:
    """
    Python implementation of file operations to replace the Node.js backend
    """
    
    def __init__(self):
        self.platform = platform.system().lower()
    
    def read_directory(self, dir_path: str) -> List[Dict[str, Any]]:
        """
        Read directory contents and return detailed file information
        """
        try:
            # Handle Windows drive paths
            if self.platform == 'windows':
                if len(dir_path) == 2 and dir_path[1] == ':':
                    dir_path += '\\'
                # Handle network paths
                if dir_path.startswith('\\\\') and dir_path.count('\\') == 2:
                    dir_path += '\\'
            
            path_obj = Path(dir_path)
            if not path_obj.exists():
                raise FileNotFoundError(f"Path not found: {dir_path}")
            
            items = []
            for item in path_obj.iterdir():
                try:
                    stat = item.stat()
                    items.append({
                        'name': item.name,
                        'path': str(item),
                        'isDirectory': item.is_dir(),
                        'size': stat.st_size,
                        'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                    })
                except (PermissionError, OSError) as e:
                    # Skip items we can't access
                    print(f"Warning: Cannot access {item}: {e}")
                    continue
            
            # Sort directories first, then files
            items.sort(key=lambda x: (not x['isDirectory'], x['name'].lower()))
            return items
            
        except Exception as e:
            raise self._handle_error(e)
    
    def search_files(self, base_path: str, term: str, depth: int = 3, current_depth: int = 0) -> List[Dict[str, Any]]:
        """
        Search for files and directories containing the search term
        """
        results = []
        
        if current_depth > depth:
            return results
        
        try:
            path_obj = Path(base_path)
            if not path_obj.exists() or not path_obj.is_dir():
                return results
            
            for item in path_obj.iterdir():
                try:
                    if item.name.lower().startswith(term.lower()):
                        stat = item.stat()
                        results.append({
                            'name': item.name,
                            'path': str(item),
                            'isDirectory': item.is_dir(),
                            'size': stat.st_size,
                            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                        })
                    
                    # Recursively search subdirectories
                    if item.is_dir():
                        sub_results = self.search_files(str(item), term, depth, current_depth + 1)
                        results.extend(sub_results)
                        
                except (PermissionError, OSError):
                    # Skip items we can't access
                    continue
            
            return results
            
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def create_folder(self, base_path: str, name: str) -> str:
        """
        Create a new folder
        """
        try:
            new_path = Path(base_path) / name
            new_path.mkdir(exist_ok=False)
            return str(new_path)
        except Exception as e:
            raise self._handle_error(e)
    
    def delete_item(self, item_path: str) -> None:
        """
        Delete a file or directory
        """
        try:
            path_obj = Path(item_path)
            if path_obj.is_dir():
                shutil.rmtree(path_obj)
            else:
                path_obj.unlink()
        except Exception as e:
            raise self._handle_error(e)
    
    def rename_item(self, old_path: str, new_name: str) -> str:
        """
        Rename a file or directory
        """
        try:
            old_path_obj = Path(old_path)
            new_path = old_path_obj.parent / new_name
            old_path_obj.rename(new_path)
            return str(new_path)
        except Exception as e:
            raise self._handle_error(e)
    
    def copy_item(self, source_path: str, destination_dir: str) -> str:
        """
        Copy a file or directory
        """
        try:
            source = Path(source_path)
            dest_dir = Path(destination_dir)
            destination = dest_dir / source.name
            
            if source.is_dir():
                shutil.copytree(source, destination)
            else:
                shutil.copy2(source, destination)
            
            return str(destination)
        except Exception as e:
            raise self._handle_error(e)
    
    def move_item(self, source_path: str, destination_dir: str) -> str:
        """
        Move a file or directory
        """
        try:
            source = Path(source_path)
            dest_dir = Path(destination_dir)
            destination = dest_dir / source.name
            
            shutil.move(source, destination)
            return str(destination)
        except Exception as e:
            raise self._handle_error(e)
    
    def get_home_directory(self) -> str:
        """
        Get the user's home directory
        """
        return str(Path.home())
    
    def open_file(self, file_path: str) -> bool:
        """
        Open a file with the system's default application
        """
        try:
            if self.platform == 'darwin':  # macOS
                subprocess.run(['open', file_path], check=True)
            elif self.platform == 'windows':
                os.startfile(file_path)
            else:  # Linux and others
                subprocess.run(['xdg-open', file_path], check=True)
            return True
        except Exception as e:
            print(f"Error opening file: {e}")
            return False
    
    def bulk_operation(self, operation: str, sources: List[str], destination: str) -> Dict[str, Any]:
        """
        Perform bulk operations on multiple files/directories
        """
        results = []
        errors = []
        
        for source_path in sources:
            try:
                if operation == 'copy':
                    result = self.copy_item(source_path, destination)
                elif operation == 'move':
                    result = self.move_item(source_path, destination)
                elif operation == 'delete':
                    self.delete_item(source_path)
                    result = source_path
                else:
                    raise ValueError(f"Unknown operation: {operation}")
                
                results.append(result)
                
            except Exception as e:
                errors.append({'path': source_path, 'error': str(e)})
        
        return {
            'success': True,
            'results': results,
            'errors': errors if errors else None
        }
    
    def copy_items(self, source_paths: List[str], destination_dir: str) -> List[str]:
        """
        Copy multiple items
        """
        try:
            results = []
            for source_path in source_paths:
                result = self.copy_item(source_path, destination_dir)
                results.append(result)
            return results
        except Exception as e:
            raise self._handle_error(e)
    
    def move_items(self, source_paths: List[str], destination_dir: str) -> List[str]:
        """
        Move multiple items
        """
        try:
            results = []
            for source_path in source_paths:
                result = self.move_item(source_path, destination_dir)
                results.append(result)
            return results
        except Exception as e:
            raise self._handle_error(e)
    
    def clipboard_operation(self, operation: str, items: List[Dict[str, str]], destination: Optional[str] = None) -> Dict[str, Any]:
        """
        Handle clipboard operations (copy/cut/paste)
        """
        results = []
        errors = []
        
        if operation == 'paste' and destination:
            for item in items:
                try:
                    if item['operation'] == 'copy':
                        result = self.copy_item(item['path'], destination)
                    elif item['operation'] == 'cut':
                        result = self.move_item(item['path'], destination)
                    else:
                        continue
                    results.append(result)
                except Exception as e:
                    errors.append({'path': item['path'], 'error': str(e)})
        
        return {
            'success': True,
            'results': results,
            'errors': errors if errors else None
        }
    
    def _handle_error(self, error: Exception) -> Exception:
        """
        Handle and convert errors to user-friendly messages
        """
        print(f"File operation error: {error}")
        
        if isinstance(error, PermissionError):
            return Exception("Permission denied")
        elif isinstance(error, FileNotFoundError):
            return Exception("Path not found")
        elif isinstance(error, FileExistsError):
            return Exception("File or folder already exists")
        else:
            return Exception("Operation failed")


# Global instance to be used by the GUI
file_service = FileService()