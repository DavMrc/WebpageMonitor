from PyQt5.QtWidgets import QLabel, QSizePolicy


class FreqLabel(QLabel):
	name = "freq_label"
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setObjectName(FreqLabel.name)
		self.setText("Frequency check")

		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
