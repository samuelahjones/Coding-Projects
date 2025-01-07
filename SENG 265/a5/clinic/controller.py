import hashlib
from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note
from clinic.dao.patient_dao_json import PatientDAOJSON
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException

class Controller():
	''' controller class that receives the system's operations '''

	def __init__(self, autosave=False):
		''' construct a controller class '''
		self.users = self.load_users()

		self.username = None
		self.password = None
		self.logged = False

		self.current_patient = None
		self.autosave = autosave
		self.patient_dao = PatientDAOJSON(self.autosave)

	def load_users(self):
		users = {}
		f = open('clinic/users.txt', 'r')
		for line in f:
			x = line.strip()
			x = x.split(",")
			users[x[0]] = x[1]
		f.close()
		return users

	def get_password_hash(self, password):
		encoded_password = password.encode('utf-8')
		hash_object = hashlib.sha256(encoded_password)
		hex_dig = hash_object.hexdigest()
		return hex_dig

	def login(self, username, password):
		''' user logs in the system '''
		pw = self.get_password_hash(password)
		if self.logged:
			raise DuplicateLoginException()
		if username in self.users:
			if pw == self.users[username]:
				self.username = username
				self.password = password
				self.logged = True
				return True
			else:
				raise InvalidLoginException()
		else:
			raise InvalidLoginException()

	def logout(self):
		''' user logs out from the system '''
		if not self.logged:
			raise InvalidLogoutException()
		else:
			self.username = None
			self.password = None
			self.logged = False
			self.current_patient = None
			return True

	def search_patient(self, phn):
		''' user searches a patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		return self.patient_dao.search_patient(phn)

	def create_patient(self, phn, name, birth_date, phone, email, address):
		''' user creates a patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# patient already exists, do not create them
		if self.search_patient(phn):
			raise IllegalOperationException()

		# finally, create a new patient
		patient = Patient(phn, name, birth_date, phone, email, address, self.autosave)
		return self.patient_dao.create_patient(patient, phn)

	def retrieve_patients(self, name):
		''' user retrieves the patients that satisfy a search criterion '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		return self.patient_dao.retrieve_patients(name)

	def update_patient(self, original_phn, phn, name, birth_date, phone, email, address):
		''' user updates a patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# first, search the patient by key
		patient = self.search_patient(original_phn)

		# patient does not exist, cannot update
		if not patient:
			raise IllegalOperationException()

		# patient is current patient, cannot update
		if self.current_patient:
			if patient == self.current_patient:
				raise IllegalOperationException()

		# treat different keys as a separate case
		if original_phn != phn:
			if self.search_patient(phn):
				raise IllegalOperationException() 
			new_patient = Patient(phn, name, birth_date, phone, email, address, self.autosave)
			self.patient_dao.update_patient(phn, new_patient)
		else:
			new_patient = Patient(original_phn, name, birth_date, phone, email, address, self.autosave)
			self.patient_dao.update_patient(original_phn, new_patient)

		return True
			
	def delete_patient(self, phn):
		''' user deletes a patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# first, search the patient by key
		patient = self.search_patient(phn)

		# patient does not exist, cannot delete
		if not patient:
			raise IllegalOperationException()

		# patient is current patient, cannot delete
		if self.current_patient:
			if patient == self.current_patient:
				raise IllegalOperationException()

		# patient exists, delete patient
		return self.patient_dao.delete_patient(phn)

	def list_patients(self):
		''' user lists all patients '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		return self.patient_dao.list_patients()

	def set_current_patient(self, phn):
		''' user sets the current patient '''

		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# first, search the patient by key
		patient = self.search_patient(phn)

		# patient does not exist
		if not patient:
			raise IllegalOperationException()

		# patient exists, set them to be the current patient
		self.current_patient = patient


	def get_current_patient(self):
		''' get the current patient '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# return current patient
		return self.current_patient

	def unset_current_patient(self):
		''' unset the current patient '''

		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# unset current patient
		self.current_patient = None


	def search_note(self, code):
		''' user searches a note from the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException()

		# search a new note with the given code and return it 
		return self.current_patient.search_note(code)

	def create_note(self, text):
		''' user creates a note in the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException()

		# create a new note and return it
		return self.current_patient.create_note(text)

	def retrieve_notes(self, search_string):
		''' user retrieves the notes from the current patient's record
			that satisfy a search string '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException()

		# return the found notes
		return self.current_patient.retrieve_notes(search_string)

	def update_note(self, code, new_text):
		''' user updates a note from the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException()

		# update note
		return self.current_patient.update_note(code, new_text)

	def delete_note(self, code):
		''' user deletes a note from the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException()

		# delete note
		return self.current_patient.delete_note(code)

	def list_notes(self):
		''' user lists all notes from the current patient's record '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException()

		# there must be a valid current patient
		if not self.current_patient:
			raise NoCurrentPatientException()

		return self.current_patient.list_notes()
