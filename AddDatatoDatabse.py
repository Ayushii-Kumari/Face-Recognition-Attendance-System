from weakref import ref
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://face-recognition-38757-default-rtdb.firebaseio.com/"
})

data ={                                      #dictionary
    "1001":{                                 #keys
        "name": "Ayushi Kumari",        #values
        "major": "CSE",
        "year": "2nd",
        "total attendance": 5,
        "year_of_joining":2023,
        "grade":8.9,
        "last_attendance_time":"2023-06-02 07:15:35"
    },
    "6009":{                                 #keys
        "name": "Arpit Bhardwaj",        #values
        "major": "CSE",
        "year": "2nd",
        "total attendance": 8,
        "year_of_joining":2022,
        "grade":9.2,
        "last_attendance_time":"2023-06-05 08:30:33"
    },
    "5007":{
        "name":"Elon Musk",
        "major":"CSE",
        "year":"4th",
        "total attendance": 0,
        "year_of_joining":2022,
        "grade":9.2,
        "last_attendance_time":"2023-06-04 08:31:33"
    },
    "5008":{                                 #keys
        "name": "Sarbadipta Das",        #values
        "major": "IT",
        "year": "3rd",
        "total attendance": 3,
        "year_of_joining":2022,
        "grade":9.5,
        "last_attendance_time":"2023-06-02 08:30:23"
    },
}

for key,values in data.items():
    ref.child(key).set(values)