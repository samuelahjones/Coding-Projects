import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QStackedWidget
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QStackedLayout, QVBoxLayout, QListWidget 
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QTableView

from clinic.controller import Controller
from clinic.gui.patient_table_model import PatientTableModel
from clinic.gui.patient_appointment_gui import PatientAppointment
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException


class MainMenu(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Paitent Derecary Main Menu")
        self.patient_appointment = None

        self.resize(700,400)

        self.button_logout = QPushButton("Logout")
        self.button_home = QPushButton("Home")
        self.button_list = QPushButton("List Patients")

        self.button_logout.clicked.connect(self.logout_button_clicked)
        self.button_home.clicked.connect(self.home_button_clicked)
        self.button_list.clicked.connect(self.list_button_clicked)

        button_group = QHBoxLayout()
        button_group.addWidget(self.button_home)
        button_group.addWidget(self.button_list)
        button_group.addWidget(self.button_logout)

        # Page 1 where the user can Search, Create, Update, Delete, Set Currnet Patient, Unset Current Patient, and Start 
        # Appointment. All the buttons need will not be enabled exept for clear this is so only operations will be allowed
        # depending on what has been done and what data has been entered 
        page1_layout1 = QGridLayout()

        phn = QLabel("PHN")
        name = QLabel("Name")
        dob = QLabel("DOB")
        phone = QLabel("Phone")
        email = QLabel("Email")
        address = QLabel("Address")

        self.text_phn = QLineEdit()
        self.text_name = QLineEdit()
        self.text_dob = QLineEdit()
        self.text_phone = QLineEdit()
        self.text_email = QLineEdit()
        self.text_address = QLineEdit()

        self.text_phn.setPlaceholderText("##########")
        self.text_name.setPlaceholderText("First Last")
        self.text_dob.setPlaceholderText("YYYY-MM-DD")
        self.text_phone.setPlaceholderText("### ### ####")
        self.text_email.setPlaceholderText("example@example.com")
        self.text_address.setPlaceholderText("Address, City")

        page1_layout1.addWidget(phn, 0, 0)
        page1_layout1.addWidget(self.text_phn, 0, 1, 1, 2)
        page1_layout1.addWidget(name, 1, 0)
        page1_layout1.addWidget(self.text_name, 1, 1, 1, 2)
        page1_layout1.addWidget(dob, 2, 0)
        page1_layout1.addWidget(self.text_dob, 2, 1, 1, 2)
        page1_layout1.addWidget(phone, 3, 0)
        page1_layout1.addWidget(self.text_phone, 3, 1, 1, 2)
        page1_layout1.addWidget(email, 4, 0)
        page1_layout1.addWidget(self.text_email, 4, 1, 1, 2)
        page1_layout1.addWidget(address, 5, 0)
        page1_layout1.addWidget(self.text_address, 5, 1, 1, 2)

        page1_layout2 = QHBoxLayout()

        self.button_clear = QPushButton("Clear")
        self.button_search = QPushButton("Search")
        label_search_phn = QLabel("PHN:")
        self.text_search_phn = QLineEdit()
        self.text_search_phn.setPlaceholderText("##########")
        self.button_search.setEnabled(False)
        page1_layout2.addWidget(label_search_phn)
        page1_layout2.addWidget(self.text_search_phn)
        page1_layout2.addWidget(self.button_search)
        page1_layout2.addWidget(self.button_clear)

        self.button_create = QPushButton("Create")
        self.button_update = QPushButton("Update")
        self.button_delete = QPushButton("Delete")
        self.button_set = QPushButton("Set Current Patient")
        self.button_unset = QPushButton("Unset Current Patient")
        self.button_start = QPushButton("Start Appointment")

        self.button_create.setEnabled(False)
        self.button_update.setEnabled(False)
        self.button_delete.setEnabled(False)
        self.button_set.setEnabled(False)
        self.button_start.setEnabled(False)
        self.button_unset.setEnabled(False)

        page1_layout3 = QHBoxLayout()

        page1_layout3.addWidget(self.button_create)
        page1_layout3.addWidget(self.button_update)
        page1_layout3.addWidget(self.button_delete)

        page1_layout4 = QHBoxLayout()

        page1_layout4.addWidget(self.button_set)
        page1_layout4.addWidget(self.button_unset)
        page1_layout4.addWidget(self.button_start)

        page1_layout5 = QHBoxLayout()

        label_current_patient = QLabel("Current Patient Set:")
        self.text_current_patient = QLineEdit()
        self.text_current_patient.setEnabled(False)
        page1_layout5.addWidget(label_current_patient)
        page1_layout5.addWidget(self.text_current_patient)

        page1_layout = QVBoxLayout()
        page1_l1 = QWidget()
        page1_l1.setLayout(page1_layout1)
        page1_l2 = QWidget()
        page1_l2.setLayout(page1_layout2)
        page1_l3 = QWidget()
        page1_l3.setLayout(page1_layout3)
        page1_l4 = QWidget()
        page1_l4.setLayout(page1_layout4)
        page1_l5 = QWidget()
        page1_l5.setLayout(page1_layout5)
        page1_layout.addWidget(page1_l1)
        page1_layout.addWidget(page1_l2)
        page1_layout.addWidget(page1_l3)
        page1_layout.addWidget(page1_l4)
        page1_layout.addWidget(page1_l5)

        page1 = QWidget()
        page1.setLayout(page1_layout)

        # Page 2 is where the user will be able to search for multiple patients by name as well as list all the patients 
        # that are in the database
        page2_layout1 = QHBoxLayout()

        label_search_name = QLabel("Name:")
        self.text_search_name = QLineEdit()
        self.button_search_name = QPushButton("Search Name")
        self.button_list_all = QPushButton("List All Patients")
        self.button_clear_page2 = QPushButton("Clear")
        page2_layout1.addWidget(label_search_name)
        page2_layout1.addWidget(self.text_search_name)
        page2_layout1.addWidget(self.button_search_name)
        page2_layout1.addWidget(self.button_list_all)
        page2_layout1.addWidget(self.button_clear_page2)

        self.page2_layout2 = QTableView()
        self.patient_table = PatientTableModel(self.controller)
        self.page2_layout2.setModel(self.patient_table)
        self.page2_layout2.setEnabled(True)

        page2_layout = QVBoxLayout()
        page2_l1 = QWidget()
        page2_l1.setLayout(page2_layout1)
        page2_layout.addWidget(page2_l1)
        page2_layout.addWidget(self.page2_layout2)

        page2 = QWidget()
        page2.setLayout(page2_layout)

        self.stacklayout = QStackedLayout()
        self.stacklayout.addWidget(page1)
        self.stacklayout.addWidget(page2)

        layout = QVBoxLayout()
        layout.addLayout(button_group)
        layout.addLayout(self.stacklayout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.clear_page2_clicked()

        # Handle changing text from page 1
        self.text_phn.textChanged.connect(self.patient_text_changed)
        self.text_name.textChanged.connect(self.patient_text_changed)
        self.text_dob.textChanged.connect(self.patient_text_changed)
        self.text_phone.textChanged.connect(self.patient_text_changed)
        self.text_email.textChanged.connect(self.patient_text_changed)
        self.text_address.textChanged.connect(self.patient_text_changed)
        self.text_search_phn.textChanged.connect(self.search_phn_text_changed)

        # Other buttons form page 1
        self.button_clear.clicked.connect(self.clear_button_clicked)
        self.button_create.clicked.connect(self.create_botton_clicked)
        self.button_search.clicked.connect(self.search_botton_clicked)
        self.button_update.clicked.connect(self.update_botton_clicked)
        self.button_delete.clicked.connect(self.delete_botton_clicked)
        self.button_set.clicked.connect(self.set_button_clicked)
        self.button_unset.clicked.connect(self.unset_button_clicked)
        self.button_start.clicked.connect(self.start_button_clicked)

        # Page 2 Bottons and text
        self.text_search_name.textChanged.connect(self.search_name_text_changed)
        self.button_clear_page2.clicked.connect(self.clear_page2_clicked)
        self.button_search_name.clicked.connect(self.search_name_button_clicked)
        self.button_list_all.clicked.connect(self.list_all_button_clicked)


    def home_button_clicked(self):
        # Page 1 
        self.stacklayout.setCurrentIndex(0)

    def list_button_clicked(self):
        # Page 2
        self.stacklayout.setCurrentIndex(1)

    def search_phn_text_changed(self):
        # If search text is changed search button us enabled
        if self.text_search_phn.text():
            self.button_search.setEnabled(True)
        else:
            self.button_search.setEnabled(False)

    def patient_text_changed(self):
        # If all lines needed to make a patient then the create button is enabled and user is able to make a patient 
        if self.text_phn.text() and self.text_name.text() and self.text_dob.text() and self.text_phone.text() and self.text_email.text() and self.text_address.text() and not self.text_search_phn.text():
            self.button_create.setEnabled(True)
        else:
            self.button_create.setEnabled(False)

    def search_name_text_changed(self):
        # If name is added then search by text is enabled 
        if self.text_search_name.text():
            self.button_search_name.setEnabled(True)
        else:
            self.button_search_name.setEnabled(False)

    def logout_button_clicked(self):
        # Quit the program and logout controller 
        apt = self.controller.logout()
        self.close()

    def clear_button_clicked(self):
        # For page 1 will set all text lines to nothing and enable editing for the text lines it also will unenable the 
        # delete, update, and set current patient buttons.
        self.text_phn.setText("")
        self.text_name.setText("")
        self.text_dob.setText("")
        self.text_phone.setText("")
        self.text_email.setText("")
        self.text_address.setText("")
        self.text_search_phn.setText("")

        self.text_phn.setEnabled(True)
        self.text_name.setEnabled(True)
        self.text_dob.setEnabled(True)
        self.text_phone.setEnabled(True)
        self.text_email.setEnabled(True)
        self.text_address.setEnabled(True)
        self.text_search_phn.setEnabled(True)

        self.button_delete.setEnabled(False)
        self.button_update.setEnabled(False)
        self.button_set.setEnabled(False)

    def create_botton_clicked(self):
        # Create new patient. First try and make the text in the phn line into an int if that throws an exeption catch 
        # it and pop a message that says phn need to be a number. See if the phn given is < 1000000000 as phn need to 
        # be a 10 digit number. If its not a 10 digit number then show a warning saying phn need to be 10 digits. If phn
        # is 10 digits then take the rest of the patients data and try to create new patient by calling create_patient 
        # from controller if the exeption IllegalOperstionExeption is thrown show warning message if not thrown show 
        # success message and clear text lines. 
        try: 
            phn = int(self.text_phn.text())
            if phn < 1000000000:
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Invalid PHN")
                msgBox.setInformativeText("Personal Health Number needs to be a 10 digit number")
                msgBox.exec()
            else:
                name = self.text_name.text()
                dob = self.text_dob.text()
                phone = self.text_phone.text()
                email = self.text_email.text()
                address = self.text_address.text()
                try:
                    new_patient = self.controller.create_patient(phn, name, dob, phone, email, address)
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Icon.Information)
                    msgBox.setWindowTitle("Success")
                    msgBox.setText("New Patient Created")
                    msgBox.setInformativeText("Patient has been successfuly created and stored")
                    msgBox.exec()
                    self.clear_button_clicked()
                except IllegalOperationException:
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Icon.Warning)
                    msgBox.setWindowTitle("Warning")
                    msgBox.setText("Patient Already Exists")
                    msgBox.setInformativeText("Personal Health Number is alreay registered to patient in system unable to create new patinet")
                    msgBox.exec()
        except ValueError:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.setText("PHN Not Valid")
            msgBox.setInformativeText("Personal Health Number needs to be a 10 digit number")
            msgBox.exec()

    def search_botton_clicked(self):
        # Search for patients. First try and make the text in the phn line into an int if that throws an exeption catch 
        # it and pop a message that says phn need to be a number. See if the phn given is <= 1000000000 as phn need to 
        # be a 10 digit number. If it is not show warning message. If it is then call search_patient from controller 
        # and then check if it returned a patient or None. If None then show warning message saying the patient dose 
        # not exist. If the patinet exists show the patient data in the correct text lines as well as enableing update,
        # delete, and set buttons as well as turning off the search text line, search button, and create button as if the 
        # user wants to update the patient that was searched the phn that was used to search for the patient will be used 
        # as the old phn. 
        try:
            key = int(self.text_search_phn.text())
            if key < 1000000000:
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Invalid PHN Search")
                msgBox.setInformativeText("Not Valid Personal Health Number")
                msgBox.exec()
            else:
                patient = self.controller.search_patient(key)
                if patient:
                    phn = str(patient.phn)
                    name = patient.name 
                    dob = patient.birth_date
                    phone = patient.phone 
                    email = patient.email 
                    address = patient.address 
                    self.text_phn.setText(phn)
                    self.text_name.setText(name)
                    self.text_dob.setText(dob)
                    self.text_phone.setText(phone)
                    self.text_email.setText(email)
                    self.text_address.setText(address)
                    self.text_search_phn.setEnabled(False)
                    self.button_search.setEnabled(False)
                    self.button_create.setEnabled(False)
                    self.button_delete.setEnabled(True)
                    self.button_update.setEnabled(True)
                    self.button_set.setEnabled(True)
                else:
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Icon.Warning)
                    msgBox.setWindowTitle("Error")
                    msgBox.setText("Invalid PHN Search")
                    msgBox.setInformativeText("Personal Health Number dose not exist in records")
                    msgBox.exec()
                    self.clear_button_clicked()
        except:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText("Invalid PHN Search")
            msgBox.setInformativeText("Need to enter number to search for personal health number")
            msgBox.exec()

    def update_botton_clicked(self):
        # Updade Patients. First try and make the text in the phn line into an int if that throws an exeption catch 
        # it and pop a message that says phn need to be a number. See if the phn given is <= 1000000000 as phn need to 
        # be a 10 digit number. If it is not show warning message. If phn is 10 digit number get all patient data from 
        # the text lines. Call update_patient from controller and if an IllegalOperationException is thrown show warning 
        # message. If no exeption is thrown then show success messsage and then call clear_button_clicked.
        try:
            old_phn = int(self.text_search_phn.text())
            phn = int(self.text_phn.text())
            if phn < 1000000000:
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Invalid PHN Search")
                msgBox.setInformativeText("Not Valid Personal Health Number")
                msgBox.exec()
            else:
                name = self.text_name.text()
                dob = self.text_dob.text()
                phone = self.text_phone.text()
                email = self.text_email.text()
                address = self.text_address.text()
                try:
                    up = self.controller.update_patient(old_phn, phn, name, dob, phone, email, address)
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Icon.Information)
                    msgBox.setWindowTitle("Success")
                    msgBox.setText("Patient Updated Successfuly")
                    msgBox.setInformativeText("Patient information has been successfuly updated and stored")
                    msgBox.exec()
                    self.clear_button_clicked()
                except IllegalOperationException:
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Icon.Warning)
                    msgBox.setWindowTitle("Error")
                    msgBox.setText("Unable to Update")
                    msgBox.setInformativeText("Patient unable to be updated at this time")
                    msgBox.exec()
        except:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.setText("PHN Not Valid")
            msgBox.setInformativeText("Personal Health Number needs to be a 10 digit number")
            msgBox.exec()  

    def delete_botton_clicked(self):
        # Delete Patients. First try and make the text in the phn line into an int if that throws an exeption catch 
        # it and pop a message that says phn need to be a number. See if the phn given is <= 1000000000 as phn need to 
        # be a 10 digit number. If it is not show warning message. If phn is 10 digets then call delete_patient from
        # controller and show success message. If exeption is thrown by delete_patient show warning message. If no 
        # exeption call clear_button_clicked.
        try:
            phn = int(self.text_search_phn.text())
            if phn < 1000000000:
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Invalid PHN Search")
                msgBox.setInformativeText("Not Valid Personal Health Number")
                msgBox.exec()
            else:
                try:
                    patient = self.controller.delete_patient(phn)
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Icon.Information)
                    msgBox.setWindowTitle("Success")
                    msgBox.setText("Patient Deleted Successfuly")
                    msgBox.setInformativeText("Patient information has been successfuly deleted and removed from recoreds")
                    msgBox.exec()
                    self.clear_button_clicked()
                except IllegalOperationException:
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Icon.Warning)
                    msgBox.setWindowTitle("Error")
                    msgBox.setText("Unable to Delete")
                    msgBox.setInformativeText("Patient unable to be deleted at this time")
                    msgBox.exec()
        except:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.setText("PHN Not Valid")
            msgBox.setInformativeText("Personal Health Number needs to be a 10 digit number")
            msgBox.exec()

    def set_button_clicked(self):
        # Set Current Patient. Takes phn that was searched that has already been checked to be a 10 digit number and when 
        # search button is clicked user not able to change the search text line untill the clear button is clicked so we
        # know that the phn is good. try and call set_current_patient from controller is exeption IllegalOperationException
        # is thrown then show warning message. If no exeption is thrown take the patient number and name and convert it
        # into a string so text_current_patient can be set to it and the user can see what the set current patient is. 
        # Enable both unset and start appointment buttons and then call clear_button_clicked.
        phn = int(self.text_search_phn.text())
        try:
            self.controller.set_current_patient(phn)
            patient = self.controller.search_patient(phn)
            current = f"{str(patient.phn)}, {patient.name}"
            self.text_current_patient.setText(current)
            self.button_unset.setEnabled(True)
            self.button_start.setEnabled(True)
            self.clear_button_clicked()
        except IllegalOperationException:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText("Unable to Set Current Patinet")
            msgBox.setInformativeText("Patient dose not exist in the database")
            msgBox.exec()

    def unset_button_clicked(self):
        # Unset Current Patient. Clear text_current_patient then call unset_current_patient from controler and unenable 
        # unset and start appointment buttons. 
        self.text_current_patient.setText("")
        self.controller.unset_current_patient()
        self.button_unset.setEnabled(False)
        self.button_start.setEnabled(False)

    def start_button_clicked(self):
        # Make PatientAppointment Window and pass the controller into it and show the window. 
        self.patient_appointment = PatientAppointment(self.controller)
        self.patient_appointment.show()

    def clear_page2_clicked(self):
        # Clear Page 2. Clear the search bar and the table of any content. Enable user to search again
        self.text_search_name.setText("")
        self.patient_table.reset()
        self.text_search_name.setEnabled(True)

        self.button_list_all.setEnabled(True)
        self.button_search_name.setEnabled(True)

    def search_name_button_clicked(self):
        # Retrive list of patients that match name being searched. Get text from search line and then call 
        # retrieve_patients from controller getting a list of patients that match the search. If there is no patients
        # in the list show warning message. Then call list_all_patients from the PatientTableModel to fill the 
        # data into the table then resize the email column and address column so all the data is visible to the user.
        name = self.text_search_name.text()
        patient_list = self.controller.retrieve_patients(name)
        if len(patient_list) == 0:
            info = f"No patients with {name} in the database"
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText("No Patinets")
            msgBox.setInformativeText(info)
            msgBox.exec()
        else:
            self.patient_table.retrive_patient_by_name(name)
            self.page2_layout2.resizeColumnToContents(4)
            self.page2_layout2.resizeColumnToContents(5)

    def list_all_button_clicked(self):
        # Get List of all patients in database and show them in the table. Call list_patients from controller and get 
        # a list of all the patients. Check the list is not None and has patients in it. If not patients show warning 
        # message. Then call list_all_patients from the PatientTableModel to fill the data into the table then resize 
        # the email column and address column so all the data is visible to the user.
        patient_list = self.controller.list_patients()
        if patient_list is not None:
            if len(patient_list) == 0:
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Error")
                msgBox.setText("No Patinets")
                msgBox.setInformativeText("No patient in the database")
                msgBox.exec()
            else:
                self.patient_table.list_all_patients()
                self.page2_layout2.resizeColumnToContents(4)
                self.page2_layout2.resizeColumnToContents(5)
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText("No Patinets")
            msgBox.setInformativeText("No patient in the database")
            msgBox.exec()