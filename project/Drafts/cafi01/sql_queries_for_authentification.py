from werkzeug.security import check_password_hash
from main import db

def readLogin(self, email):
    password_encr = self.cursor.execute("""SELECT password FROM tbl_user WHERE email=?""", email )
    return password_encr

def userExists(self, email):
    exists = False
    # if email already exists in the sql database, set exists to True
    return exists

# ----------
# Sign Up  |
# ----------
from main import db
from werkzeug.security import generate_password_hash

email = input('email')
firstName = input('firstName')
surName = input('surName')
password1 = input('password1')
password2 = input('password2')

if not userExists(email):
    db.insertUser(name=firstName, surname=surName, username=email[0:-4], email=email, password=generate_password_hash(password1, method='sha256'))
else:
    print("User already exists, try Login.")
    
# ----------
# Login    |
# ----------
email = input('email')
password = input('password')
password_encr = db.readLogin(email)

print(password)
print(password_encr)

if not userExists(email):
    print('Email does not exist.')
elif check_password_hash(password_encr, password):
    print('Login successful!')
else:
    print('Incorrect password, try again.')
