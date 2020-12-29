from PyQt5.QtCore import QEasingCurve, QVariantAnimation
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QLabel, QSizePolicy


class ResultLab(QLabel):
	name = "result_lab"

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.parent = parent
		self.setObjectName(ResultLab.name)
		self.setText("Waiting...")

		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)

		self.animation = QVariantAnimation()
		self.animation_dur = 2000
		self.animation.valueChanged.connect(self.changeColor)
	
	def changeColor(self, color: QColor):
		palette = self.palette()
		palette.setColor(QPalette.WindowText, color)
		self.setPalette(palette)
	
	def animate(self, count=-1):
		self.animation.setLoopCount(count)
		self.animation.setStartValue(QColor(0, 0, 0, 255))
		self.animation.setEndValue(QColor(0, 0, 0, 0))
		self.animation.setDuration(self.animation_dur)
		self.animation.setEasingCurve(QEasingCurve.InBack)
		self.animation.start()
	
	def stop(self):
		self.animation.stop()

		palette = self.palette()
		palette.setColor(QPalette.WindowText, QColor(0, 0, 0, 255))
		self.setPalette(palette)

		self.setText("Finished!")
