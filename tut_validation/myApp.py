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

# get_data(2) # Get Single data using ID
# get_data()  # Get All Data

# Post Method:
def post_data():
    data = {
        'name': 'Prohit',
        'roll': 108,
        'city': 'guna',
    }
    # Convert Python data into Json Data
    json_data = json.dumps(data)   
    # Send Request Client to Server for post
    r = requests.post(url = URL, data = json_data)    
    # Extract Response Data in json formate
    data = r.json()   
    #Print Response Data 
    print(data)     


post_data() 

# Update Method:
def update_data():
    data = {
        'id':3,
        'name': 'Ram',
        'city': 'Guna',
    }
    # Convert Python data into Json Data
    json_data = json.dumps(data)   
    # Send Request Client to Server for Update
    r = requests.put(url=URL, data=json_data)    

    # Extract Response Data in json formate
    data = r.json()   
    #Print Response Data 
    print(data)     

# update_data()

# Delete Method:
def delete_data():
    data = {'id':5}
    json_data = json.dumps(data)   # Convert Python data into Json Data
    r = requests.delete(url=URL, data=json_data)    # Send Request Client to Server for delete

    data = r.json()   # Extract Response Data in json formate
    print(data)     #Print Response Data 

# delete_data()