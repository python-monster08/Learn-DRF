import requests
import json

URL = "http://127.0.0.1:8000/api/student/"

#  Get Method: 
def get_data(id=None):
    data = {}   #Intialize the blank Dict.
    if id is not None:
        data = {'id':id}    # Python Data
    json_data = json.dumps(data)   # Convert Python data into Json Data
    r = requests.get(url=URL, data=json_data)    # Send Request Client to Server

    data = r.json()   # Extract Response Data in json formate
    print(data)     #Print Response Data 

# get_data(1) # Get Single data using ID
# get_data()  # Get All Data

# Post Method:
def post_data():
    data = {
        'name': 'Mohit',
        'roll': 105,
        'city': 'Shihore',
    }
    json_data = json.dumps(data)   # Convert Python data into Json Data
    r = requests.post(url=URL, data=json_data)    # Send Request Client to Server for post

    data = r.json()   # Extract Response Data in json formate
    print(data)     #Print Response Data 


# post_data() 

# Update Method:
def update_data():
    data = {
        'id':1,
        'name': 'Girraj ',
        'city': 'Guna',
    }
    json_data = json.dumps(data)   # Convert Python data into Json Data
    r = requests.put(url=URL, data=json_data)    # Send Request Client to Server for Update

    data = r.json()   # Extract Response Data in json formate
    print(data)     #Print Response Data 

update_data()

# Delete Method:
def delete_data():
    data = {'id':6}
    json_data = json.dumps(data)   # Convert Python data into Json Data
    r = requests.delete(url=URL, data=json_data)    # Send Request Client to Server for delete

    data = r.json()   # Extract Response Data in json formate
    print(data)     #Print Response Data 

# delete_data()