from PySide6.QtCore import Qt, QMimeData,QPoint
from PySide6.QtGui import QDrag,QPixmap,QPainter,QColor
from PySide6.QtWidgets import QApplication

class DragDropMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setProperty('dragOver', False)
    
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()
    
    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return
        
        if not hasattr(self, 'drag_start_position'):
            return
        
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        
        selected_items = self.get_selected_files()
        if not selected_items:
            return
        
        drag = QDrag(self)
        mime_data = QMimeData()

        paths = [item['path'] for item in selected_items]
        mime_data.setText("\n".join(paths))
        
        
        try:
            from Config.styles import COLORS  
            
            pixmap = QPixmap(48, 48)
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            
           
            if len(selected_items) > 1:
                bg_color = QColor(COLORS['primary'])
                bg_color.setAlpha(200) 
                icon_color = QColor(COLORS['text']) 
                text = str(len(selected_items))
            else:
                if selected_items[0].get('isDirectory', False):
                    bg_color = QColor(COLORS['primary'])
                    bg_color.setAlpha(100)
                    icon_color = QColor(COLORS['primary']).darker(120)
                    text = "📁"
                else:
                    bg_color = QColor(COLORS['primary'])
                    bg_color.setAlpha(200)
                    icon_color = QColor(COLORS['text'])
                    text = "📄"
            
            painter.setBrush(bg_color)
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(0, 0, 48, 48, 8, 8)
            
            
            text_color = QColor(COLORS['text'])
            painter.setPen(text_color)
            
            painter.setPen(icon_color)
            font = painter.font()
            font.setBold(True)
            font.setPointSize(14)
            painter.setFont(font)
            
            painter.drawText(pixmap.rect(), Qt.AlignCenter, text)
            painter.end()
        except Exception as e:
            print(f"Error creating drag icon: {str(e)}")
            
            pixmap = None

        drag.setMimeData(mime_data)
        if pixmap:
            drag.setPixmap(pixmap)
            drag.setHotSpot(QPoint(24, 24))
        
        drag.exec(Qt.DropAction.MoveAction | Qt.DropAction.CopyAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            self.setProperty('dragOver', True)
            self.style().unpolish(self)
            self.style().polish(self)
            event.acceptProposedAction()
        else:
            event.ignore()
    
    def dragMoveEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            event.ignore()
    
    def dragLeaveEvent(self, event):
        self.setProperty('dragOver', False)
        self.style().unpolish(self)
        self.style().polish(self)
        event.accept()
    
    def dropEvent(self, event):
        self.setProperty('dragOver', False)
        self.style().unpolish(self)
        self.style().polish(self)
        
        if event.mimeData().hasText():
            # Determine drop target path
            target_path = self.parent_window.current_path
            
            # Check if dropped on a folder item
            item_at_drop = self.itemAt(event.pos())
            if item_at_drop:
                row = item_at_drop.row()
                name_item = self.item(row, 0)
                if name_item:
                    file_info = name_item.data(Qt.ItemDataRole.UserRole)
                    if file_info and file_info['isDirectory']:
                        target_path = file_info['path']
            
            paths = event.mimeData().text().split('\n')
            
            
            if event.keyboardModifiers() & Qt.KeyboardModifier.ControlModifier:
                
                for path in paths:
                    self.parent_window.copy_item(path, target_path)
            else:
                
                for path in paths:
                    self.parent_window.move_item(path, target_path)
            
            event.acceptProposedAction()
        else:
            event.ignore()
    
    def get_selected_files(self):
        """Get selected files from the table"""
        selected = []
        for row in range(self.rowCount()):
            item = self.item(row, 0)
            if item and item.isSelected():
                file_info = item.data(Qt.ItemDataRole.UserRole)
                if file_info:
                    selected.append(file_info)
        return selected