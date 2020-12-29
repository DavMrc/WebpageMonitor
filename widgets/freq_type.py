from PyQt5.QtWidgets import QComboBox

class FreqType(QComboBox):
	name = "freq_type"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(FreqType.name)

		types = ['seconds', 'minutes', 'hours']
		self.addItems(types)
