from PySide6.QtCore import QThread, Signal

class WorkerThread(QThread):
    """Background thread for API calls"""
    finished = Signal(object)
    error = Signal(str)
    
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None
    
    def run(self):
        try:
            self.result = self.func(*self.args, **self.kwargs)
            self.finished.emit(self.result)
        except Exception as e:
            self.error.emit(str(e))