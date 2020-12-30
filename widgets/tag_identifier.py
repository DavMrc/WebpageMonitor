from PyQt5.QtWidgets import QComboBox

class TagIdentifier(QComboBox):
	name = "id_class_type"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(TagIdentifier.name)

		types = ['id', 'class']
		self.addItems(types)
