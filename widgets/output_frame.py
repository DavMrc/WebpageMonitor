from PyQt5.QtWidgets import QTextEdit, QHBoxLayout


class OutputText(QTextEdit):
	name = 'output_frame'

	def __init__(self, parent, output: str):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(OutputText.name)

		self.output = output
		self.insertPlainText(output)

		self.setReadOnly(True)


class OutputFrame(QHBoxLayout):
	def __init__(self, parent, output: str):
		super().__init__()
		output_text = OutputText(parent=parent, output=output)

		self.addWidget(output_text)
