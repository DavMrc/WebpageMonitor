from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from widgets.line import Line
from widgets.monitor_lab import MonitorLab
from widgets.tag_lab import TagLab
from widgets.tag_type import TagType
from widgets.url_inp import UrlInput
from widgets.tag_identifier_value import TagIdentifierValue
from widgets.tag_identifier import TagIdentifier
from widgets.freq_lab import FreqLabel
from widgets.freq_type import FreqType
from widgets.freq_value import FreqValue
from widgets.send_btn import SendBtn


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Gui(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(QMainWindow, self).__init__()

        self.setWindowIcon(QIcon('./icon/logo.png'))
        self.setWindowTitle("Monitor a webpage")
        self.setObjectName("MainWindow")

        self.setupUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # row 0
        self.row0 = QtWidgets.QVBoxLayout()
        self.row0.setObjectName("row0")

        self.monitor_webpage_lab = MonitorLab(self.centralwidget)
        self.line = Line(self.centralwidget)

        self.row0.addWidget(self.monitor_webpage_lab)
        self.row0.addWidget(self.line)
        self.verticalLayout.addLayout(self.row0)

        # row 1
        self.row1 = QtWidgets.QHBoxLayout()
        self.row1.setObjectName("row1")

        self.url_lab = QtWidgets.QLabel(self.centralwidget)
        self.url_lab.setText("URL:")
        self.url_lab.setObjectName("url_lab")
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.url_inp = UrlInput(self.centralwidget)

        self.row1.addWidget(self.url_lab)
        self.row1.addItem(spacerItem)
        self.row1.addWidget(self.url_inp)
        self.verticalLayout.addLayout(self.row1)

        # row 2
        self.row2 = QtWidgets.QHBoxLayout()
        self.row2.setObjectName("row2")

        self.tag_lab = TagLab(self.centralwidget)
        spacerItem1 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.tag_type_inp = TagType(self.centralwidget)

        self.row2.addWidget(self.tag_lab)
        self.row2.addItem(spacerItem1)
        self.row2.addWidget(self.tag_type_inp)
        self.verticalLayout.addLayout(self.row2)

        # row 3
        self.row3 = QtWidgets.QHBoxLayout()
        self.row3.setObjectName("row3")

        self.tag_identifier_inp = TagIdentifier(self.centralwidget)
        self.tag_identifier_value_inp = TagIdentifierValue(self.centralwidget)

        self.row3.addWidget(self.tag_identifier_inp)
        self.row3.addWidget(self.tag_identifier_value_inp)
        self.verticalLayout.addLayout(self.row3)

        # row 4
        self.row4 = QtWidgets.QHBoxLayout()
        self.row4.setObjectName("row4")

        self.freq_lab = FreqLabel(self.centralwidget)
        self.freq_value = FreqValue(self.centralwidget)
        self.freq_type = FreqType(self.centralwidget) 
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.row4.addWidget(self.freq_lab)
        self.row4.addItem(spacerItem2)
        self.row4.addWidget(self.freq_value)
        self.row4.addItem(spacerItem3)
        self.row4.addWidget(self.freq_type)
        self.verticalLayout.addLayout(self.row4)

        # spacer between row 4 and 5
        spacerItem4 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)

        # row 5
        self.row5 = QtWidgets.QHBoxLayout()
        self.row5.setObjectName("row5")

        self.send_btn = SendBtn(self.centralwidget)

        self.row5.addWidget(self.send_btn)
        self.verticalLayout.addLayout(self.row5)

        # set central widget and finish
        self.setCentralWidget(self.centralwidget)
    
    def centerWindow(self):
        # unused, but could be useful
        def get_screensize():
            import ctypes

            user32 = ctypes.windll.user32
            user32.SetProcessDPIAware()
            return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        def get_centerpos(scrwidth, scrheight, winwidth, winheight):
            return scrwidth//2 - (winwidth//2), scrheight//2 - (winheight//2)

        scrwidth, scrheight = get_screensize()
        winwidth, winheight = scrwidth//4, scrheight//4
        xpos, ypos = get_centerpos(scrwidth, scrheight, winwidth, winheight)

        self.setGeometry(xpos, ypos, winwidth, winheight)

    def mainloop(self):
        self.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
