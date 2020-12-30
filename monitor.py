import requests
import time
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from bs4 import BeautifulSoup as BS

from params import Params


class Monitor(object):
	def __init__(self, params: Params):
		self.params = params

	def start_thread(self, on_html_tag_change: callable):
		# self.thread = threading.Thread(target=self.__start)
		# self.thread.start()
		thread = MThread(self.__start)
		thread.signal.result.connect(on_html_tag_change)

		pool = QThreadPool()
		pool.start(thread)
	
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
				
				# set it as property, will be returned when .join() is called
				self.test = target2
				print(target2)

				# return the same value, for sync method
				return target2
			else:
				print("No tags matching the current configuration:")
				print(self.params)
		
		except requests.ConnectionError:
			print(f"Host '{self.params.url}' could not be reached. Check if it exists.")
		# except KeyboardInterrupt:
		# 	print("Execution was aborted")
	
	def get_target_tag(self):
		webpage = requests.get(self.params.url).content

		soup = BS(webpage, 'lxml')
		return soup.find(
			self.params.tag_type,
			attrs={self.params.tag_identifier: self.params.tag_value}
		)


class MThread(QRunnable):
	def __init__(self, func, *args, **kwargs):
		super(MThread, self).__init__()

		self.func = func
		self.args = args
		self.kwargs = kwargs
		self.signal = Signal()

	@pyqtSlot()
	def run(self):
		print('thread started')
		result = self.func()
		self.signal.result.emit(result)


class Signal(QObject):
	result = pyqtSignal(str)
