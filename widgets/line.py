from PyQt5.QtWidgets import QFrame


class Line(QFrame):
	def __init__(self, parent):
		super().__init__(parent=parent)

		self.setFrameShape(QFrame.HLine)
		self.setFrameShadow(QFrame.Sunken)
