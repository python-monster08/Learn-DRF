import requests, json

URL = "http://127.0.0.1:8000/create_student/"

# Create Student Data by Another Applications
data = {
    'name':'Ravina',
    'roll':'104',
    'city':'11',
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)

data  = r.json()
print(data)
