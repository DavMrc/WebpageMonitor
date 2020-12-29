from PyQt5.QtWidgets import QComboBox

class IdClassType(QComboBox):
	name = "id_class_type"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(IdClassType.name)

		types = ['id', 'class']
		self.addItems(types)
