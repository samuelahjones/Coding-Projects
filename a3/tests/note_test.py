from unittest import TestCase
from unittest import main
from clinic.controller import Note

class NoteTests(TestCase):

	def setUp(self):
		self.note1 = Note(1, "patient has cut on right upper leg")
		self.note2 = Note(2, "Medication given at 10:45pm next does due at 1:45am")
		self.note3 = Note(3, "complaining about back pain")
		self.note4 = Note(4, "patient has requested to be called the King of the world")
		self.note5 = Note(5, "cheese")

	def test_get_text(self):
		# Expected text to be returned by note
		expected_text1 = "patient has cut on right upper leg"
		expected_text2 = "Medication given at 10:45pm next does due at 1:45am"
		expected_text3 = "complaining about back pain"
		expected_text4 = "patient has requested to be called the King of the world"
		expected_text5 = "cheese"

		# Test text returned 
		text = self.note1.get_text()
		self.assertEqual(text, expected_text1, "Text for note 1 has been loaded")

		text = self.note2.get_text()
		self.assertEqual(text, expected_text2, "Text for note 1 has been loaded")

		text = self.note4.get_text()
		self.assertNotEqual(text, expected_text3, "Text for note 1 has been loaded")

		text = self.note4.get_text()
		self.assertEqual(text, expected_text4, "Text for note 1 has been loaded")

		text = self.note4.get_text()
		self.assertNotEqual(text, expected_text5, "Text for note 1 has been loaded")

	def test_get_code(self):
		# Expected text to be returned by note
		expected_code1 = 1
		expected_code2 = 2
		expected_code3 = 3
		expected_code4 = 4
		expected_code5 = 5

		# Test code retured 
		code = self.note1.get_code()
		self.assertEqual(code, expected_code1, "Code from note 1")

		code = self.note1.get_code()
		self.assertNotEqual(code, expected_code2, "Code from note 1")

		code = self.note3.get_code()
		self.assertEqual(code, expected_code3, "Code from note 1")

		code = self.note4.get_code()
		self.assertEqual(code, expected_code4, "Code from note 1")

		code = self.note5.get_code()
		self.assertEqual(code, expected_code5, "Code from note 1")

	def test_change_text(self):
		# Expected text after it is changed 
		expected_text1 = Note(1, "Fruit")
		expected_text2 = Note(2, "The weather is 9 degrees celcious with winds out of the northwest visability mild with sweels in the 5 to 8 ft range")
		expected_text3 = Note(3, "complaining about back pain and headacke")
		expected_text4 = Note(4, "patient has requested to be called cheese")
		expected_text5 = Note(5, "")

		# Test making text shorter
		self.note1.change_text("Fruit")
		self.assertEqual(self.note1, expected_text1, "Text has been changed")

		# Test making text longer
		self.note2.change_text("The weather is 9 degrees celcious with winds out of the northwest visability mild with sweels in the 5 to 8 ft range")
		self.assertEqual(self.note2, expected_text2, "Text has been changed")

		# Test adding some words
		self.note3.change_text("complaining about back pain and headacke")
		self.assertEqual(self.note3, expected_text3, "Text has been changed")

		# Test taking away words and adding new ones in there place
		self.note4.change_text("patient has requested to be called cheese")
		self.assertEqual(self.note4, expected_text4, "Text has been changed")

		# Test giving no text
		self.note5.change_text("")
		self.assertEqual(self.note5, expected_text5, "Text has been changed")


if __name__ == '__main__':
	unittest.main()