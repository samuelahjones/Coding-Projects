import datetime
from clinic.note import Note

class PatientRecord():

	def __init__(self):
		self.patient_notes = list()
		self.num_notes = 0

	def add_note(self, note):
		self.num_notes += 1 # before note is added to it can be the code of that note
		new_note = Note(self.num_notes, note)
		self.patient_notes.append(new_note)
		return new_note

	def get_note(self, code):
		if code > self.num_notes: # code can not be bigger then number of notes created 
			return None
		else:
			n = 0
			for x in self.patient_notes:
				if code == x.get_code(): # have to make sure code matches because notes can be deleted
					note = self.patient_notes[n]
					return note
				n += 1
			return None

	def search_text(self, text):
		return_list = list()
		for x in self.patient_notes:
			if text in x.get_text(): # looks through each notes text
				return_list.append(x)
		return return_list

	def change_note(self, code, text):
		if code > self.num_notes:
			return False
		else:
			n = 0
			for x in self.patient_notes:
				if code == x.get_code():
					self.patient_notes[n].change_text(text) # task undertaken by Note class
					return True
				n += 1
			return False

	def remove_note(self, code):
		if code > self.num_notes:
			return False
		else:
			n = 0
			for x in self.patient_notes:
				if code == x.get_code():
					del self.patient_notes[n] # deletes desired note and dose not return deleted note also dose not reduse number of notes becase num_notes is used as the code for new notes
					return True
				n += 1
			return False

	def get_all_notes(self):
		return_list = list()
		for x in self.patient_notes:
			return_list.insert(0, x) # Makes a list that has the newest note depending on its code first 
		return return_list
