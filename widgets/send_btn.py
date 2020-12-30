from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QSizePolicy, QMessageBox
from PyQt5.QtGui import QFont

from widgets.url_inp import UrlInput
from widgets.tag_type import TagType
from widgets.freq_value import FreqValue
from widgets.freq_type import FreqType
from widgets.tag_identifier import TagIdentifier
from widgets.tag_identifier_value import TagIdentifierValue
from widgets.result_lab import ResultLab

from checker import Checker
from params import Params
from monitor import Monitor


class SendBtn(QPushButton):
	name = "send_btn"

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setObjectName(SendBtn.name)
		self.setText("GO!")

		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)

		font = QFont()
		font.setPointSize(14)
		self.setFont(font)

		self.clicked.connect(self.on_press)
	
	def on_press(self):
		_findchild = self.parent.findChild  # for leaner code

		url = _findchild(UrlInput, UrlInput.name).text()
		tag_type = _findchild(TagType, TagType.name).currentText()
		tag_identifier = _findchild(TagIdentifier, TagIdentifier.name).currentText()
		tag_value = _findchild(TagIdentifierValue, TagIdentifierValue.name).text()
		freq_type = _findchild(FreqType, FreqType.name).currentText()
		freq_val = _findchild(FreqValue, FreqValue.name).value()

		if (
			Checker.url(url) and
			Checker.tag_type(tag_type) and
			Checker.tag_identifier(tag_identifier) and
			Checker.tag_value(tag_value) and
			Checker.freq_val(freq_val) and
			Checker.freq_type(freq_type)

		):
			# start monitoring
			params = Params({
				'url': url,
				'tag_type': tag_type,
				'tag_identifier': tag_identifier,
				'tag_value': tag_value,
				'freq_type': freq_type,
				'freq_val': freq_val,
			})
			monitor = Monitor(params)
			monitor.start_thread(self.on_html_tag_change)

			# insert result label
			self.result_lab = ResultLab(self.parent)
			_findchild(QHBoxLayout, 'row5').addWidget(self.result_lab)

			# start animation
			self.result_lab.animate()
		else:
			# handle error
			error_msg = "Your input had the following errors:\n"
			if not Checker.url(url):
				error_msg += f"- URL '{url}' was not valid. Make sure it's not empty, does not contain spaces and starts with 'http://'\n"

			if not Checker.tag_type(tag_type):
				error_msg += f"- Tag type '{tag_type}' is not a valid HTML tag.\n"
			
			if not Checker.tag_identifier(tag_identifier):
				error_msg += f"- Tag identifier '{tag_identifier}' must be either 'id' or 'class'.\n"

			if not Checker.tag_value(tag_value):
				error_msg += f"- Tag identifier '{tag_value}' must not be empty and must not contain spaces.\n"

			if not Checker.freq_val(freq_val):
				error_msg += f"- Frequency '{freq_val}' must be at least 1.\n"

			if not Checker.freq_type(freq_type):
				error_msg += f"- Time measure '{freq_type}' must be one of 'seconds', 'minutes' or 'hours'. Shortcuts 's', 'm' and 'h' are also accepted.\n"

			error_dialog = QMessageBox()
			error_dialog.setIcon(QMessageBox.Critical)
			error_dialog.setText(error_msg)
			error_dialog.setWindowTitle("Errore!")
			error_dialog.exec_()
	
	def on_html_tag_change(self, html_tag):
		# stop the animation
		self.result_lab.stop()

		print('Button received the output!:')
		print(html_tag)
