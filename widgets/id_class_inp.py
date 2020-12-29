from PyQt5.QtWidgets import QLineEdit


class IdClassInput(QLineEdit):
	name = "id_class_inp"

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setObjectName(IdClassInput.name)
		self.setPlaceholderText("foo-bar")
