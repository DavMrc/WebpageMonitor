from PyQt5.QtWidgets import QSpinBox


class FreqVal(QSpinBox):
	name = "freq_val"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(FreqVal.name)
		self.setMinimum(1)
