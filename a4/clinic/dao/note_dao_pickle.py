import os
import datetime
from pickle import dump, load
from clinic.dao.note_dao import NoteDAO
from clinic.note import Note

class NoteDAOPickle(NoteDAO):
	''' NoteDAOPickle class that preforms all the CRUD operations for the PatientRecord class '''
	def __init__(self, phn, autosave):
		''' Construct the note dao pickle class '''
		self.autosave = autosave
		self.phn = phn
		self.counter = 0
		# Use the patient's phn as the name of the file 
		self.filename = f"clinic/records/{self.phn}.dat"

		self.notes = []
		if self.autosave:
			try:
				# checks if file already exists if yes throws exception if no creates on with the right name 
				file = open(self.filename, "x")
			except:
				with open(self.filename, "rb") as file:
					while True: # creats an infanit loops to load notes with everything from the file 
						try:
							element = load(file) # If nothing left in the file will throw exception
							self.notes.append(element)
							self.counter += 1
						except:
							break # Breaks out of infinet loop
			file.close()

	def search_note(self, key):
		''' Looks though all the notes as returns the one with the same key '''
		for note in self.notes:
			if note.code == key:
				return note
		return None

	def create_note(self, text):
		''' create a note in the patient's record '''
		self.counter += 1
		current_time = datetime.datetime.now()
		new_note = Note(self.counter, text, current_time)
		self.notes.append(new_note)
		if self.autosave: # If autosave=True will add the new note to file
			with open(self.filename, "ab") as file:
				dump(new_note, file)
		return new_note

	def retrieve_notes(self, search_string):
		''' retrieve notes in the patient's record that satisfy a search string '''
		retrieved_notes = []
		for note in self.notes:
			if search_string in note.text:
				retrieved_notes.append(note)
		return retrieved_notes

	def update_note(self, key, new_text):
		''' update a note from the patient's record '''
		updated_note = None

		# first, search the note by code
		for note in self.notes:
			if note.code == key:
				updated_note = note
				break

		# note does not exist
		if not updated_note:
			return False

		# note exists, update fields
		updated_note.text = new_text
		updated_note.timestamp = datetime.datetime.now()
		if self.autosave: # If autosave=True will re write the entire note file updating the note
			os.remove(self.filename)
			file = open(self.filename, "wb")
			for x in self.notes:
				dump(x, file)
			file.close()
		return True

	def delete_note(self, key):
		''' delete a note from the patient's record '''
		note_to_delete_index = -1

		# first, search the note by code
		for i in range(len(self.notes)):
			if self.notes[i].code == key:
				note_to_delete_index = i
				break

		# note does not exist
		if note_to_delete_index == -1:
			return False

		# note exists, delete note
		self.notes.pop(note_to_delete_index)
		if self.autosave: # If autosave=True will re write the entire note file not adding the note that was deleted
			os.remove(self.filename)
			file = open(self.filename, "wb")
			for x in self.notes:
				dump(x, file)
			file.close()
		return True

	def list_notes(self):
		# list existing notes
		notes_list = []
		for i in range(-1, -len(self.notes)-1, -1):
			notes_list.append(self.notes[i])
		return notes_list
