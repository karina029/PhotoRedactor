from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
'''
import sqlite3
#  Create data base
db = sqlite3.connect('dbaccount.db')
#  Create cursor
c = db.cursor()

c.execute("""CREATE TABLE logins (
    Login text, 
    passwords text
)""")

db.commit()

#  Close data base
db.close()
'''

app1 = QApplication([])
win_account = QWidget()
win_account.setWindowTitle('Account')
win_account.resize(400, 300)
win_account.setStyleSheet('''background-color:  rgb(223, 190, 232);''')
account_label = QLabel('Hello! This is Photo Redactor')
q_label = QLabel('Do you have account?')
field_login = QLineEdit()
field_login.setPlaceholderText("Login...")
field_password = QLineEdit()
field_password.setPlaceholderText("Password...")
sign_in_btn = QPushButton('Sign in')
sign_up_btn = QPushButton('Sign up')

hlayout1 = QHBoxLayout()
hlayout1.addWidget(account_label, alignment=Qt.AlignCenter)
hlayout2 = QHBoxLayout()
hlayout2.addWidget(q_label, alignment=Qt.AlignCenter)
hlayout3 = QHBoxLayout()
hlayout3.addWidget(field_login)
hlayout4 = QHBoxLayout()
hlayout4.addWidget(field_password)
hlayout5 = QHBoxLayout()
hlayout5.addWidget(sign_in_btn, alignment=Qt.AlignLeft)
hlayout5.addWidget(sign_up_btn, alignment=Qt.AlignRight)


vlayout1 = QVBoxLayout()
vlayout1.addLayout(hlayout1, stretch = 3)
vlayout1.addLayout(hlayout2, stretch = 2)
vlayout1.addLayout(hlayout3)
vlayout1.addLayout(hlayout4)
vlayout1.addLayout(hlayout5)

win_account.setLayout(vlayout1)

win_sign_up = QWidget()
app2 = QApplication([])
win_sign_up.setWindowTitle('Sign up')
win_sign_up.resize(400, 300)
win_sign_up.setStyleSheet('''background-color: rgb(237, 196, 138);''')
creatac_label = QLabel('Create your private account!')

field_login1 = QLineEdit()
field_login1.setPlaceholderText("Login...")
field_password1 = QLineEdit()
field_password1.setPlaceholderText("Password...")
sign_up_btn1 = QPushButton('Sign up')

hlay1 = QHBoxLayout()
hlay1.addWidget(creatac_label, alignment=Qt.AlignCenter)
hlay2 = QHBoxLayout()
hlay2.addWidget(field_login1)
hlay3 = QHBoxLayout()
hlay3.addWidget(field_password1)
hlay4 = QHBoxLayout()
hlay4.addWidget(sign_up_btn1, alignment=Qt.AlignCenter)


vlay1 = QVBoxLayout()
vlay1.addLayout(hlay1)
vlay1.addLayout(hlay2)
vlay1.addLayout(hlay3)
vlay1.addLayout(hlay4)

win_sign_up.setLayout(vlay1)

sign_in_btn.setStyleSheet('''color: white;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));
	width: 100 px; height: 30;
	border-radius: 10px;''')

sign_up_btn.setStyleSheet('''
	color: white;
	background-color:qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 199, 0, 255), stop:1 rgba(192, 5, 67, 255));
	width: 100 px; height: 30;
	border-radius: 10px;''')
sign_up_btn1.setStyleSheet('''
	color: white;
	background-color:qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 199, 0, 255), stop:1 rgba(192, 5, 67, 255));
	width: 100 px; height: 30;
	border-radius: 10px;''')



