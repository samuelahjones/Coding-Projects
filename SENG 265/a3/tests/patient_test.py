from unittest import TestCase
from unittest import main
from clinic.controller import Patient

class PatientTests(TestCase):

	def setUp(self):
		# Make some Patients for tests 
		self.patient1 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
		self.patient2 = Patient(9790013000, "Mary Doe", "2002-09-25", "250 230 1100", "mary.doe@gmail.com", "300 Moss St, Victoria")
		self.patient3 = Patient(9794412887, "Jim Bob", "1975-05-23", "778 203 1010", "jimmy.bob@jimbb.com", "300 Moss St, Victoria")
		self.patient4 = Patient(9700993344, "White Chocolate", "2008-03-20", "216 390 2945", "whitechocolate69@gmail.com", "300 4th St, Bermuda")
		self.patient5 = Patient(1000000000, "John Jones", "2000-01-01", "100 000 0000", "john@jones.com", "3967 W Broadway, Vancouver")

	def test_is_phn_equal(self):
		# Test with wrong phn
		self.assertFalse(self.patient1.is_phn_equal(6645498761), "Not the right phn")

		#Test with right phn
		self.assertTrue(self.patient5.is_phn_equal(1000000000), "The right phn")

		#Test with short phn and long phn
		self.assertFalse(self.patient3.is_phn_equal(66), "phn too short")
		self.assertFalse(self.patient2.is_phn_equal(664549876100909), "phn to long")

	def test_get_name(self):
		# Names expected to be returned 
		expected_name1 = "John Doe"
		expected_name2 = "White Chocolate"

		# Get name from Patient then compare to expected name 
		name = self.patient1.get_name()
		self.assertEqual(name, expected_name1, "John Doe is the name")

		name = self.patient4.get_name()
		self.assertEqual(name, expected_name2, "White Chocolate is the name")

	def test_get_phn(self):
		# Phn expected to be returned 
		expected_phn1 = 9794412887
		expected_phn2 = 1000000000

		# Get phn from Patient and compare to expected name
		phn = self.patient3.get_phn()
		self.assertEqual(phn, expected_phn1, "Phn from Patient 3")

		phn = self.patient5.get_phn()
		self.assertEqual(phn, expected_phn2, "Phn from Patient 5")


	def test_update(self):
		# Create some expected resultes for test 
		expected_patient1 = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
		expected_patient2 = Patient(9790013000, "Mary Doe", "2002-09-25", "250 230 1100", "mary.doe@gmail.com", "300 Moss St, Victoria")
		expected_patient3 = Patient(9794412887, "Jim Bob", "1975-05-23", "778 203 1010", "jimmy.bob@jimbob.com", "300 Moss St, Victoria")
		expected_patient4 = Patient(9700993344, "White Chocolate", "2008-03-20", "216 390 2945", "whitechocolate69@gmail.com", "4576 W 33rd, Vancouver")
		expected_patient5 = Patient(1000000000, "John Jones", "2000-01-01", "100 000 0000", "john@jones.com", "Earth")

		# Testing will same values 
		self.assertTrue(self.patient1.update(9790014000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria"))
		self.assertNotEqual(self.patient1, expected_patient1, "update worked as well as eq")

		self.assertTrue(self.patient2.update(9790013000, "Mary Doe", "2002-09-25", "250 230 1100", "mary.doe@gmail.com", "300 Moss St, Victoria"))
		self.assertEqual(self.patient2, expected_patient2, "update worked as well as eq")

		# Added one letter to eamil only
		self.assertTrue(self.patient3.update(9794412887, "Jim Bob", "1975-05-23", "778 203 1010", "jimmy.bob@jimbob.com", "300 Moss St, Victoria"))
		self.assertEqual(self.patient3, expected_patient3, "update worked as well as eq")

		# Testing with differernt values
		self.assertTrue(self.patient4.update(9700993344, "White Chocolate", "2008-03-20", "216 390 2945", "whitechocolate69@gmail.com", "4576 W 33rd, Vancouver"))
		self.assertEqual(self.patient4, expected_patient4, "update worked as well as eq")

		self.assertTrue(self.patient5.update(1000000000, "John Jones", "2000-01-01", "100 000 0000", "john@jones.com", "Earth"))
		self.assertEqual(self.patient5, expected_patient5, "update worked as well as eq")


if __name__ == '__main__':
	unittest.main()
