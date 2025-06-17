from PySide6.QtGui import QKeySequence,QShortcut
from PySide6.QtCore import Qt

def setup_shortcuts(window):
    copy_shortcut = QShortcut(QKeySequence.StandardKey.Copy, window)
    copy_shortcut.activated.connect(window.copy_selected)

    cut_shortcut = QShortcut(QKeySequence.StandardKey.Cut, window)
    cut_shortcut.activated.connect(window.cut_selected)

    paste_shortcut = QShortcut(QKeySequence.StandardKey.Paste, window)
    paste_shortcut.activated.connect(window.paste_item)

    delete_shortcut = QShortcut(QKeySequence.StandardKey.Delete, window)
    delete_shortcut.activated.connect(window.delete_selected)
    delete_shortcut.setContext(Qt.ShortcutContext.ApplicationShortcut)

    properties_shortcut = QShortcut(QKeySequence("Alt+Enter"), window)
    properties_shortcut.activated.connect(window.show_properties)
    properties_shortcut.setContext(Qt.ShortcutContext.ApplicationShortcut)

    undo_shortcut = QShortcut(QKeySequence.StandardKey.Undo, window)
    undo_shortcut.activated.connect(window.undo_last_operation)
    undo_shortcut.setContext(Qt.ShortcutContext.ApplicationShortcut)