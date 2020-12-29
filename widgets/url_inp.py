from os import name
from PyQt5.QtWidgets import QLineEdit


class UrlInput(QLineEdit):
	name = "url_inp"

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setObjectName(UrlInput.name)
		self.setPlaceholderText("http://")
