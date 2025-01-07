import sys
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QStackedWidget
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QStackedLayout, QVBoxLayout, QListWidget 
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

from clinic.controller import Controller
from clinic.gui.patient_appointment_gui import PatientAppointment
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException

# The Skelotin of this code and call was copied from Lab 11 Excercize C 
class PatientTableModel(QAbstractTableModel):

	def __init__(self, controller):
		super().__init__()
		self.controller = controller
		self._data = []
		self.reset()

	def reset(self):
		# Will show no data in the Table
		self._data = []
		# emitting the layoutChanged signal to alert the QTableView of model changes
		self.layoutChanged.emit()

	def data(self, index, role):
		value = self._data[index.row()][index.column()]

		if role == Qt.ItemDataRole.DisplayRole:
			# Perform per-type checks and render accordingly.
			if isinstance(value, str):
				# Render strings with quotes
				return '%s' % value
			# Default (anything not captured above: e.g. int)
			return value

		if role == Qt.ItemDataRole.TextAlignmentRole:
			if isinstance(value, int) or isinstance(value, float):
				# Align right, vertical middle.
				return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight

	def rowCount(self, index):
		# The length of the outer list.
		return len(self._data)

	def columnCount(self, index):
		# The following takes the first sub-list, and returns
		# the length (only works if all rows are an equal length)
		if self._data:
			return len(self._data[0])
		else:
			return 0

	def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
		headers = ['PHN', 'Name', 'Date of Birth', 'Phone', 'Email', 'Address']
		if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
			return '%s' % headers[section]
		return super().headerData(section, orientation, role)

	def list_all_patients(self):
		# First sets _data to an emply array then calls list_patients from controller and gets a patient list. Iterates 
		# through the patient list putting all the data in a line then adding that to _data. Once all that is done signals
		# that the layout has changed so the data can be veiwed 
		self._data = []
		patient_list = self.controller.list_patients()
		for patient in patient_list:
			line = []
			line.append(patient.phn)
			line.append(patient.name)
			line.append(patient.birth_date)
			line.append(patient.phone)
			line.append(patient.email)
			line.append(patient.address)
			self._data.append(line)
		self.layoutChanged.emit()

	def retrive_patient_by_name(self, text):
		# First sets _data to an emply array then calls retrieve_patients from controller and gets a patient list. Iterates 
		# through the patient list putting all the data in a line then adding that to _data. Once all that is done signals
		# that the layout has changed so the data can be veiwed 
		self._data = []
		patient_list = self.controller.retrieve_patients(text)
		for patient in patient_list:
			line = []
			line.append(patient.phn)
			line.append(patient.name)
			line.append(patient.birth_date)
			line.append(patient.phone)
			line.append(patient.email)
			line.append(patient.address)
			self._data.append(line)
		self.layoutChanged.emit()