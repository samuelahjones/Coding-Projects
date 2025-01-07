from clinic.patient import Patient
from clinic.patient_record import PatientRecord
from clinic.note import Note
class Controller():
	
	def __init__(self):
		# Sets defalt Username and Password 
		self.username = "user"
		self.password = "clinic2024"
		# When controller is created it is logged out 
		self.logged_in = False
		self.num_patients = 0
		self.patient_list = list()
		self.current_patient = None
		# Can tell if a current patient is set 
		self.current_patient_set = False

	# looks if controller is already logged in if not if they are using the correct Username and Password
	def login(self, username, password):
		if self.logged_in == True:
			return False
		elif username == self.username and password == self.password:
			self.logged_in = True
			return True
		else:
			return False

	# looks if controller is already logged out if not logs out 
	def logout(self):
		if self.logged_in == False:
			return False
		else:
			self.logged_in = False
			return True

	# Checks if controller is logged in or not
	def is_logged_in(self):
		if self.logged_in == False:
			return False
		else:
			return True


	def create_patient(self, phn, name, birth_date, phone, email, address):
		if self.is_logged_in() == False:
			return None
		elif self.num_patients == 0: # If not patients in list don't have to check if phn already exists so new patient can be created right away
			new_patient = Patient(phn, name, birth_date, phone, email, address)
			self.patient_list.append(new_patient)
			self.num_patients += 1
			return new_patient
		else:
			for x in self.patient_list: # Checks if phn is already in use by another patient in the list
				if x.is_phn_equal(phn) == True:
					return None
			new_patient = Patient(phn, name, birth_date, phone, email, address)
			self.patient_list.append(new_patient)
			self.num_patients += 1
			return new_patient


	def search_patient(self, phn):
		if self.is_logged_in() == False:
			return None
		elif self.num_patients == 0: # If no patients have been added then nothing to search 
			return None
		else:	
			for x in self.patient_list: # goes through list of patients to find the one the matches given phn
				if x.is_phn_equal(phn) == True:
					return x
			return None # If phn does not match any phn patient has not been added 


	def retrieve_patients(self, name):
		if self.is_logged_in() == False:
			return None
		elif self.num_patients == 0:
			return None
		else:
			return_list = list() 
			for x in self.patient_list: # looks at each patient
				if name in x.get_name(): # looks at both first and last name 
					return_list.append(x)
			return return_list

	# looks if a phn already exists and returns a boolean 
	def dose_phn_exist(self, phn):
		for x in self.patient_list:
			if x.is_phn_equal(phn) == True:
				return True
		return False


	def update_patient(self, old_phn, new_phn, name, birth_date, phone, email, address):
		if self.is_logged_in() == False:
			return False
		elif self.num_patients == 0:
			return False
		elif self.current_patient_set != False: # Can not update Current Patient
			if self.current_patient.get_phn() == old_phn: # Looks if the patient you are wanting to update is the current patient
				return False 
		else:
			if old_phn == new_phn: # If you are not changing the phn you do not need to look if the new phn already exists
				for x in self.patient_list:
					if x.is_phn_equal(old_phn) == True:
						t = x.update(new_phn, name, birth_date, phone, email, address)
						return t
			if self.dose_phn_exist(old_phn) == True and self.dose_phn_exist(new_phn) == False: # Make sure new phn dose not already exist in aother patient
				for x in self.patient_list:
					if x.is_phn_equal(old_phn) == True:
						t = x.update(new_phn, name, birth_date, phone, email, address)
						return t
			return False


	def delete_patient(self, phn):
		if self.is_logged_in() == False:
			return False
		elif self.num_patients == 0:
			return False
		elif self.current_patient_set != False: 
			if self.current_patient.get_phn() == phn: # Looks if the patient you are wanting to remove is the current patient
				return False 
		else:
			n = 0
			for x in self.patient_list:
				if x.is_phn_equal(phn) == True:
					del self.patient_list[n] # deletes patient from list
					self.num_patients -= 1 
					return True
				n += 1
			return False


	def list_patients(self):
		if self.is_logged_in() == False:
			return None
		else:
			return self.patient_list # Gives list of patients


	def get_current_patient(self):
		if self.is_logged_in() == False:
			return None
		elif self.current_patient_set == False: 
			return None
		else:
			return self.current_patient


	def set_current_patient(self, phn):
		if self.is_logged_in() == False:
			pass
		elif self.num_patients == 0: # Can not set current patient if no patients have been added 
			pass
		else:
			x = self.search_patient(phn)
			self.current_patient = x
			self.current_patient_set = True


	def unset_current_patient(self):
		if self.is_logged_in() == False:
			pass
		else:
			self.current_patient = None
			self.current_patient_set = False


	def create_note(self, text):
		if self.is_logged_in() == False:
			return None
		elif self.num_patients == 0:
			return None
		elif self.current_patient_set == False:
			return None
		else:
			note = self.current_patient.add_note(text) # Gives task to patient
			return note


	def search_note(self, code): 
		# Checks peramiters it knows the answer too 
		if self.is_logged_in() == False:
			return None
		elif self.num_patients == 0:
			return None
		elif self.current_patient_set == False:
			return None
		elif code <= 0: # checks if code is not 0 or negative, dose not know how many notes have been created
			return None
		else:
			note = self.current_patient.get_note(code) # Gives task to patient 
			return note

	def retrieve_notes(self, text):
		if self.is_logged_in() == False:
			return None
		elif self.num_patients == 0:
			return None
		elif self.current_patient_set == False:
			return None
		elif text == "": # checks if text fro note has come contentd
			return None
		else:
			note_list = self.current_patient.search_text(text) # Gives task to patient
			return note_list


	def update_note(self, code, text):
		if self.is_logged_in() == False:
			return False
		elif self.num_patients == 0:
			return False
		elif self.current_patient_set == False:
			return False
		elif text == "": 
			return False
		elif code <= 0:
			return False
		else:
			note = self.current_patient.change_note(code, text) # Gives task to patient
			return note


	def delete_note(self, code):
		if self.is_logged_in() == False:
			return False
		elif self.num_patients == 0:
			return False
		elif self.current_patient_set == False:
			return False
		elif code <= 0:
			return False
		else:
			note = self.current_patient.remove_note(code) # Gives task to patient
			return note


	def list_notes(self):
		if self.is_logged_in() == False:
			return None
		elif self.num_patients == 0:
			return None
		elif self.current_patient_set == False:
			return None
		else:
			return self.current_patient.get_all_notes() # Gives task to patient