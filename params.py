class Params(object):
	def __init__(self, params_dict):
		self.url = 				params_dict['url']
		self.tag_type = 		params_dict['tag_type']
		self.tag_identifier = 	params_dict['tag_identifier']
		self.tag_value = 		params_dict['tag_value']
		self.freq_val = 		params_dict['freq_val']
		self.freq_type = 		params_dict['freq_type']

		self.__params_dict__ = params_dict

	def __str__(self) -> str:
		import json

		return json.dumps(self.__params_dict__, indent=2)