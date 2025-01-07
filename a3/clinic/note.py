import datetime


class Note():
	
	def __init__(self, code, text):
		self.code = code
		self.text = text
		self.timestamp = datetime.datetime.now()

	def __eq__(self, other): # for == operation dose not check timestamp
		if self.code == other.code and self.text == other.text:
			return True
		return False

	def __ne__(self, other): # for != operation dose not check timestamp
		if self.code != other.code and self.text != other.text:
			return False 
		return True

	def get_text(self):
		return self.text

	def get_code(self):
		return self.code

	def change_text(self, text):
		self.text = text
		self.timestamp = datetime.datetime.now() # Updates the timestamp

