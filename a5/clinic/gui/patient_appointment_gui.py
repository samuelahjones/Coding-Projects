import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QStackedWidget
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QStackedLayout, QVBoxLayout, QListWidget 
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QPlainTextEdit

from clinic.controller import Controller
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException

class PatientAppointment(QMainWindow):

	def __init__(self, controller):
		super().__init__()
		self.controller = controller
		self.patient = self.controller.get_current_patient()
		patient_title = f"Appointment - {self.patient.phn} {self.patient.name}"
		self.setWindowTitle(patient_title)

		self.resize(700,400)

		# Create Buttons to switch between different windows 
		self.button_end = QPushButton("End Appointment")
		self.button_home = QPushButton("Create \\ Update \\ Delete")
		self.button_list = QPushButton("Search Patient's Notes")

		# Add them to a widget that will go along the top of the window
		button_group = QHBoxLayout()
		button_group.addWidget(self.button_home)
		button_group.addWidget(self.button_list)
		button_group.addWidget(self.button_end)

		# Connect the buttons to functions when they are clicked 
		self.button_end.clicked.connect(self.end_button_clicked)
		self.button_home.clicked.connect(self.home_button_clicked)
		self.button_list.clicked.connect(self.list_button_clicked)

		# Page 1 - Create / Update / Delete Notes 
		page1_layout1 = QHBoxLayout()

		label_note_code = QLabel("Note Code:")
		self.text_note_code = QLineEdit()
		self.button_clear_page1 = QPushButton("Clear")
	   	
		page1_layout1.addWidget(label_note_code)
		page1_layout1.addWidget(self.text_note_code)
		page1_layout1.addWidget(self.button_clear_page1)

		# Plain Text Edit Widget for the text of the notes 
		self.page1_layout2 = QPlainTextEdit()

		# The Widget for the bottom buttons 
		page1_layout3 = QHBoxLayout()

		self.button_create = QPushButton("Create")
		self.button_update = QPushButton("Update")
		self.button_delete = QPushButton("Delete")

		self.button_create.setEnabled(False)
		self.button_update.setEnabled(False)
		self.button_delete.setEnabled(False)

		page1_layout3.addWidget(self.button_create)
		page1_layout3.addWidget(self.button_update)
		page1_layout3.addWidget(self.button_delete)

		# Create the final page layout 
		page1_layout = QVBoxLayout()
		page1_l1 = QWidget()
		page1_l1.setLayout(page1_layout1)
		page1_l3 = QWidget()
		page1_l3.setLayout(page1_layout3)
		page1_layout.addWidget(page1_l1)
		page1_layout.addWidget(self.page1_layout2)
		page1_layout.addWidget(page1_l3)

		# Make Page 1 into a Widget so it can be added to QStackedLayout
		page1 = QWidget()
		page1.setLayout(page1_layout)

		# Page 2 - Search Patient's Notes
		page2_layout1 = QHBoxLayout()

		label_search_name = QLabel("Search Text:")
		self.text_search = QLineEdit()
		self.button_search_name = QPushButton("Search Text")
		self.button_list_all = QPushButton("List All Notes")
		page2_layout1.addWidget(label_search_name)
		page2_layout1.addWidget(self.text_search)
		page2_layout1.addWidget(self.button_search_name)
		page2_layout1.addWidget(self.button_list_all)

		# You will not be able to edit any of the text when searching for notes that is why setReadOnly is set to True
		self.page2_layout2 = QPlainTextEdit()
		self.page2_layout2.setReadOnly(True)

		page2_layout3 = QHBoxLayout()

		self.button_clear_page2 = QPushButton("Clear")
		page2_layout3.addWidget(self.button_clear_page2)

		# Create the final page layout
		page2_layout = QVBoxLayout()
		page2_l1 = QWidget()
		page2_l1.setLayout(page2_layout1)
		page2_l3 = QWidget()
		page2_l3.setLayout(page2_layout3)
		page2_layout.addWidget(page2_l1)
		page2_layout.addWidget(self.page2_layout2)
		page2_layout.addWidget(page2_l3)

		# Make Page 2 into a Widget so it can be added to QStackedLayout
		page2 = QWidget()
		page2.setLayout(page2_layout)

		# Add Page 1 and 2 to Stacked Layout 
		self.stacklayout = QStackedLayout()
		self.stacklayout.addWidget(page1)
		self.stacklayout.addWidget(page2)

		layout = QVBoxLayout()
		layout.addLayout(button_group)
		layout.addLayout(self.stacklayout)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

		# Handle changing text from page 1
		self.text_note_code.textChanged.connect(self.home_text_changed)
		self.page1_layout2.textChanged.connect(self.home_text_changed)

		# Handle button clickes for page 1
		self.button_create.clicked.connect(self.create_button_clicked)
		self.button_update.clicked.connect(self.update_button_clicked)
		self.button_delete.clicked.connect(self.delete_button_clicked)
		self.button_clear_page1.clicked.connect(self.clear_page1_clicked)

		# Handle changing text from page 2
		self.button_search_name.clicked.connect(self.search_name_clicked)
		self.button_list_all.clicked.connect(self.list_all_clicked)
		self.button_clear_page2.clicked.connect(self.clear_page2_clicked)

	def end_button_clicked(self):
		# Close the window when appointment has ended 
		self.close()

	def home_button_clicked(self):
		# Change to Page 1
		self.stacklayout.setCurrentIndex(0)

	def list_button_clicked(self):
		# Change to Page 2
		self.stacklayout.setCurrentIndex(1)

	def home_text_changed(self):
		# Depending of where to user has added text the Create, Update, and Delete buttons will be enabled 
		if self.page1_layout2.toPlainText() and self.text_note_code.text():
			# User has added a code for a note and text so the Update button has been enabled and user is able to update note
			self.button_delete.setEnabled(False)
			self.button_update.setEnabled(True)
			self.button_create.setEnabled(False)
		elif self.page1_layout2.toPlainText() and not self.text_note_code.text():
			# User has only added text so user is allowed to create new note for patient 
			self.button_create.setEnabled(True)
			self.button_delete.setEnabled(False)
			self.button_update.setEnabled(False)
		elif self.text_note_code.text() and not self.page1_layout2.toPlainText():
			# User has only added a note code so user is allowed to delete that note from the patients recored 
			self.button_update.setEnabled(False)
			self.button_delete.setEnabled(True)
			self.button_create.setEnabled(False)
		else:
			# No text has been added so no button is enabled 
			self.button_create.setEnabled(False)
			self.button_update.setEnabled(False)
			self.button_delete.setEnabled(False)

	def create_button_clicked(self):
		# First get the text from the PlainTextEit Widget. Then check is the current patient set in the controller
		# is the same patient as this appointment. If the controller current patient and the windows patient are 
		# different show warning message and close window. If patient and controller patient are the same then 
		# create new note and clear text signaling to the user that the new note has been created   
		text = self.page1_layout2.toPlainText()
		if self.patient == self.controller.get_current_patient():
			self.controller.create_note(text)
			msgBox = QMessageBox(self)
			msgBox.setIcon(QMessageBox.Icon.Information)
			msgBox.setWindowTitle("Success")
			msgBox.setText("Note Created")
			msgBox.setInformativeText("Note has been succsesfuly created and stored in patients file")
			msgBox.exec()
			self.clear_page1_clicked()
		else:
			msgBox = QMessageBox(self)
			msgBox.setIcon(QMessageBox.Icon.Warning)
			msgBox.setWindowTitle("Warning")
			msgBox.setText("Incorrect Patient")
			msgBox.setInformativeText("Close Window and reset current patient")
			msgBox.exec()
			self.close()

	def update_button_clicked(self):
		# First get the text from the PlainTextEdit Widget, then try to and get the code turing it into an int if the 
		# code can not be turned into an int a exeption will be thrown and the warring will be shown to the user. If all
		# good check patient is corect then call controller to update note. If note succefuly updated "Note Created" 
		# message will be shown if not then a warning will be shown. Text and code only cleared if note succesfully updated
		text = self.page1_layout2.toPlainText()
		try:
			code = int(self.text_note_code.text())
			if self.patient == self.controller.get_current_patient():
				note = self.controller.update_note(code, text)
				if True:
					msgBox = QMessageBox(self)
					msgBox.setIcon(QMessageBox.Icon.Information)
					msgBox.setWindowTitle("Success")
					msgBox.setText("Note Updated")
					msgBox.setInformativeText("Note has been succsesfuly updated and stored in patients file")
					msgBox.exec()
					self.clear_page1_clicked()
				else:
					msgBox = QMessageBox(self)
					msgBox.setIcon(QMessageBox.Icon.Warning)
					msgBox.setWindowTitle("Warning")
					msgBox.setText("Unable to Update")
					msgBox.setInformativeText("Note not able to update as code dose not exist")
					msgBox.exec()
			else:
				msgBox = QMessageBox(self)
				msgBox.setIcon(QMessageBox.Icon.Warning)
				msgBox.setWindowTitle("Warning")
				msgBox.setText("Incorrect Patient")
				msgBox.setInformativeText("Close Window and reset current patient")
				msgBox.exec()
				self.close()
		except:
			msgBox = QMessageBox(self)
			msgBox.setIcon(QMessageBox.Icon.Warning)
			msgBox.setWindowTitle("Warning")
			msgBox.setText("Code Needs to be Number")
			msgBox.setInformativeText("The patients code needs to be a number above 0 text in not accepted")
			msgBox.exec()

	def delete_button_clicked(self):
		# Try to get code and turn into an int if exeptetion thrown show warning message if no exeption then check patient 
		# and call delete note method from controller clear code text if delete note succesfull if not then throw warning 
		# and show warning
		try:
			code = int(self.text_note_code.text())
			if self.patient == self.controller.get_current_patient():
				note = self.controller.delete_note(code)
				if True:
					msgBox = QMessageBox(self)
					msgBox.setIcon(QMessageBox.Icon.Information)
					msgBox.setWindowTitle("Success")
					msgBox.setText("Note Deleted")
					msgBox.setInformativeText("Note has been succsesfuly deleted and removed from patients file")
					msgBox.exec()
					self.clear_page1_clicked()
				else:
					msgBox = QMessageBox(self)
					msgBox.setIcon(QMessageBox.Icon.Warning)
					msgBox.setWindowTitle("Warning")
					msgBox.setText("Unable to Delete Note")
					msgBox.setInformativeText("Note was not able to be deleted from patient file, code may not exist")
					msgBox.exec()
			else:
				msgBox = QMessageBox(self)
				msgBox.setIcon(QMessageBox.Icon.Warning)
				msgBox.setWindowTitle("Warning")
				msgBox.setText("Incorrect Patient")
				msgBox.setInformativeText("Close Window and reset current patient")
				msgBox.exec()
				self.close()
		except:
			msgBox = QMessageBox(self)
			msgBox.setIcon(QMessageBox.Icon.Warning)
			msgBox.setWindowTitle("Warning")
			msgBox.setText("Code Needs to be Number")
			msgBox.setInformativeText("The patients code needs to be a number above 0 text in not accepted")
			msgBox.exec()

	def clear_page1_clicked(self):
		# Set both code line and text box on page 1 to nothing thereby clearing it
		self.page1_layout2.setPlainText("")
		self.text_note_code.setText("")

	# Functions for page 2
	def search_name_clicked(self):
		# Get text to search from search line then clear both search line and text box if patient is correct then call 
		# retrieve_notes from controller then iterate through the returned list and add the node code and timestamp on 
		# one line then the note text below it it will list smallest note code to largest
		search_text = self.text_search.text()
		self.clear_page2_clicked()
		if self.patient == self.controller.get_current_patient():
			note_list = self.controller.retrieve_notes(search_text)
			for note in note_list:
				line1 = f"{note.code}, {note.timestamp}"
				line2 = f"{note.text}"
				self.page2_layout2.appendPlainText(line1)
				self.page2_layout2.appendPlainText(line2)
		else:
			msgBox = QMessageBox(self)
			msgBox.setIcon(QMessageBox.Icon.Warning)
			msgBox.setWindowTitle("Warning")
			msgBox.setText("Incorrect Patient")
			msgBox.setInformativeText("Close Window and reset current patient")
			msgBox.exec()
			self.close()

	def list_all_clicked(self):
		# Clear the text box then check if patient is the correct patient then call list notes and iterate through the 
		# note list listing the note code and timestamp on one line and the text the line below it. The notes will be 
		# listed from largest note code to smallest
		self.clear_page2_clicked()
		if self.patient == self.controller.get_current_patient():
			note_list = self.controller.list_notes()
			for note in note_list:
				line1 = f"{note.code}, {note.timestamp}"
				line2 = f"{note.text}"
				self.page2_layout2.appendPlainText(line1)
				self.page2_layout2.appendPlainText(line2)
		else:
			msgBox = QMessageBox(self)
			msgBox.setIcon(QMessageBox.Icon.Warning)
			msgBox.setWindowTitle("Warning")
			msgBox.setText("Incorrect Patient")
			msgBox.setInformativeText("Close Window and reset current patient")
			msgBox.exec()
			self.close()

	def clear_page2_clicked(self):
		# Sets the search line and text box to nothing resulting in a clear
		self.page2_layout2.setPlainText("")
		self.text_search.setText("")