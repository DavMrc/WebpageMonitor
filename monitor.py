import requests
import time
from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup as BS

from params import Params


class Monitor(object):
	def __init__(self, params: Params):
		self.params = params

	def start_thread(self, on_html_tag_changed: callable):
		self.thread = MThread(self.__start)
		self.thread.start()
		self.thread.signal.connect(on_html_tag_changed)
	
	def start_sync(self):
		return self.__start()
	
	def __start(self) -> str:
		# calculate sleep amount, i.e. frequency
		sleep_amount = 0
		if self.params.freq_type == 's' or self.params.freq_type == 'seconds':
			sleep_amount = self.params.freq_val
		elif self.params.freq_type == 'm' or self.params.freq_type == 'minutes':
			sleep_amount = self.params.freq_val * 60
		elif self.params.freq_type == 'h' or self.params.freq_type == 'hours':
			sleep_amount = self.params.freq_val * (60 * 60)
		
		try:
			target = self.get_target_tag()
			iter = 0

			if target:
				target2 = target

				while target2 == target:
					print(f"Iter #{iter}: {target2}")
					time.sleep(sleep_amount)

					target2 = self.get_target_tag()
					iter += 1

				print("Target tag changed! Here it is:")
				print(target2)
				return str(target2)
			else:
				print("No tags matching the current configuration:")
				print(self.params)
		
		except requests.ConnectionError:
			print(f"Host '{self.params.url}' could not be reached. Check if it exists.")
	
	def get_target_tag(self):
		webpage = requests.get(self.params.url).content

		soup = BS(webpage, 'lxml')
		return soup.find(
			self.params.tag_type,
			attrs={self.params.tag_identifier: self.params.tag_value}
		)


class MThread(QThread):
	signal = pyqtSignal(str)

	def __init__(self, on_html_tag_changed: callable, parent=None):
		super().__init__(parent=parent)
		self.on_html_tag_changed = on_html_tag_changed

	def run(self):
		htmltag = self.on_html_tag_changed()
		self.signal.emit(htmltag)
