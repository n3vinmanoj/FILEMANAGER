"""
Modern styling for PyQt6 File Manager application
"""


COLORS = {
    'primary': '#2563eb',        
    'primary_hover': '#1d4ed8',  
    'secondary': '#64748b',      
    'background': '#0f172a',     
    'surface': '#1e293b',       
    'surface_hover': '#334155',  
    'text': '#f8fafc',          
    'text_secondary': '#cbd5e1', 
    'success': '#10b981',       
    'warning': '#f59e0b',       
    'error': '#ef4444',          
    'border': '#475569',
    'drag_over':'#1e40af40',
    'selection': '#3b82f640',
    'keyboard_focus': '#60a5fa40',    
}


MAIN_STYLE = f"""
QMainWindow {{
    background-color: {COLORS['background']};
    color: {COLORS['text']};
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 14px;
}}

/* Toolbar Styling */
QToolBar {{
    background-color: {COLORS['surface']};
    border: none;
    border-bottom: 1px solid {COLORS['border']};
    padding: 8px;
    spacing: 8px;
}}

* {{
    outline: none  !important;
    border: none !important;
}}

*::focus {{
    outline: none !important;
}}

QpushButton:focus, QLineEdit:focus {{
    outline: none !important;
    border : none !important;
}}

QTableWidget::item:focus {{
    outline: none;
    show-decoration-selected: 0;
}}

QToolBar QAction {{
    padding: 8px 16px;
    margin: 0 4px;
    border-radius: 6px;
    background-color: transparent;
    color: {COLORS['text']};
}}

QToolBar QAction:hover {{
    background-color: {COLORS['surface_hover']};
}}

/* Button Styling */
QPushButton {{
    background-color: {COLORS['primary']};
    color: white;
    border: none;
    padding: 10px 16px;
    border-radius: 6px;
    font-weight: 500;
    min-width: 80px;
}}

QPushButton:hover {{
    background-color: {COLORS['primary_hover']};
}}

QPushButton:pressed {{
    background-color: #1e40af;
}}

QPushButton:disabled {{
    background-color: {COLORS['secondary']};
    color: {COLORS['text_secondary']};
}}

/* Navigation buttons */
QPushButton#backButton, QPushButton#homeButton {{
    min-width: 40px;
    padding: 8px;
    border-radius: 6px;
    font-size: 16px;
}}

/* Input Fields */
QLineEdit {{
    background-color: {COLORS['surface']};
    border: 1px solid {COLORS['border']};
    border-radius: 6px;
    padding: 10px 12px;
    color: {COLORS['text']};
    font-size: 14px;
}}

QLineEdit:focus {{
    border-color: {COLORS['primary']};
    outline: none !important;
}}

QLineEdit::placeholder {{
    color: {COLORS['text_secondary']};
}}

/* Table Widget */
QTableWidget {{
    background-color: {COLORS['surface']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    gridline-color: {COLORS['border']};
    selection-background-color: {COLORS['primary']};
    alternate-background-color: rgba(255, 255, 255, 0.05);
}}

QTableWidget::item {{
    padding: 12px 8px;
    color: {COLORS['text']};
    border: none;
    outline: none;
}}

QTableWidget::item:focus {{
    outline: none !important;
    border: none !important;
    background-color: {COLORS['primary']};
    color: white;
}}

QTableWidget::item:selected {{
    background-color: {COLORS['primary']};
    color: white;
    outline: none;
}}

QTableWidget::item:hover {{
    background-color: {COLORS['surface_hover']};
}}

QTableWidget::item:selected:focus {{
    outline: none !important;
    border: none !important;
    background-color: {COLORS['primary']};
    color: white;
}}

/* Header */
QHeaderView::section {{
    background-color: {COLORS['background']};
    color: {COLORS['text']};
    padding: 12px 8px;
    border: none;
    border-bottom: 2px solid {COLORS['border']};
    font-weight: 600;
}}

QHeaderView::section:hover {{
    background-color: {COLORS['surface_hover']};
}}

QHeaderView::section:focus {{
    outline: none !important;
}}

/* Scrollbars */
QScrollBar:vertical {{
    background-color: {COLORS['surface']};
    width: 12px;
    border-radius: 6px;
    margin: 0;
}}

QScrollBar::handle:vertical {{
    background-color: {COLORS['secondary']};
    border-radius: 6px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background-color: {COLORS['text_secondary']};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    border: none;
    background: none;
}}

/* Status Bar */
QStatusBar {{
    background-color: {COLORS['surface']};
    border-top: 1px solid {COLORS['border']};
    color: {COLORS['text_secondary']};
    padding: 4px 8px;
}}

/* Progress Bar */
QProgressBar {{
    background-color: {COLORS['surface']};
    border: 1px solid {COLORS['border']};
    border-radius: 4px;
    text-align: center;
    color: {COLORS['text']};
    height: 20px;
}}

QProgressBar::chunk {{
    background-color: {COLORS['primary']};
    border-radius: 3px;
}}

/* Menu Styling */
QMenu {{
    background-color: {COLORS['surface']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    padding: 4px;
    color: {COLORS['text']};
}}

QMenu::item {{
    padding: 8px 16px;
    border-radius: 4px;
    margin: 2px;
}}

QMenu::item:selected {{
    background-color: {COLORS['primary']};
    color: white;
}}

QMenu::separator {{
    height: 1px;
    background-color: {COLORS['border']};
    margin: 4px 0;
}}
"""

SIDEBAR_STYLE = f"""
/* Sidebar styling */
QFrame#sidebarFrame {{
    background-color: {COLORS['surface']};
    border-right: 1px solid {COLORS['border']};
    min-width: 170px;
    max-width: 170px;
}}

/* Section headers - much more compact */
QFrame#sidebarFrame QLabel {{
    color: {COLORS['text_secondary']};
    font-weight: 600;
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 8px 8px 2px 8px !important;
    margin: 0;
    background-color: transparent;
    min-height: 12px;
    max-height: 12px;
}}

/* List widgets - very compact */
QFrame#sidebarFrame QListWidget {{
    background-color: transparent;
    border: none;
    outline: none;
    color: {COLORS['text']};
    font-size: 11px;
    font-weight: 500;
    padding: 0;
    margin: 0 4px 8px 4px;
    spacing: 0;
}}

/* List items - minimal padding for compactness */
QFrame#sidebarFrame QListWidget::item {{
    padding: 6px 8px;
    border-radius: 4px;
    margin: 0;
    min-height: 12px;
    max-height: 24px;
    color: {COLORS['text']};
    background-color: transparent;
    border: none;
}}

/* Hover state */
QFrame#sidebarFrame QListWidget::item:hover {{
    background-color: {COLORS['surface_hover']};
    color: {COLORS['text']};
}}

/* Selected state */
QFrame#sidebarFrame QListWidget::item:selected {{
    background-color: {COLORS['primary']};
    color: white;
    font-weight: 600;
}}

/* Selected and not active */
QFrame#sidebarFrame QListWidget::item:selected:!active {{
    background-color: {COLORS['primary']};
    color: white;
    opacity: 0.8;
}}

/* Completely disable scrollbars */
QFrame#sidebarFrame QListWidget {{
    scrollbar-width: none;
}}

QFrame#sidebarFrame QListWidget::-webkit-scrollbar {{
    width: 0px;
    height: 0px;
}}

QFrame#sidebarFrame QListWidget::vertical-scrollbar,
QFrame#sidebarFrame QListWidget::horizontal-scrollbar {{
    width: 0px;
    height: 0px;
    background: transparent;
}}

QFrame#sidebarFrame QListWidget::vertical-scrollbar:handle,
QFrame#sidebarFrame QListWidget::horizontal-scrollbar:handle {{
    width: 0px;
    height: 0px;
    background: transparent;
}}

/* Focus styling */
QFrame#sidebarFrame QListWidget:focus {{
    outline: none;
    border: none;
}}

QFrame#sidebarFrame QListWidget::item:focus {{
    outline: none;
    border: none;
}}

/* Device list special styling - even more compact */
QFrame#sidebarFrame QListWidget#devicesList::item {{
    font-size: 10px;
    color: {COLORS['text_secondary']};
    max-height: 20px;
}}

QFrame#sidebarFrame QListWidget#devicesList::item:hover {{
    color: {COLORS['text']};
}}

QFrame#sidebarFrame QListWidget#devicesList::item:selected {{
    color: white;
}}

/* Force specific heights for lists to prevent scrolling */
QFrame#sidebarFrame QListWidget#placesList {{
    max-height: 230px;
    min-height: 230px;
}}

QFrame#sidebarFrame QListWidget#devicesList {{
    max-height: 200px;
    min-height: 200px;
}}
"""
DRAG_DROP_STYLE= f"""
/* Drag and Drop styling */
QTableWidget[dragOver="true"] {{
    background-color: {COLORS['drag_over']};
    border: 2px dashed {COLORS['primary']};
}}

QTableWidget::item:drag {{
    background-color: {COLORS['surface']};
    border: 1px solid {COLORS['primary']};
    border-radius: 4px;
    opacity: 0.8;
}}

QTableWidget::item:selected {{
    background-color: {COLORS['selection']};
    border: 1px solid {COLORS['primary']};
}}

/* Keyboard focus indicators */
QTableWidget::item:focus {{
    background-color: {COLORS['keyboard_focus']};
    border: 1px solid {COLORS['primary']};
}}

/* Selection styling */
QTableWidget::item:selected:active {{
    background-color: {COLORS['selection']};
    color: {COLORS['text']};
}}

QTableWidget::item:selected:!active {{
    background-color: {COLORS['surface_hover']};
    color: {COLORS['text']};
}}
"""


# Dialog styling
DIALOG_STYLE = f"""
QDialog {{
    background-color: {COLORS['surface']};
    color: {COLORS['text']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
}}

QDialogButtonBox QPushButton {{
    min-width: 100px;
    padding: 8px 16px;
}}

QLabel {{
    color: {COLORS['text']};
    font-weight: 500;
}}

QFormLayout QLabel {{
    color: {COLORS['text_secondary']};
}}
"""


MESSAGE_BOX_STYLE = f"""
QMessageBox {{
    background-color: {COLORS['surface']};
    color: {COLORS['text']};
}}

QMessageBox QPushButton {{
    min-width: 80px;
    padding: 6px 12px;
}}

QMessageBox QLabel {{
    color: {COLORS['text']};
}}
"""

def apply_styles(app):
    """Apply the complete stylesheet to the application"""
    complete_style = MAIN_STYLE + DIALOG_STYLE + MESSAGE_BOX_STYLE + DRAG_DROP_STYLE + SIDEBAR_STYLE
    app.setStyleSheet(complete_style)

def get_icon_color():
    """Return the appropriate color for icons"""
    return COLORS['text']

def get_success_color():
    """Return success color for status messages"""
    return COLORS['success']

def get_error_color():
    """Return error color for status messages"""
    return COLORS['error']