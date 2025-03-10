import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QFormLayout
)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        
        # Identitas Group
        identity_group = QGroupBox("Identitas (vertical box layout)")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Hendra Ahmad Yani"))
        identity_layout.addWidget(QLabel("Nim : F1D022122"))
        identity_layout.addWidget(QLabel("Kelas : C"))
        identity_group.setLayout(identity_layout)
        
        # Navigation Buttons
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        
        # Registration Form
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()
        self.full_name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        self.gender_male = QRadioButton("Male")
        self.gender_female = QRadioButton("Female")
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.gender_male)
        gender_layout.addWidget(self.gender_female)
        
        self.country = QComboBox()
        self.country.addItems(["Select Country", "Indonesia", "Malaysia", "Timor Leste", "Singapore"])
        
        form_layout.addRow("Full Name:", self.full_name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Phone:", self.phone)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", self.country)
        form_group.setLayout(form_layout)
        
        # Action Buttons
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        action_layout.addWidget(QPushButton("Submit"))
        action_layout.addWidget(QPushButton("Cancel"))
        action_group.setLayout(action_layout)
        
        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(identity_group)
        main_layout.addWidget(nav_group)
        main_layout.addWidget(form_group)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())