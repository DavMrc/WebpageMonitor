from PyQt5.QtCore import QThread, pyqtSignal


class MThread(QThread):
	signal = pyqtSignal(str)

	def __init__(self, on_html_tag_changed: callable, parent=None):
		super().__init__(parent=parent)
		self.on_html_tag_changed = on_html_tag_changed

	def run(self):
		htmltag = self.on_html_tag_changed()
		self.signal.emit(htmltag)