import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QStackedWidget
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QStackedLayout, QVBoxLayout, QListWidget

from clinic.controller import Controller
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException

from clinic.gui.main_menu_gui import MainMenu

class ClinicGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.log_in = None
        self.controller = Controller(autosave=True)
        self.setWindowTitle("Login")

        self.resize(400,200)

        layout = QGridLayout()
        # layout.setContentsMargins(20,20,20,20)

        label_username = QLabel("Username")
        self.text_username = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()
        self.text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_login = QPushButton("Login")
        self.button_quit = QPushButton("Quit")

        layout.addWidget(label_username, 1, 0)
        layout.addWidget(self.text_username, 1, 1, 1, 2)
        layout.addWidget(label_password, 2, 0)
        layout.addWidget(self.text_password, 2, 1, 1, 2)
        layout.addWidget(self.button_quit, 3, 1)
        layout.addWidget(self.button_login, 3, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Manage button clicks, Can use the enter key insted of clicking login button
        self.button_login.clicked.connect(self.login_button_clicked)
        self.text_username.returnPressed.connect(self.login_button_clicked)
        self.text_password.returnPressed.connect(self.login_button_clicked)
        self.button_quit.clicked.connect(self.quit_button_clicked)   


    def login_button_clicked(self):
        ''' 'handles controller login '''

        username = self.text_username.text()
        password = self.text_password.text()

        # Controller might not be logout depending on how the program was exited so first is to logout. If exeption 
        # try to login if that throws an exeption then say show warning with invalid username or passward. 
        try:
            apt = self.controller.logout()
            try:
                apt = self.controller.login(username, password)
                # Logged in successfully, Create MainMenu Window and show it when clone this window
                if self.log_in is None:
                    self.log_in = MainMenu(self.controller)
                self.log_in.show()
                self.close()
            except InvalidLoginException:
                # Incorrect Username or Password
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Warning")
                msgBox.setText("Error")
                msgBox.setInformativeText("Incorrect username or password")
                msgBox.exec()
        except InvalidLogoutException:
            try:
                apt = self.controller.login(username, password)
                # Logged in successfully, Create MainMenu Window and show it when clone this window 
                if self.log_in is None:
                    self.log_in = MainMenu(self.controller)
                self.log_in.show()
                self.close()
            except InvalidLoginException:
                # Incorrect Username or Password
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Warning")
                msgBox.setText("Error")
                msgBox.setInformativeText("Incorrect username or password")
                msgBox.exec()

        self.text_password.setText("")
        self.text_username.setText("")


    def quit_button_clicked(self):
        ''' quit the program '''
        self.close()



def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
