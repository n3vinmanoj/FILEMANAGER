from PySide6.QtWidgets import QApplication, QStyle
from PySide6.QtGui import QIcon
import os

# Map extensions to custom icon file paths
CUSTOM_ICON_PATHS = {
    '.py': 'Utils/icons/python.png',
    '.pdf': 'Utils/icons/PDF.png',
    '.js': 'Utils/icons/JS.png',
    '.html': 'Utils/icons/HTML.png',
    '.css': 'Utils/icons/CSS.png',
    '.img' or '.jpg' or '.jpeg' or '.png': 'Utils/icons/IMG.png',
    '.java': 'Utils/icons/JAVA.png',
    '.iso': 'Utils/icons/ISO.png'
    # Add more as needed
}

def get_icon(file_info):
    """Get appropriate icon for file/folder"""
    app = QApplication.instance()
    style = app.style()

    if file_info['isDirectory']:
        return style.standardIcon(QStyle.StandardPixmap.SP_DirIcon)

    name = file_info['name']
    _, ext = os.path.splitext(name)
    ext = ext.lower()

    # Use custom icon if available
    if ext in CUSTOM_ICON_PATHS and os.path.exists(CUSTOM_ICON_PATHS[ext]):
        return QIcon(CUSTOM_ICON_PATHS[ext])

    # Fallback to standard icons
    icon_map = {
        '.txt': QStyle.StandardPixmap.SP_FileIcon,
        '.pdf': QStyle.StandardPixmap.SP_FileDialogDetailedView,
        '.doc': QStyle.StandardPixmap.SP_FileDialogContentsView,
        '.docx': QStyle.StandardPixmap.SP_FileDialogContentsView,
        '.xls': QStyle.StandardPixmap.SP_FileDialogInfoView,
        '.xlsx': QStyle.StandardPixmap.SP_FileDialogInfoView,
        '.jpg': QStyle.StandardPixmap.SP_FileDialogContentsView,
        '.jpeg': QStyle.StandardPixmap.SP_FileDialogContentsView,
        '.png': QStyle.StandardPixmap.SP_FileDialogContentsView,
        '.gif': QStyle.StandardPixmap.SP_FileDialogContentsView,
        '.mp3': QStyle.StandardPixmap.SP_MediaVolume,
        '.mp4': QStyle.StandardPixmap.SP_MediaPlay,
        '.py': QStyle.StandardPixmap.SP_FileDialogDetailedView,
        '.js': QStyle.StandardPixmap.SP_FileDialogDetailedView,
        '.html': QStyle.StandardPixmap.SP_BrowserReload,
        '.css': QStyle.StandardPixmap.SP_BrowserReload,
        '.zip': QStyle.StandardPixmap.SP_DirIcon,
        '.rar': QStyle.StandardPixmap.SP_DirIcon,
        '.exe': QStyle.StandardPixmap.SP_ComputerIcon,
    }

    return style.standardIcon(icon_map.get(ext, QStyle.StandardPixmap.SP_FileIcon))
def get_file_type(file_info):
    """Get file type based on extension"""
    name = file_info['name']
    ext = os.path.splitext(name)[1].lower()
    
    types = {
        '.txt': 'Text Document',
        '.pdf': 'PDF Document',
        '.doc': 'Word Document',
        '.docx': 'Word Document',
        '.xls': 'Excel Spreadsheet',
        '.xlsx': 'Excel Spreadsheet',
        '.jpg': 'JPEG Image',
        '.jpeg': 'JPEG Image',
        '.png': 'PNG Image',
        '.gif': 'GIF Image',
        '.mp3': 'MP3 Audio',
        '.mp4': 'MP4 Video',
        '.py': 'Python Script',
        '.js': 'JavaScript File',
        '.html': 'HTML Document',
        '.css': 'CSS File',
        '.zip': 'ZIP Archive',
        '.rar': 'RAR Archive',
        '.exe': 'Executable File'
    }
    
    return types.get(ext, f"{ext[1:].upper()} File" if ext else "File")