import os
import json 
from clinic.dao.patient_decoder import PatientDecoder
from clinic.dao.patient_encoder import PatientEncoder
from clinic.dao.patient_dao import PatientDAO

class PatientDAOJSON(PatientDAO):
	''' PatientDAOJSON class that preforms all the CRUD operations for the Controller class all exceptions handeled by Controllar class'''
	def __init__(self, autosave):
		''' Construct the patient dao json class '''
		self.autosave = autosave
		self.filename = "clinic/patients.json"
		self.patients = {}

		# If autosave=True then will read and write patient data to a json file 
		if self.autosave:
			try:
				# checks if file already exists if yes throws exception if no creates on with the right name 
				file = open(self.filename, "x")
			except:
				file = open(self.filename, "r")
				for line in file: # Reads through the file line by line 
					jsn = json.loads(line, cls=PatientDecoder) # Decodes the line 
					phn = jsn.phn # gets the patient phn 
					self.patients[phn] = jsn # adds the patient to the patient dictionary
			file.close()
		else:
			pass

	def search_patient(self, key):
		# Returns the patient that has the same kay
		return self.patients.get(key)

	def create_patient(self, patient, phn):
		# creates a new patient and adds it to the dictionary
		self.patients[phn] = patient
		if self.autosave: # If autosave=Ture will add the new patient to the json file 
			file = open(self.filename, "a")
			patient_json = json.dumps(patient, cls=PatientEncoder) # Encodes the patient for the json file
			file.write(patient_json) 
			file.write("\n") # Makes new line for next patient 
			file.close()
		return patient

	def retrieve_patients(self, name):
		# Returns list of patients that have the same name 
		retrieved_patients = []
		for patient in self.patients.values():
			if name in patient.name:
				retrieved_patients.append(patient)
		return retrieved_patients

	def update_patient(self, key, patient):
		# Updates existing patient
		self.patients[key] = patient
		if self.autosave: # If autosave=Ture will update patient details on json file by rewriting the entire thing 
			os.remove(self.filename)
			file = open(self.filename, "w")
			for x in self.patients.values(): # loops through each patient 
				patient_json = json.dumps(x, cls=PatientEncoder) 
				file.write(patient_json) 
				file.write("\n")
			file.close()

	def delete_patient(self, key):
		# Removes existing patient from patient dicinary
		self.patients.pop(key)
		# If autosave=True then will remove patient from json file by rewriting it
		# Patient has already been removed so it will not be added back to json file
		if self.autosave:
			os.remove(self.filename) 
			file = open(self.filename, "w")
			for x in self.patients.values(): # loops through eah patient add each one to json file 
				patient_json = json.dumps(x, cls=PatientEncoder)
				file.write(patient_json)
				file.write("\n")
			file.close()
		return True

	def list_patients(self):
		# Returns lists of all patients in the Dictionary
		patients_list = []
		for patient in self.patients.values():
			patients_list.append(patient)
		return patients_list