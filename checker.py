from params import Params


class Checker(object):
	@staticmethod
	def url(url: str) -> bool:
		return (url.startswith('http') and
				len(url) != 0 and
				' ' not in url)

	@staticmethod
	def tag_type(tag_type: str) -> bool:
		tags = [t.strip() for t in open('./possible-tags.txt', 'r').readlines()]
		return tag_type in tags

	@staticmethod
	def tag_value(tag_value: str) -> bool:
		return len(tag_value) != 0
	
	@staticmethod
	def tag_identifier(tag_identifier: str) -> bool:
		return tag_identifier in ['id', 'class']
	
	@staticmethod
	def freq_val(freq_val: int) -> bool:
		if not isinstance(freq_val, int):
			freq_val = int(freq_val)
		
		return freq_val >= 1

	@staticmethod
	def freq_type(freq_type: str) -> bool:
		return freq_type in ['seconds', 'minutes', 'hours',
							 's', 'm', 'h']

	@staticmethod
	def check_input() -> Params:
		import requests

		# url check
		url = input("Enter the url to be monitored: ")
		status_code = -1

		while status_code != 200:
			while not Checker.url(url):
				url = input("Url invalid, retry: ")
			
			try:
				response = requests.get(url)
				status_code = response.status_code
			except requests.ConnectionError:
				url = input("Url could not be reached, retry: ")

		# tag type
		tag_type = input("Enter the HTML tag type to be monitored: ")
		while not Checker.tag_type(tag_type):
			tag_type = input("Unknown HTML tag, retry: ")
		
		# tag identifier
		tag_identifier = input("Enter the tag's identifier, must be either 'id' or 'class': ")
		while not Checker.tag_identifier(tag_identifier):
			tag_identifier = input("Tag's identifier must be either 'id' or 'class', retry: ")

		# tag value check
		tag_value = input("Enter the tag's id or class value: ")
		while not Checker.tag_value(tag_value):
			tag_value = input("Tag's id or class must not be null, retry: ")

		# frequency type
		freq_type = input("Enter the time measure, being one of 'seconds', 'minutes' or 'hours'.\nShortcuts available: 's', 'm', 'h'")
		while not Checker.freq_type(freq_type):
			freq_type = input("Time measure invalid, retry")
		
		# frequency value
		freq_val = input("Enter the frequency of check (in the above time measure): ")
		freq_val = int(freq_val)
		while not Checker.freq_val(freq_val):
			freq_val = input("Time measure must not be zero or negative, retry: ")
			freq_val = int(freq_val)

		return Params({
			'url': url,
			'tag_type': tag_type,
			'tag_identifier': tag_identifier,
			'tag_value': tag_value,
			'freq_val': freq_val,
			'freq_type': freq_type})
	
	@staticmethod
	def check_yaml(path: str) -> Params:
		import yaml

		yml = yaml.safe_load(open(path, 'r'))
		
		if (
			Checker.url(yml['url']) and
			Checker.tag_type(yml['tag_type']) and
			Checker.tag_identifier(yml['tag_identifier']) and
			Checker.tag_value(yml['tag_value']) and
			Checker.freq_val(yml['freq_val']) and
			Checker.freq_type(yml['freq_type'])
		):
			return Params(yml)
		else:
			if not Checker.url(yml['url']):
				print(f"URL '{yml['url']}' was not valid.")

			if not Checker.tag_type(yml['tag_type']):
				print(f"Tag type '{yml['tag_type']}' was not valid.")
			
			if not Checker.tag_identifier(yml['tag_identifier']):
				print(f"Tag identifier '{yml['tag_identifier']}' was not valid.")

			if not Checker.tag_value(yml['tag_value']):
				print(f"'{yml['tag_value']}' was not valid.")

			if not Checker.freq_val(yml['freq_val']):
				print(f"Frequency '{yml['freq_val']}' was not valid.")

			if not Checker.freq_type(yml['freq_type']):
				print(f"Time measure '{yml['freq_type']}' was not valid.")
