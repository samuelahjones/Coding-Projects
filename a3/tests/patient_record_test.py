from unittest import TestCase
from unittest import main
from clinic.controller import PatientRecord
from clinic.controller import Note

class PatientRecordTests(TestCase):

	def setUp(self):
		self.patient_record = PatientRecord()

	def test_add_note(self):
		# Creating some expected notes 
		expected_note_1 = Note(1, "SENG 265 is the best class")
		expected_note_2 = Note(2, "Uvic is in Victoria BC")
		expected_note_3 = Note(3, "complaining about back pain")
		expected_note_4 = Note(4, "has very high blood pressure 200/120")
		expected_note_5 = Note(5, "pain is very high possiable internal bleeding")

		# Adding notes
		note = self.patient_record.add_note("SENG 265 is the best class")
		self.assertIsNotNone(note, "Note 1 has been added")
		self.assertEqual(note, expected_note_1, "Note 1 is correct")

		note = self.patient_record.add_note("Uvic is in Victoria BC")
		self.assertIsNotNone(note, "Note 1 has been added")
		self.assertEqual(note, expected_note_2, "Note 1 is correct")

		note = self.patient_record.add_note("complaining about back pain")
		self.assertIsNotNone(note, "Note 1 has been added")
		self.assertEqual(note, expected_note_3, "Note 1 is correct")

		note = self.patient_record.add_note("has very high blood pressure 200/120")
		self.assertIsNotNone(note, "Note 1 has been added")
		self.assertEqual(note, expected_note_4, "Note 1 is correct")

		note = self.patient_record.add_note("pain is very high possiable internal bleeding")
		self.assertIsNotNone(note, "Note 1 has been added")
		self.assertEqual(note, expected_note_5, "Note 1 is correct")

	def test_get_note(self):
		# Creating come notes in the pacient record
		note = self.patient_record.add_note("SENG 265 is the best class")
		note = self.patient_record.add_note("Uvic is in Victoria BC")
		note = self.patient_record.add_note("complaining about back pain")
		note = self.patient_record.add_note("has very high blood pressure 200/120")
		note = self.patient_record.add_note("pain is very high possiable internal bleeding")

		# Creating some expected notes 
		expected_note_1 = Note(1, "SENG 265 is the best class")
		expected_note_2 = Note(2, "Uvic is in Victoria BC")
		expected_note_3 = Note(3, "complaining about back pain")
		expected_note_4 = Note(4, "has very high blood pressure 200/120")
		expected_note_5 = Note(5, "pain is very high possiable internal bleeding")

		# Get first note 
		note = self.patient_record.get_note(1)
		self.assertIsNotNone(note, "got first note")
		self.assertEqual(note, expected_note_1, "note that was recived matches")

		# Giving code that has not been used yet
		note = self.patient_record.get_note(6)
		self.assertIsNone(note, "trying to get a note that was never created")

		# Seeing if 0 will brake the code
		note = self.patient_record.get_note(0)
		self.assertIsNone(note, "0 should not be a valid note")

		# Negative numbers should return none 
		note = self.patient_record.get_note(-1)
		self.assertIsNone(note, "negative codes should not get a note")

		# Asking for note that has been added 
		note = self.patient_record.get_note(3)
		self.assertIsNotNone(note, "code has note attached")
		self.assertEqual(note, expected_note_3, "note 3 matches")

	def test_search_text(self):
		# Creating some expected notes 
		expected_note_1 = Note(1, "SENG 265 is the best class")
		expected_note_2 = Note(2, "Uvic is in Victoria BC")
		expected_note_3 = Note(3, "complaining about back pain")
		expected_note_4 = Note(4, "has very high blood pressure 200/120")
		expected_note_5 = Note(5, "pain is very high possiable internal bleeding")

		# Creating come notes in the pacient record
		note = self.patient_record.add_note("SENG 265 is the best class")
		note = self.patient_record.add_note("Uvic is in Victoria BC")
		note = self.patient_record.add_note("complaining about back pain")
		note = self.patient_record.add_note("has very high blood pressure 200/120")
		note = self.patient_record.add_note("pain is very high possiable internal bleeding")

		retrieved_list = self.patient_record.search_text("bleeding")
		self.assertEqual(len(retrieved_list), 1, "1 note has 'bleeding' in them")
		note = retrieved_list[0]
		self.assertEqual(note, expected_note_5, "note 5 has been given")

		retrieved_list = self.patient_record.search_text("is")
		self.assertEqual(len(retrieved_list), 3, "Has three notes in the list")
		self.assertEqual(retrieved_list[0], expected_note_1, "note 1 has 'is' in it")
		self.assertEqual(retrieved_list[1], expected_note_2, "note 2 has 'is' in it")
		self.assertEqual(retrieved_list[2], expected_note_5, "note 5 has 'is' in it")

		# Seeing if numbers are able to be searched
		retrieved_list = self.patient_record.search_text("200/120")
		self.assertEqual(len(retrieved_list), 1, "One note given")
		note = retrieved_list[0]
		self.assertEqual(note, expected_note_4, "Note 4 is expected")

		# Multible numbers in the same note 
		retrieved_list = self.patient_record.search_text("2")
		self.assertEqual(len(retrieved_list), 2, "Should only give two notes back")
		self.assertEqual(retrieved_list[0], expected_note_1, "note 1 has been returned")
		self.assertEqual(retrieved_list[1], expected_note_4, "note 4 has been returned")

		# Upper clase and lower case 
		retrieved_list = self.patient_record.search_text("V")
		self.assertEqual(len(retrieved_list), 1, "One note has 'V' in them")
		self.assertEqual(retrieved_list[0], expected_note_2, "note 2 has upper case V in it")

		# can you search a space 
		retrieved_list = self.patient_record.search_text(" ")
		self.assertEqual(len(retrieved_list), 5, "aLL notes should be returned")
		self.assertEqual(retrieved_list[0], expected_note_1, "note 1 has been returned")
		self.assertEqual(retrieved_list[1], expected_note_2, "note 2 has been returned")
		self.assertEqual(retrieved_list[2], expected_note_3, "note 3 has been returned")
		self.assertEqual(retrieved_list[3], expected_note_4, "note 4 has been returned")
		self.assertEqual(retrieved_list[4], expected_note_5, "note 5 has been returned")

	def test_change_note(self):
		# Creating some expected notes that have chnages 
		expected_note_1 = Note(1, "SENG 265 is a class at UVic")
		expected_note_2 = Note(2, "UVic is in Victoria BC")
		expected_note_3 = Note(3, "complaining about back pain and shorness of breath")
		expected_note_4 = Note(4, "has very high blood pressure 200/120 heart rate 80 bpm")
		expected_note_5 = Note(5, "pain is very high")

		# Creating come notes in the pacient record
		note = self.patient_record.add_note("SENG 265 is the best class")
		note = self.patient_record.add_note("Uvic is in Victoria BC")
		note = self.patient_record.add_note("complaining about back pain")
		note = self.patient_record.add_note("has very high blood pressure 200/120")
		note = self.patient_record.add_note("pain is very high possiable internal bleeding")

		# Trying to change note that dose not exist
		self.assertFalse(self.patient_record.change_note(6, "Baseball"), "Note 6 has not been created")

		# Changing note that has been created
		self.assertTrue(self.patient_record.change_note(1, "SENG 265 is a class at UVic"), "Note 1 has been changed")
		note = self.patient_record.get_note(1)
		self.assertEqual(note, expected_note_1, "Note 1 has been succsefuly changed")

		# Changeing the rest of the notes
		self.assertTrue(self.patient_record.change_note(2, "UVic is in Victoria BC"), "Note 2 has been changed")
		self.assertTrue(self.patient_record.change_note(3, "complaining about back pain and shorness of breath"), "Note 3 has been changed")
		self.assertTrue(self.patient_record.change_note(4, "has very high blood pressure 200/120 heart rate 80 bpm"), "Note 4 has been changed")
		self.assertTrue(self.patient_record.change_note(5, "pain is very high"), "Note 5 has been changed")

		note = self.patient_record.get_note(2)
		self.assertEqual(note, expected_note_2, "Note 2 has been succsefuly changed")
		note = self.patient_record.get_note(3)
		self.assertEqual(note, expected_note_3, "Note 3 has been succsefuly changed")
		note = self.patient_record.get_note(4)
		self.assertEqual(note, expected_note_4, "Note 4 has been succsefuly changed")
		note = self.patient_record.get_note(5)
		self.assertEqual(note, expected_note_5, "Note 5 has been succsefuly changed")

		# Trying 0, and negatives
		self.assertFalse(self.patient_record.change_note(10, "Baseball"), "Note has not been created")
		self.assertFalse(self.patient_record.change_note(0, "Baseball"), "Note has not been created")
		self.assertFalse(self.patient_record.change_note(-6, "Baseball"), "Note has not been created")

	def test_remove_note(self):
		# Creating come notes in the pacient record
		note = self.patient_record.add_note("SENG 265 is the best class")
		note = self.patient_record.add_note("Uvic is in Victoria BC")
		note = self.patient_record.add_note("complaining about back pain")
		note = self.patient_record.add_note("has very high blood pressure 200/120")
		note = self.patient_record.add_note("pain is very high possiable internal bleeding")

		# Trying to remove note that dose not exist
		self.assertFalse(self.patient_record.remove_note(6), "Note dose not exist")

		# Removing a note that dose exist
		self.assertTrue(self.patient_record.remove_note(1), "Note 1 has been removed")
		self.assertIsNone(self.patient_record.get_note(1))

		# Trying with 0 and negaive numbers 
		self.assertFalse(self.patient_record.remove_note(0), "0 should not remove anything")
		self.assertFalse(self.patient_record.remove_note(-3), "Negative numbers should not remove anything")

		# Removing rest of notes
		self.assertTrue(self.patient_record.remove_note(2), "Note 2 has been removed")
		self.assertIsNone(self.patient_record.get_note(2))
		self.assertTrue(self.patient_record.remove_note(5), "Note 5 has been removed")
		self.assertIsNone(self.patient_record.get_note(5))
		self.assertTrue(self.patient_record.remove_note(4), "Note 4 has been removed")
		self.assertIsNone(self.patient_record.get_note(4))
		self.assertTrue(self.patient_record.remove_note(3), "Note 3 has been removed")
		self.assertIsNone(self.patient_record.get_note(3))

	def test_get_all_notes(self):
		# Creating some expected notes 
		expected_note_1 = Note(1, "SENG 265 is the best class")
		expected_note_2 = Note(2, "Uvic is in Victoria BC")
		expected_note_3 = Note(3, "complaining about back pain")
		expected_note_4 = Note(4, "has very high blood pressure 200/120")
		expected_note_5 = Note(5, "pain is very high possiable internal bleeding")

		notes_list = self.patient_record.get_all_notes()
		self.assertEqual(len(notes_list), 0, "No notes have been created")

		# Creating a note in the pacient record
		note = self.patient_record.add_note("SENG 265 is the best class")

		# Get all the notes
		notes_list = self.patient_record.get_all_notes()
		self.assertEqual(len(notes_list), 1, "One note have been created")
		self.assertEqual(notes_list[0], expected_note_1, "Note should be the same as expected_note_1")

		# Add more notes
		note = self.patient_record.add_note("Uvic is in Victoria BC")
		note = self.patient_record.add_note("complaining about back pain")
		note = self.patient_record.add_note("has very high blood pressure 200/120")
		note = self.patient_record.add_note("pain is very high possiable internal bleeding")

		# Get all the notes 
		notes_list = self.patient_record.get_all_notes()
		self.assertEqual(len(notes_list), 5, "There are five notes")
		self.assertEqual(notes_list[1], expected_note_2, "Note should be the same as expected_note_2")
		self.assertEqual(notes_list[2], expected_note_3, "Note should be the same as expected_note_3")
		self.assertEqual(notes_list[3], expected_note_4, "Note should be the same as expected_note_4")
		self.assertEqual(notes_list[4], expected_note_5, "Note should be the same as expected_note_5")

		# Remove some notes
		self.patient_record.remove_note(9)
		self.patient_record.remove_note(1)
		self.patient_record.remove_note(4)

		# Get list after removing notes
		notes_list = self.patient_record.get_all_notes()
		self.assertEqual(len(notes_list), 3, "Three notes should be given after some removing")
		self.assertEqual(notes_list[0], expected_note_2, "Note should be the same as expected_note_2")
		self.assertEqual(notes_list[1], expected_note_3, "Note should be the same as expected_note_3")
		self.assertEqual(notes_list[2], expected_note_5, "Note should be the same as expected_note_5")


if __name__ == '__main__':
	unittest.main()