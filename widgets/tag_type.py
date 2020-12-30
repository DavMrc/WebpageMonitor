from PyQt5.QtWidgets import QComboBox


class TagType(QComboBox):
	name = "tag_inp"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(TagType.name)

		items = [i.strip() for i in open('./possible-tags.txt', 'r').readlines()]
		self.addItems(items)
