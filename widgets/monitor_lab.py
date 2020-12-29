from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtGui import QFont


class MonitorLab(QLabel):
	name = "monitor_webpage_lab"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(MonitorLab.name)
		self.setText("Monitor a webpage")

		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)

		font = QFont()
		font.setPointSize(22)
		self.setFont(font)
