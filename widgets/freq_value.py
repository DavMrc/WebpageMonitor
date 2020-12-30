from PyQt5.QtWidgets import QSpinBox


class FreqValue(QSpinBox):
	name = "freq_val"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(FreqValue.name)
		self.setMinimum(1)
