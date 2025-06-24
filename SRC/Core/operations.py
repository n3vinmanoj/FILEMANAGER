import os
import sys
from datetime import datetime
from PySide6.QtCore import Qt, QTimer,QSize
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QToolBar, QStatusBar, 
    QProgressBar, QDialog, QApplication,QListWidgetItem,QToolButton,QListWidget,QAbstractItemView
)
from send2trash import send2trash  # Add this import at the top
from PySide6.QtGui import QAction
from Services.api import FileManagerAPI
from .worker import WorkerThread
from Core.table_widget import FileListWidget
from .Dialogs.dialogs import CreateFolderDialog, RenameDialog, PropertiesDialog
from UI.py.Main_ui import Ui_MainWindow
from Utils.shortcuts import setup_shortcuts
from Utils.formatters import format_size
from Utils.icons import get_icon, get_file_type
from Config.styles import get_success_color, get_error_color
from Core.Dialogs.recycle_bin_dialog import RecycleBinDialog

class FileManagerWindow(QMainWindow, Ui_MainWindow):
    """Main file manager window with all business logic"""
    def __init__(self):
        try:
            print("Initializing FileManagerWindow...")
            super().__init__()
            print("✓ Super initialization complete")
            
            self.setupUi(self)
            print("✓ UI setup complete")

            self.setMinimumSize(900, 700)
            
            self.api = FileManagerAPI(parent_window=self) 
            print("✓ API initialized")
            
            self.current_path = ""
            self.clipboard = None
            self.worker_threads = []
            self.undo_stack = []
            self.history_index=-1
            self.history = []
            
            print("Initializing UI components...")
            self.init_ui()
            print("✓ UI components initialized")
            
            print("Setting up shortcuts...")
            setup_shortcuts(self)
            print("✓ Shortcuts setup complete")
            
            # print("Checking server connection...")
            # self.check_server_connection()
            # print("✓ Server check complete")
            
            print("Loading home directory...")
            self.load_home_directory()
            print("✓ Home directory load initiated")

            self.current_view = "list"  # 'list' or 'icon'
            self.icon_size = "medium"
            
            self.show_hidden=False
            print("FileManagerWindow initialization complete!")
            
        except Exception as e:
            print(f"❌ Error during FileManagerWindow initialization: {e}")
            
            QMessageBox.critical(
                None, 
                "Initialization Error", 
                f"Failed to initialize File Manager:\n\n{str(e)}\n\n"
                f"See console for details."
            )
            sys.exit(1)
    
    def mousePressEvent(self, event):
    # Only clear if we're not clicking on a file item or sidebar item
        if not self.file_list.underMouse() and not self.sidebarFrame.underMouse():
            self.file_list.clearSelection()
            if hasattr(self, "icon_view_widget"):
                self.icon_view_widget.clearSelection()

        # Also clear selection in sidebar lists
        self.placesList.clearSelection()
        self.devicesList.clearSelection()

        # Force immediate UI update
        self.file_list.viewport().update()
        if hasattr(self, "icon_view_widget"):
            self.icon_view_widget.viewport().update()

        super().mousePressEvent(event)
        
    def init_ui(self):
        self.verticalLayout_3.removeWidget(self.file_list)
        self.file_list.deleteLater()
        
        # Replace file_list with custom widget
        self.file_list = FileListWidget(self.centralwidget,parent_window=self)
        self.file_list.setObjectName("file_list")
        self.verticalLayout_3.addWidget(self.file_list, 1)
        
        # Connect signals
        self.placesList.itemClicked.connect(self.on_place_clicked)
        self.devicesList.itemClicked.connect(self.on_device_clicked)
        self.backButton.clicked.connect(self.go_back)
        self.homeButton.clicked.connect(self.go_home)
        self.address_input.returnPressed.connect(self.navigate_from_address)
        self.go_button.clicked.connect(self.navigate_from_address)
        self.search_input.returnPressed.connect(self.search_files)
        self.search_button.clicked.connect(self.search_files)
        #self.clear_search_button.clicked.connect(self.clear_search)
        self.refresh_button.clicked.connect(self.refresh)
        self.new_folder_button.clicked.connect(self.create_folder)
        self.upButton.clicked.connect(self.go_up)
        self.forwardButton.clicked.connect(self.go_forward)

        self.hidden_toggle = self.findChild(QToolButton, "hidden_toggle")
        self.hidden_toggle.toggled.connect(self.toggle_hidden_files)

        self.placesList.itemClicked.connect(lambda _: self.file_list.clearSelection())
        self.devicesList.itemClicked.connect(lambda _: self.file_list.clearSelection())

        
        self.itemCountLabel.setText("Items: 0")

        self.populate_sidebar()
        
        # Status bar setup
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.statusBar.addPermanentWidget(self.progress_bar)

        self.icon_view_widget = QListWidget(self.centralwidget)
        self.icon_view_widget.setObjectName(u"icon_view_widget")
        self.icon_view_widget.setViewMode(QListWidget.IconMode)
        self.icon_view_widget.setResizeMode(QListWidget.Adjust)
        self.icon_view_widget.setSpacing(10)
        self.icon_view_widget.setWordWrap(True)
        self.icon_view_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.icon_view_widget.itemDoubleClicked.connect(self.on_icon_double_click)
        self.verticalLayout_3.addWidget(self.icon_view_widget)
        self.icon_view_widget.hide()

# Connect view actions
        self.actionList_View = self.findChild(QAction, "actionList_View")
        self.actionIcon_View = self.findChild(QAction, "actionIcon_View")
        self.actionSmall_Icons = self.findChild(QAction, "actionSmall_Icons")
        self.actionMedium_Icons = self.findChild(QAction, "actionMedium_Icons")

        self.actionList_View.triggered.connect(self.switch_to_list_view)
        self.actionIcon_View.triggered.connect(self.switch_to_icon_view)
        self.actionSmall_Icons.triggered.connect(lambda: self.set_icon_size("small"))
        self.actionMedium_Icons.triggered.connect(lambda: self.set_icon_size("medium"))

# Disable icon size options initially
        self.actionSmall_Icons.setEnabled(False)
        self.actionMedium_Icons.setEnabled(False)

        self.file_list.setFocus()

        self.file_list.selectionModel().selectionChanged.connect(self.update_selected_count)
        self.icon_view_widget.itemSelectionChanged.connect(self.update_selected_count)


    def switch_to_list_view(self):
        self.current_view = "list"
        self.icon_view_widget.hide()
        self.file_list.show()
    
    # Update menu states
        self.actionList_View.setChecked(True)
        self.actionIcon_View.setChecked(False)
        self.actionSmall_Icons.setEnabled(False)
        self.actionMedium_Icons.setEnabled(False)
    
    # Set focus to file list
        self.file_list.setFocus()
        self.refresh(force=True)

        self.update_selected_count()

    def switch_to_icon_view(self):
        self.current_view = "icon"
        self.file_list.hide()
        self.icon_view_widget.show()
    
    # Update menu states
        self.actionIcon_View.setChecked(True)
        self.actionList_View.setChecked(False)
        self.actionSmall_Icons.setEnabled(True)
        self.actionMedium_Icons.setEnabled(True)
    
    # Apply current icon size
        if self.icon_size == "small":
            self.icon_view_widget.setIconSize(QSize(24, 24))
            self.icon_view_widget.setGridSize(QSize(80, 70))
        else:  # medium
            self.icon_view_widget.setIconSize(QSize(32, 32))
            self.icon_view_widget.setGridSize(QSize(100, 80))
    
    # Set focus to icon view
        self.icon_view_widget.setFocus()
        self.refresh(force=True)

        self.update_selected_count()

    def set_icon_size(self, size):
        self.icon_size = size
        if self.current_view == "icon":
            if size == "small":
                self.icon_view_widget.setIconSize(QSize(24, 24))
                self.icon_view_widget.setGridSize(QSize(80, 70))
                self.actionSmall_Icons.setChecked(True)
                self.actionMedium_Icons.setChecked(False)
            else:  # medium
                self.icon_view_widget.setIconSize(QSize(32, 32))
                self.icon_view_widget.setGridSize(QSize(100, 80))
                self.actionSmall_Icons.setChecked(False)
                self.actionMedium_Icons.setChecked(True)
            self.refresh()

    def on_icon_double_click(self, item):
        file_info = item.data(Qt.UserRole)
        if file_info:
            if file_info['isDirectory']:
                self.navigate_to_path(file_info['path'])
            else:
                self.open_file(file_info['path'])

    def populate_icon_view(self, files):
        self.icon_view_widget.clear()
        for file_info in files:
            item = QListWidgetItem()
            item.setText(file_info['name'])
            item.setIcon(get_icon(file_info))
            item.setData(Qt.UserRole, file_info)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignTop)
            self.icon_view_widget.addItem(item)
    
    # Set uniform item sizes for grid alignment
        self.icon_view_widget.setUniformItemSizes(True)

    def update_selected_count(self):
        """Update the selected items count display"""
        if self.current_view == "list":
            selected_count = len(self.file_list.selectionModel().selectedRows())
        else:
            selected_count = len(self.icon_view_widget.selectedItems())
    
        self.selectedCountLabel.setText(f"Selected: {selected_count}")

    def toggle_hidden_files(self, checked):
        self.show_hidden = checked
        self.refresh(force=True)
    def populate_sidebar(self):
        home_path = os.path.expanduser("~")
        home_path = os.path.expanduser("~")
        places = [
            ("🏠 Home", home_path),
            ("🖥️ Desktop", os.path.join(home_path, "Desktop")),
            ("📄 Documents", os.path.join(home_path, "Documents")),
            ("📥 Downloads", os.path.join(home_path, "Downloads")),
            ("🎵 Music", os.path.join(home_path, "Music")),
            ("🖼️ Pictures", os.path.join(home_path, "Pictures")),
            ("🎬 Videos", os.path.join(home_path, "Videos")),
            ("🗑️ Trash", os.path.join(home_path, "Trash"))  # Linux trash location
        ]

    # Clear existing items and add new ones
        self.placesList.clear()
        for name, path in places:
            #if os.path.exists(path):  # Only add if path exists
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole, path)
            self.placesList.addItem(item)

    # Get available drives (Windows)
        if sys.platform == 'win32':
            import string
            drives = []
            for letter in string.ascii_uppercase:
                path = f"{letter}:\\"
                if os.path.exists(path):
                    drives.append((f"{letter}: Drive", path))
        
        # Add network drives if any
            if os.path.exists("\\\\"):
                drives.append(("Network", "\\\\"))
        else:  # Linux/Mac
            drives = [
            ("File System", "/"),
            ("Home", home_path)
            ]
        # Add media directories if they exist
            for media_dir in ['/media', '/mnt', '/Volumes']:
                if os.path.exists(media_dir):
                    drives.append(("Removable Media", media_dir))

    # Add devices
        self.devicesList.clear()
        for name, path in drives:
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole, path)
            self.devicesList.addItem(item)

    def on_place_clicked(self, item):
        """Handle clicks on places in sidebar"""
        path = item.data(Qt.UserRole)
        if path:
            if "Trash" in item.text():
                self.open_recycle_bin()
            else:
                self.navigate_to_path(path)
    
    def open_recycle_bin(self):
        """Open the custom recycle bin dialog."""
        dialog = RecycleBinDialog(self)
        dialog.exec()

    def on_device_clicked(self, item):
        """Handle clicks on devices in sidebar"""
        path = item.data(Qt.UserRole)
        if path:
            self.navigate_to_path(path)

    def go_forward(self):
        """Navigate forward in history"""
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            path = self.history[self.history_index]
            self.navigate_to_path(path, add_to_history=False)

    def go_up(self):
        """Navigate to parent directory"""
        if self.current_path:
            parent_path = os.path.dirname(self.current_path)
            if parent_path != self.current_path:  # Prevent infinite loop at root
                self.navigate_to_path(parent_path)

    def create_worker_thread(self, func, *args, **kwargs):
        thread = WorkerThread(func, *args, **kwargs)
        self.worker_threads.append(thread)
        thread.finished.connect(lambda: self.cleanup_thread(thread))
        return thread

    def cleanup_thread(self, thread):
        if thread in self.worker_threads:
            self.worker_threads.remove(thread)
            thread.deleteLater()

    def closeEvent(self, event):
        for thread in self.worker_threads:
            if thread.isRunning():
                thread.wait()
        super().closeEvent(event)

    # def check_server_connection(self):
    #     try:
    #         response = requests.get(f"{self.api.base_url}/api/health", timeout=2)
    #         if response.status_code == 200:
    #             print("✓ Connected to backend server")
    #         else:
    #             self.show_connection_error()
    #     except requests.RequestException:
    #         self.show_connection_error()

    # def show_connection_error(self):
    #     QMessageBox.critical(
    #         self, 
    #         "Connection Error", 
    #         "Cannot connect to the backend server.\n\n"
    #         "Please make sure the Node.js server is running:\n"
    #         "node server.js\n\n"
    #         "Server should be running on http://localhost:8080"
    #     )
    
    def set_loading(self, loading):
        self.progress_bar.setVisible(loading)
        if loading:
            self.progress_bar.setRange(0, 0)
        self.file_list.setEnabled(not loading)
    
    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)
        self.statusBar.showMessage(f"Error: {message}", 5000)
    
    def show_success(self, message):
        self.statusBar.showMessage(message, 3000)
    
    def load_home_directory(self):
        self.set_loading(True)
        thread = self.create_worker_thread(self.api.get_home_dir)
        thread.finished.connect(self.on_home_dir_loaded)
        thread.error.connect(self.on_api_error)
        thread.start()
    
    def on_home_dir_loaded(self, home_path):
        self.set_loading(False)
        self.navigate_to_path(home_path)
    
    def navigate_to_path(self, path, add_to_history=True):
        """Navigate to a path with history management"""
        if not os.path.exists(path):
            self.show_error(f"Path does not exist: {path}")
            return
        
        if self.current_path == path:
            return
        if add_to_history:
       
            if self.history_index < len(self.history) - 1:
                self.history = self.history[:self.history_index+1]
        
            self.history.append(path)
            self.history_index = len(self.history) - 1
    
    
        #self.backButton.setEnabled(self.history_index > 0)
        #self.forwardButton.setEnabled(self.history_index < len(self.history) - 1)
        self.update_navigation_buttons()
    
        self.set_loading(True)
        thread = self.create_worker_thread(self.api.read_directory, path)
        thread.finished.connect(lambda files: self.on_directory_loaded(files, path))
        thread.error.connect(self.on_api_error)
        thread.start()

    def update_navigation_buttons(self):
        """Update back/forward button states based on history"""
        self.backButton.setEnabled(self.history_index > 0)
        self.forwardButton.setEnabled(self.history_index < len(self.history) - 1)

    def on_directory_loaded(self, files, path):
        self.set_loading(False)
        self.current_path = path
        self.address_input.setText(path)
    
        if self.current_view == "list":
            self.file_list.populate_files(files)
        else:
            self.populate_icon_view(files)
        
        self.itemCountLabel.setText(f"Items: {len(files)}")
        #self.backButton.setEnabled(bool(path and path != "/"))
        self.update_navigation_buttons()
        self.show_success(f"Loaded {len(files)} items")
        self.update_selected_count()
    
    # Set focus to current view
        if self.current_view == "list":
            self.file_list.setFocus()
        else:
            self.icon_view_widget.setFocus()
    
    def navigate_from_address(self):
        path = self.address_input.text().strip()
        if path:
            self.navigate_to_path(path)
    
    def go_back(self):
        if self.history_index > 0:
            self.history_index -= 1
            path = self.history[self.history_index]
            self.navigate_to_path(path, add_to_history=False)
    
    def go_home(self):
        self.load_home_directory()
    
    def refresh(self, force=False):
        """Refresh current directory with optional force parameter"""
        if self.current_path:
        # Only clear the view AFTER we have new data (removed immediate clearing)
            if force:
                temp_path = self.current_path
                self.current_path = ""
                self.navigate_to_path(temp_path, add_to_history=False)
            else:
                self.navigate_to_path(self.current_path, add_to_history=False)
        
        # Keep focus without explicit clearing
            if self.current_view == "list":
                self.file_list.setFocus()
            else:
                self.icon_view_widget.setFocus()
    
    def search_files(self):
        search_term = self.search_input.text().strip()
        if search_term and self.current_path:
            self.set_loading(True)
            thread = self.create_worker_thread(self.api.search_files, self.current_path, search_term)
            thread.finished.connect(lambda files: self.on_search_results(files, search_term))
            thread.error.connect(self.on_api_error)
            thread.start()
    
    def on_search_results(self, files, search_term):
        self.set_loading(False)
    
        if self.current_view == "list":
            self.file_list.populate_files(files)
        else:
            self.populate_icon_view(files)
        
        self.show_success(f"Found {len(files)} items matching '{search_term}'")
        self.update_selected_count()
    
    # Set focus to current view
        if self.current_view == "list":
            self.file_list.setFocus()
        else:
            self.icon_view_widget.setFocus()
    
    def clear_search(self):
        self.search_input.clear()
        self.refresh()
    
    def create_folder(self):
        dialog = CreateFolderDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            folder_name = dialog.get_folder_name()
            if folder_name:
                self.set_loading(True)
                thread = self.create_worker_thread(self.api.create_folder, self.current_path, folder_name)
                thread.finished.connect(lambda: self.on_folder_created(folder_name))
                thread.error.connect(self.on_api_error)
                thread.start()
    
    def on_folder_created(self, folder_name):
        self.set_loading(False)
        self.show_success(f"Created folder '{folder_name}'")
        self.refresh(force=True)
    
    def rename_item(self, file_info):
        dialog = RenameDialog(file_info['name'], self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_name = dialog.get_new_name()
            if new_name and new_name != file_info['name']:
                self.set_loading(True)
                thread = self.create_worker_thread(self.api.rename_item, file_info['path'], new_name)
                thread.finished.connect(lambda: self.on_item_renamed(file_info['path'], file_info['name'], new_name))
                thread.error.connect(self.on_api_error)
                thread.start()
    
    def on_item_renamed(self, path, old_name, new_name):
        self.set_loading(False)
        self.show_success(f"Renamed '{old_name}' to '{new_name}'")
        self.add_to_undo_stack({
            'type': 'rename',
            'old_path': path,
            'new_path': os.path.join(os.path.dirname(path), new_name),
            'old_name': old_name,
            'new_name': new_name
        })
        self.refresh(force=True)
    


# operations.py
    def delete_selected(self):
        selected_files = self.file_list.get_selected_files()
        if not selected_files:
            return

        if len(selected_files) == 1:
            message = f"Are you sure you want to delete '{selected_files[0]['name']}'?"
        else:
            message = f"Are you sure you want to delete {len(selected_files)} items?"
            message += "\n\nSelected items:"
            for i, file in enumerate(selected_files[:5]):
                message += f"\n• {file['name']}"
            if len(selected_files) > 5:
                message += f"\n• ... and {len(selected_files) - 5} more"
        message += "\n\nItems will be moved to Trash."

        msg_box = QMessageBox(
            QMessageBox.Icon.Question,
            "Confirm Delete",
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            self
        )
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        msg_box.setEscapeButton(QMessageBox.StandardButton.No)
        msg_box.setWindowModality(Qt.WindowModality.ApplicationModal)

        if msg_box.exec() == QMessageBox.StandardButton.Yes:
            self.set_loading(True)
            total_files = len(selected_files)
            completed = 0

            def on_delete_complete():
                nonlocal completed
                completed += 1
                if completed == total_files:
                    self.set_loading(False)
                    self.show_success(f"Moved {total_files} item{'s' if total_files > 1 else ''} to Trash")
                    self.refresh(force=True)

            for file_info in selected_files:
                # Use API's delete_item instead of send2trash directly
                thread = self.create_worker_thread(self.api.delete_item, file_info['path'])
                thread.finished.connect(on_delete_complete)
                thread.error.connect(lambda e, name=file_info['name']: self.handle_delete_error(str(e), name))
                thread.start()

    def handle_delete_error(self, error_message, item_name):
        self.show_error(f"Error deleting '{item_name}': {error_message}")
    
    def copy_selected(self):
        selected_files = self.file_list.get_selected_files()
        if not selected_files:
            return
    
        self.set_loading(True)
        paths = [file['path'] for file in selected_files]
    
        if len(selected_files) == 1:
            self.clipboard = {"path": paths[0], "operation": "copy"}
            self.show_success("Item copied to clipboard")
        else:
            self.clipboard = {
            "paths": paths,
            "operation": "copy"
            }
            self.show_success(f"{len(selected_files)} items copied to clipboard")
        self.set_loading(False)
    
    def cut_selected(self):
        selected_files = self.file_list.get_selected_files()
        if not selected_files:
            return
    
        self.set_loading(True)
        paths = [file['path'] for file in selected_files]
    
        if len(selected_files) == 1:
            self.clipboard = {"path": paths[0], "operation": "cut"}
            self.show_success("Item cut to clipboard")
        else:
            self.clipboard = {
            "paths": paths,
            "operation": "cut"
            }
            self.show_success(f"{len(selected_files)} items cut to clipboard")
        self.set_loading(False)

    
    
    def add_to_undo_stack(self, operation):
    
        if operation['type'] == 'rename':
            restructured = {
            'type': 'rename',
            'source_path': operation['old_path'],
            'dest_path': operation['new_path'],
            'old_name': operation['old_name'],
            'new_name': operation['new_name']
            }
        elif operation['type'] in ['copy', 'move']:
            restructured = {
                'type': operation['type'],
                'source_path': operation['source_path'],
                'dest_path': operation['dest_path']
            }
        else:
        
            restructured = operation
    
        self.undo_stack.append(restructured)
        if len(self.undo_stack) > 20:
            self.undo_stack.pop(0)

    
    def undo_last_operation(self):
        if not self.undo_stack:
            self.show_success("Nothing to undo")
            return

        operation = self.undo_stack.pop()
        self.set_loading(True)

        try:
            if operation['type'] == 'rename':
            
                thread = self.create_worker_thread(
                    self.api.rename_item,
                    operation['dest_path'],  
                    operation['old_name']   
                )
                thread.finished.connect(lambda: self.on_undo_complete("Rename undone"))
                thread.error.connect(self.on_api_error)
                thread.start()

            elif operation['type'] == 'copy':
            
                if isinstance(operation['dest_path'], list):
                
                    dest_paths = operation['dest_path']
                    total = len(dest_paths)
                    completed = [0]  
                    def on_delete_complete():
                        completed[0] += 1
                        if completed[0] == total:
                            self.on_undo_complete(f"Copied {total} item{'s' if total > 1 else ''} removed")

                    for path in dest_paths:
                        thread = self.create_worker_thread(
                            self.api.delete_item,
                            path
                        )
                        thread.finished.connect(on_delete_complete)
                        thread.error.connect(self.on_api_error)
                        thread.start()
                else:
                
                    thread = self.create_worker_thread(
                        self.api.delete_item,
                        operation['dest_path']
                    )
                    thread.finished.connect(lambda: self.on_undo_complete("Copied item removed"))
                    thread.error.connect(self.on_api_error)
                    thread.start()

            elif operation['type'] == 'move':
            
                if isinstance(operation['source_path'], list):
                
                    source_paths = operation['source_path']
                    dest_paths = operation['dest_path']
                    total = len(source_paths)
                    completed = [0]

                    def on_move_complete():
                        completed[0] += 1
                        if completed[0] == total:
                            self.on_undo_complete(f"Moved {total} item{'s' if total > 1 else ''} restored")

                    for source, dest in zip(source_paths, dest_paths):
                        thread = self.create_worker_thread(
                            self.api.move_item,
                            dest,  
                            os.path.dirname(source)  
                        )
                        thread.finished.connect(on_move_complete)
                        thread.error.connect(self.on_api_error)
                        thread.start()
                else:
                
                    thread = self.create_worker_thread(
                        self.api.move_item,
                        operation['dest_path'],  
                        os.path.dirname(operation['source_path'])  
                    )
                    thread.finished.connect(lambda: self.on_undo_complete("Moved item restored"))
                    thread.error.connect(self.on_api_error)
                    thread.start()

            elif operation['type'] == 'delete':
           
                self.set_loading(False)
                self.show_error("Cannot undo delete operation")
                return

        except Exception as e:
            self.set_loading(False)
            self.show_error(f"Failed to undo: {str(e)}")
    
    def on_undo_complete(self, message):
        self.set_loading(False)
        self.show_success(message)
        self.refresh(force=True)
    
    
    def on_copy_completed(self, source_paths, dest_paths):
        self.set_loading(False)
    
   
        if isinstance(source_paths, list):
            count = len(source_paths)
            self.show_success(f"Copied {count} item{'s' if count > 1 else ''}")
            self.add_to_undo_stack({
            'type': 'copy',
            'source_path': source_paths,
            'dest_path': dest_paths
            })
        else:
        
            self.show_success(f"Copied {os.path.basename(source_paths)}")
            self.add_to_undo_stack({
            'type': 'copy',
            'source_path': source_paths,
            'dest_path': dest_paths
            })
    
        self.refresh()

    def on_move_completed(self, source_paths, dest_paths):
        self.set_loading(False)
    
    
        if isinstance(source_paths, list):
            count = len(source_paths)
            self.show_success(f"Moved {count} item{'s' if count > 1 else ''}")
            self.add_to_undo_stack({
            'type': 'move',
            'source_path': source_paths,
            'dest_path': dest_paths
        })
        else:
       
            self.show_success(f"Moved {os.path.basename(source_paths)}")
            self.add_to_undo_stack({
            'type': 'move',
            'source_path': source_paths,
            'dest_path': dest_paths
            })
    
        self.refresh()
    def paste_item(self):
        if not self.clipboard:
            self.show_error("Nothing to paste")
            return

        self.set_loading(True)
        source_paths = []
        dest_paths = []

    # Store clipboard reference BEFORE potentially clearing it
        clipboard_data = self.clipboard
    
        if clipboard_data.get("operation") == "cut":
            self.clipboard = None  # Clear clipboard for cut operation

    # Use clipboard_data instead of self.clipboard for all checks
        if "paths" in clipboard_data:
            paths = clipboard_data["paths"]
            operation = clipboard_data["operation"]
    
            for path in paths:
                dest_path = os.path.join(self.current_path, os.path.basename(path))
                source_paths.append(path)
                dest_paths.append(dest_path)
        
                thread = self.create_worker_thread(
                self.api.copy_item if operation == "copy" else self.api.move_item,
                path, 
                self.current_path
                )
                thread.finished.connect(lambda s=path, d=dest_path: None)
                thread.error.connect(self.on_api_error)
                thread.start()
    
            QTimer.singleShot(500, lambda: self.on_paste_complete(
                source_paths, 
                dest_paths, 
                operation
            ))

        else:
            path = clipboard_data["path"]
            operation = clipboard_data["operation"]
            dest_path = os.path.join(self.current_path, os.path.basename(path))
    
            thread = self.create_worker_thread(
                self.api.copy_item if operation == "copy" else self.api.move_item,
                path,
                self.current_path
            )
            thread.finished.connect(lambda: self.on_paste_complete(
                [path], 
                [dest_path], 
                operation
            ))
            thread.error.connect(self.on_api_error)
            thread.start()

    def on_paste_complete(self, source_paths, dest_paths, operation):
        self.set_loading(False)
        count = len(source_paths)
    
        self.add_to_undo_stack({
        'type': 'move' if operation == "cut" else 'copy',
        'source_path': source_paths,
        'dest_path': dest_paths
        })
    
    
        if count > 1:
            self.show_success(f"Pasted {count} items")
        else:
            self.show_success(f"Pasted {os.path.basename(source_paths[0])}")
    
    
        if operation == "cut":
            self.clipboard = None
    
        self.refresh(force=True)
    def open_file(self, path):
        thread = self.create_worker_thread(self.api.open_file, path)
        thread.finished.connect(lambda: self.show_success("File opened"))
        thread.error.connect(self.on_api_error)
        thread.start()
    
    def move_item(self, source_path, destination_dir):
        self.set_loading(True)
        dest_path = os.path.join(destination_dir, os.path.basename(source_path))
        
        thread = self.create_worker_thread(self.api.move_item, source_path, destination_dir)
        thread.finished.connect(lambda: self.on_move_completed(source_path, dest_path))
        thread.error.connect(self.on_api_error)
        thread.start()
    
    def on_move_completed(self, source_path, dest_path):
        self.set_loading(False)
        self.show_success(f"Moved {os.path.basename(source_path)}")
        self.add_to_undo_stack({
            'type' : 'move',
            'source_path': source_path,
            'dest_path': dest_path
        })
        self.refresh()
    
    def handle_move_items(self, source_paths, destination_dir):
        if isinstance(source_paths, list):
            for path in source_paths:
                self.move_item(path, destination_dir)
        else:
            self.move_item(source_paths, destination_dir)
    
    def show_properties(self):
        selected_files = self.file_list.get_selected_files()
        if len(selected_files) == 1:
            dialog = PropertiesDialog(selected_files[0], self)
            dialog.exec()
    
    def on_api_error(self, error_message):
        self.set_loading(False)
        self.show_error(error_message)