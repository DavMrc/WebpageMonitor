from PyQt5.QtWidgets import QLabel, QSizePolicy


class TagLab(QLabel):
	name = "tag_lab"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(TagLab.name)
		self.setText("Tag:")

		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
