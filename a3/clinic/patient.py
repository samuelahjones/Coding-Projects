from clinic.patient_record import PatientRecord


class Patient():
	
	def __init__(self, phn, name, birth_date, phone, email, address):
		self.phn = phn 
		self.name = name
		self.birth_date = birth_date
		self.phone = phone
		self.email = email
		self.address = address
		self.autocounter = PatientRecord()

	def __eq__(self, other): # for == operator
		if self.phn == other.phn and self.name == other.name and self.birth_date == other.birth_date and self.phone == other.phone and self.email == other.email and self.address == other.address:
			return True
		return False

	def __ne__(self, other): #for != operator
		if self.phn != other.phn and self.name != other.name and self.birth_date != other.birth_date and self.phone != other.phone and self.email != other.email and self.address != other.address:
			return False
		return True

	def is_phn_equal(self, phn): # checks current phn wth phn given 
		if self.phn == phn:
			return True
		else:
			return False

	def get_name(self):
		return self.name

	def get_phn(self):
		return self.phn

	def update(self, phn, name, birth_date, phone, email, address): 
		# Dose not have to check anything as controller has already done that 
		self.phn = phn
		self.name = name
		self.birth_date = birth_date
		self.phone = phone
		self.email = email
		self.address = address
		return True

	def add_note(self, text):
		note = self.autocounter.add_note(text) # Gives task to patient record
		return note

	def get_note(self, code):
		note = self.autocounter.get_note(code) # Gives task to patient record
		return note 

	def search_text(self, text):
		note_list = self.autocounter.search_text(text) # Gives task to patient record
		return note_list

	def change_note(self, code, text):
		note = self.autocounter.change_note(code, text) # Gives task to patient record
		return note

	def remove_note(self, code):
		note = self.autocounter.remove_note(code) # Gives task to patient record
		return note

	def get_all_notes(self):
		return self.autocounter.get_all_notes() # Gives task to patient record

