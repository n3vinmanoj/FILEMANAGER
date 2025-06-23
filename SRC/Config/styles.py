"""
Modern styling for PyQt6 File Manager application - Neutral Clean Design
"""


COLORS = {
    'primary': '#6b7280',        # Neutral gray - subdued but visible
    'primary_hover': '#9ca3af',  # Lighter gray on hover
    'primary_light': '#d1d5db',  # Light gray
    'primary_dark': '#4b5563',   # Darker gray
    'secondary': '#6b7280',      # Medium gray
    'background': '#1a1a1a',     # Dark background like Linux
    'surface': '#2a2a2a',        # Dark surface
    'surface_hover': '#3a3a3a',  # Hover state
    'surface_light': '#242424',  # Slightly lighter surface
    'text': '#e5e5e5',           # Light text on dark
    'text_secondary': '#b5b5b5', # Medium gray text
    'text_muted': '#888888',     # Muted gray text
    'success': '#6b7280',        # Neutral gray
    'warning': '#6b7280',        # Neutral gray
    'error': '#6b7280',          # Neutral gray
    'border': '#404040',         # Dark border
    'border_light': '#353535',   # Lighter dark border
    'border_subtle': '#4a4a4a',  # Subtle border
    'drag_over':'#6b728020',     # Subtle overlay
    'selection': '#6b728025',    # Subtle selection
    'keyboard_focus': '#6b728015', # Barely visible focus
    'divider': '#404040',        # Dark divider
}


MAIN_STYLE = f"""
QMainWindow {{
    background-color: {COLORS['background']};
    color: {COLORS['text']};
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 400;
}}

/* Toolbar Styling - Ultra minimal */
QToolBar {{
    background-color: {COLORS['surface_light']};
    border: none;
    border-bottom: 1px solid {COLORS['border']};
    padding: 8px;
    spacing: 8px;
}}

* {{
    outline: none !important;
    border: none !important;
}}

*::focus {{
    outline: none !important;
}}

QpushButton:focus, QLineEdit:focus {{
    outline: none !important;
    border: none !important;
}}

QTableWidget::item:focus {{
    outline: none;
    show-decoration-selected: 0;
}}

QToolBar QAction {{
    padding: 8px 16px;
    margin: 0 4px;
    border-radius: 8px;
    background: transparent;
    color: {COLORS['text']};
}}

QToolBar QAction:hover {{
    background-color: {COLORS['surface_hover']};
}}

/* Button Styling - Soft rounded */
QPushButton {{
    background-color: {COLORS['primary']};
    color: white;
    border: none;
    padding: 10px 16px;
    border-radius: 12px;
    font-weight: 500;
    min-width: 80px;
    font-size: 13px;
}}

QPushButton:hover {{
    background-color: {COLORS['primary_hover']};
}}

QPushButton:pressed {{
    background-color: {COLORS['primary_dark']};
}}

QPushButton:disabled {{
    background-color: {COLORS['secondary']};
    color: {COLORS['text_secondary']};
}}

/* Navigation buttons - Soft and neutral */
QPushButton#backButton, QPushButton#homeButton {{
    min-width: 40px;
    padding: 8px;
    border-radius: 10px;
    font-size: 16px;
    background-color: {COLORS['surface']};
    color: {COLORS['text_secondary']};
    border: 1px solid {COLORS['border']};
}}

QPushButton#backButton:hover, QPushButton#homeButton:hover {{
    background-color: {COLORS['surface_hover']};
    color: {COLORS['text']};
    border-color: {COLORS['border_subtle']};
}}

/* Input Fields - Soft with gentle borders */
QLineEdit {{
    background-color: {COLORS['surface_light']};
    border: 1px solid {COLORS['border']};
    border-radius: 10px;
    padding: 10px 12px;
    color: {COLORS['text']};
    font-size: 14px;
    font-weight: 400;
}}

QLineEdit:focus {{
    border-color: {COLORS['border_subtle']};
    background-color: {COLORS['surface']};
    outline: none !important;
}}

QLineEdit::placeholder {{
    color: {COLORS['text_muted']};
    font-style: normal;
}}

/* Table Widget - Less blocky, more flowing */
QTableWidget {{
    background-color: {COLORS['surface_light']};
    border: 1px solid {COLORS['border']};
    border-radius: 16px;
    gridline-color: transparent;
    selection-background-color: {COLORS['selection']};
    alternate-background-color: {COLORS['surface']};
    show-decoration-selected: 0;
}}

QTableWidget::item {{
    padding: 16px 12px;
    color: {COLORS['text']};
    border: none;
    outline: none;
    font-weight: 400;
    border-bottom: 1px solid {COLORS['border_light']};
}}

QTableWidget::item:focus {{
    outline: none !important;
    border: none !important;
    background-color: {COLORS['selection']};
    color: {COLORS['text']};
    border-bottom: 1px solid {COLORS['border_light']};
}}

QTableWidget::item:selected {{
    background-color: {COLORS['selection']};
    color: {COLORS['text']};
    outline: none;
    border-bottom: 1px solid {COLORS['border_light']};
}}

QTableWidget::item:hover {{
    background-color: {COLORS['surface_hover']};
    border-bottom: 1px solid {COLORS['border_light']};
}}

QTableWidget::item:selected:focus {{
    outline: none !important;
    border: none !important;
    background-color: {COLORS['selection']};
    color: {COLORS['text']};
    border-bottom: 1px solid {COLORS['border_light']};
}}

/* Header - Soft and minimal */
QHeaderView::section {{
    background-color: {COLORS['surface']};
    color: {COLORS['text_secondary']};
    padding: 16px 12px;
    border: none;
    border-bottom: 1px solid {COLORS['border']};
    border-right: 1px solid {COLORS['border_light']};
    font-weight: 500;
    font-size: 13px;
}}

QHeaderView::section:hover {{
    background-color: {COLORS['surface_hover']};
}}

QHeaderView::section:focus {{
    outline: none !important;
}}

QHeaderView::section:last {{
    border-right: none;
}}

/* Scrollbars - Nearly invisible */
QScrollBar:vertical {{
    background-color: transparent;
    width: 8px;
    border-radius: 4px;
    margin: 0;
}}

QScrollBar::handle:vertical {{
    background-color: {COLORS['border_subtle']};
    border-radius: 4px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background-color: {COLORS['secondary']};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    border: none;
    background: none;
}}

/* Status Bar - Ultra minimal */
QStatusBar {{
    background-color: {COLORS['surface_light']};
    border-top: 1px solid {COLORS['border']};
    color: {COLORS['text_secondary']};
    padding: 4px 8px;
    font-size: 12px;
}}

/* Progress Bar - Soft and neutral */
QProgressBar {{
    background-color: {COLORS['surface']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    text-align: center;
    color: {COLORS['text']};
    height: 20px;
    font-weight: 500;
}}

QProgressBar::chunk {{
    background-color: {COLORS['primary']};
    border-radius: 7px;
}}

/* Menu Styling - Soft and flowing */
QMenu {{
    background-color: {COLORS['surface_light']};
    border: 1px solid {COLORS['border']};
    border-radius: 12px;
    padding: 8px;
    color: {COLORS['text']};
}}

QMenu::item {{
    padding: 12px 16px;
    border-radius: 8px;
    margin: 2px;
    font-weight: 400;
}}

QMenu::item:selected {{
    background-color: {COLORS['surface_hover']};
    color: {COLORS['text']};
}}

QMenu::separator {{
    height: 1px;
    background-color: {COLORS['border']};
    margin: 8px 0;
}}
"""

SIDEBAR_STYLE = f"""
/* Sidebar styling - Soft and minimal */
QFrame#sidebarFrame {{
    background-color: {COLORS['surface']};
    border-right: 1px solid {COLORS['border']};
    min-width: 170px;
    max-width: 170px;
}}

/* Section headers - Soft typography */
QFrame#sidebarFrame QLabel {{
    color: {COLORS['text_muted']};
    font-weight: 600;
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 12px 12px 4px 12px !important;
    margin: 0;
    background-color: transparent;
    min-height: 12px;
    max-height: 12px;
}}

/* List widgets - Soft and flowing */
QFrame#sidebarFrame QListWidget {{
    background-color: transparent;
    border: none;
    outline: none;
    color: {COLORS['text']};
    font-size: 11px;
    font-weight: 500;
    padding: 0;
    margin: 0 8px 12px 8px;
    spacing: 2px;
}}

/* List items - Soft rounded */
QFrame#sidebarFrame QListWidget::item {{
    padding: 8px 12px;
    border-radius: 8px;
    margin: 1px 0;
    min-height: 12px;
    max-height: 24px;
    color: {COLORS['text']};
    background-color: transparent;
    border: none;
    font-weight: 400;
}}

/* Hover state - Very subtle */
QFrame#sidebarFrame QListWidget::item:hover {{
    background-color: {COLORS['surface_hover']};
    color: {COLORS['text']};
}}

/* Selected state - Soft */
QFrame#sidebarFrame QListWidget::item:selected {{
    background-color: {COLORS['selection']};
    color: {COLORS['text']};
    font-weight: 500;
}}

/* Selected and not active */
QFrame#sidebarFrame QListWidget::item:selected:!active {{
    background-color: {COLORS['selection']};
    color: {COLORS['text']};
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

/* Device list special styling - Ultra subtle */
QFrame#sidebarFrame QListWidget#devicesList::item {{
    font-size: 10px;
    color: {COLORS['text_muted']};
    max-height: 20px;
}}

QFrame#sidebarFrame QListWidget#devicesList::item:hover {{
    color: {COLORS['text']};
}}

QFrame#sidebarFrame QListWidget#devicesList::item:selected {{
    color: {COLORS['text']};
}}

/* Force specific heights for lists to prevent scrolling */
QFrame#sidebarFrame QListWidget#placesList {{
    max-height: 270px;
    min-height: 270px;
}}

QFrame#sidebarFrame QListWidget#devicesList {{
    max-height: 200px;
    min-height: 200px;
}}
"""

DRAG_DROP_STYLE = f"""
/* Drag and Drop styling - Very subtle */
QTableWidget[dragOver="true"] {{
    background-color: {COLORS['drag_over']};
    border: 2px dashed {COLORS['border_subtle']};
}}

QTableWidget::item:drag {{
    background-color: {COLORS['surface']};
    border: 1px solid {COLORS['border_subtle']};
    border-radius: 8px;
    opacity: 0.8;
}}

QTableWidget::item:selected {{
    background-color: {COLORS['selection']};
    border: none;
}}

/* Keyboard focus indicators - Barely visible */
QTableWidget::item:focus {{
    background-color: {COLORS['keyboard_focus']};
    border: none;
}}

/* Selection styling - Ultra soft */
QTableWidget::item:selected:active {{
    background-color: {COLORS['selection']};
    color: {COLORS['text']};
}}

QTableWidget::item:selected:!active {{
    background-color: {COLORS['surface_hover']};
    color: {COLORS['text']};
}}
"""

# Dialog styling - Soft and neutral
DIALOG_STYLE = f"""
QDialog {{
    background-color: {COLORS['surface_light']};
    color: {COLORS['text']};
    border: 1px solid {COLORS['border']};
    border-radius: 16px;
}}

QDialogButtonBox QPushButton {{
    min-width: 100px;
    padding: 8px 16px;
    border-radius: 10px;
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
    background-color: {COLORS['surface_light']};
    color: {COLORS['text']};
    border-radius: 12px;
}}

QMessageBox QPushButton {{
    min-width: 80px;
    padding: 6px 12px;
    border-radius: 8px;
}}

QMessageBox QLabel {{
    color: {COLORS['text']};
    font-weight: 400;
}}
"""
ICON_VIEW_STYLE = f"""
/* Icon View Item Styling */
QListWidget#icon_view_widget::item {{
    min-width: 100px;
    max-width: 120px;
    min-height: 80px;
    margin: 10px;
}}

QListWidget#icon_view_widget::item[iconsize="small"] {{
    min-width: 80px;
    max-width: 100px;
    min-height: 70px;
    margin: 10px;
}}
"""

TOOLBAR_STYLE = f"""
/* Toolbar View Button Styling */
QToolBar QToolButton {{
    background-color: transparent;
    border: 1px solid transparent;
    border-radius: 4px;
    padding: 4px;
}}

QToolBar QToolButton:hover {{
    background-color: {COLORS['surface_hover']};
    border: 1px solid {COLORS['border_subtle']};
}}
"""

def apply_styles(app):
    """Apply the complete stylesheet to the application"""
    complete_style = MAIN_STYLE + DIALOG_STYLE + MESSAGE_BOX_STYLE + DRAG_DROP_STYLE + SIDEBAR_STYLE + ICON_VIEW_STYLE + TOOLBAR_STYLE
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