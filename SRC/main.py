import sys
import traceback
from PySide6.QtWidgets import QApplication, QMessageBox
from Core.operations import FileManagerWindow  # Import the actual GUI window class
from Config.styles import apply_styles

def main():
    app = QApplication(sys.argv)
    
    try:
        apply_styles(app)
        print("✓ Styles applied successfully")
    except Exception as e:
        print(f"⚠️  Warning: Could not apply styles: {e}")
    
    app.setApplicationName("File Manager")
    app.setApplicationVersion("1.0")
    print("✓ Application metadata set")
    
    try:
        print("Creating FileManagerWindow...")
        # Create the GUI window, not the FileOperations class
        window = FileManagerWindow()
        print("✓ FileManagerWindow created successfully")
        
        print("Showing window...")
        window.show()
        print("✓ Window shown")
        
        print("Starting application event loop...")
        sys.exit(app.exec())
        
    except Exception as e:
        print(f"❌ Error creating or showing window: {e}")
        print("Full traceback:")
        traceback.print_exc()
        
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setWindowTitle("Application Error")
        error_dialog.setText(f"Failed to start File Manager:\n\n{str(e)}")
        error_dialog.setDetailedText(traceback.format_exc())
        error_dialog.exec()

if __name__ == "__main__":
    main()