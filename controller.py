from gpiozero import AngularServo
from time import sleep
import pyrebase

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

config = {
  "apiKey" : "AIzaSyDdv3bogFpO1hhgJwC5AC_D2AAsW7Cwp2E",
  "authDomain" : "raspi-31b59.firebaseapp.com",
  "databaseURL" : "https://raspi-31b59-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "raspi-31b59",
  "storageBucket": "raspi-31b59.appspot.com",
  "messagingSenderId": "237198629770",
  "appId": "1:237198629770:web:25d05038fadc5d053a8673"
};

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()
database = firebase.database()
#data = {"key1":val}

def control(val):
    if val == 0:
        print("controller value 0")
        value = "mask detected"
        data = {"key1":value}
        database.set(data)
        servo.angle = 90
        sleep(2)
        
    elif val == 1:
        value = "mask not detected"
        print("conroller value 1")
        data = {"key1":value}
        database.set(data)
        servo.angle = 0
        sleep(2)

