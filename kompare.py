from jtc import Json

import pyrebase

config = {
	"apiKey": "AIzaSyA7QO0r37ncDU3h3fkBfUbmTxIEhpanBIs",
    "authDomain": "kompareproduction.firebaseapp.com",
    "databaseURL": "https://kompareproduction.firebaseio.com",
    "storageBucket": "kompareproduction.appspot.com",
    "messagingSenderId": "787427917798",
  "serviceAccount": "test.json",
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

email = "anivarth@gmail.com"

password = "anivarth"

# Log the user in
user = auth.sign_in_with_email_and_password(email, password)

db = firebase.database()

users = db.child("users")


f = open("jsonto.csv", 'wb')

f.close()

print users.shallow().get(user['idToken']).each()

for i in users.shallow().get(user['idToken']).each():
	print i

for u in users.shallow().get(user['idToken']).each():
	print "I am appending {} to the file jsonto.csv. Please don't tamper with that file!".format(u)
	kompare_prod = Json(dict(users.child(u).get(user['idToken']).val()))
	kompare_prod.convert_to_csv(filename = "jsonto.csv", delimiter = "`", write_mode = 'a')