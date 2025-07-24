import json # no installation required, built-in

#! JSON from string
string = '''
{
    "people": [
        {
            "name": "Samin",
            "age": 20,
            "skills": ["python", "html/css", "c/c++"],
            "unemployed": true
        },
        {
            "name": "Sadik",
            "age": 22,
            "skills": ["django", "javascript"],
            "unemployed": false
        }
    ]
}
'''

print("Type:",type(string)) # a python string but formatted like valid json
print(string)

data = json.loads(string) # Convert from JSON to Python
print("\nType:",type(data)) # converts certain json types into corresponding python types
print(data) # json object becomes a python dictionary

print("\n['people'] Type:",type(data['people'])) # json array becomes a python list
print(data['people'][0]['unemployed'], end=' ') # json boolean True/False from true/false

print("Names:")
for person in data['people']: # iterating through json array normally like a python list
    print(person['name'])
    del person['skills'][1]

print("\nPython None = JSON", json.dumps(None)) # Convert from Python to JSON
new_string = json.dumps(data, indent=2, sort_keys=True) # indent and sort_keys are optional
print("\nJSON from Python:", new_string)
# indent is a number of spaces to per level
# sort_keys will sort the keys alphabetically


#! JSON from file
with open('testData.json') as f:
    data = json.load(f) # Convert JSON from a file to Python

print("\nID and Names from File:")
for info in data:
    print(info['id'] ,":", info['name'])
    if 'language' in info: del info['language']

with open('testData.json', 'w') as f:
    json.dump(data, f, indent=4) # Convert Python to JSON and write to a file
    # format = json.dump(what_to_dump, where_to_dump, optional_args)


#! JSON from API
import urllib.request # no installation required, built-in
# Send GET request to public API and receive response
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users/1") as res:
    data = res.read() # Read raw bytes from response
    print(f"\nSingle User Data from API (raw JSON bytes):\n{data}")
    print(f"\nSingle User Data from API (converted to python dict):\n{json.loads(data)}")
    print(f"\nCleaned User Data from API:\n{json.dumps(json.loads(data), indent=2)}")

import requests # not built-in, but more popular and easier for real use
res = requests.get("https://jsonplaceholder.typicode.com/users") # Send GET request to API
if res.status_code == 200: # Check if request was successful
    users = res.json() # res.json() converts JSON response to Python list of dicts
    print(f"\nAccessed Data from API:\n{users[0]}")
    
    addresses = dict() # taste of real world use: (usually needs to go deep into nested data)
    for user in res.json(): # json data can be iterated & accessed like a python list 
        lati, longi = user["address"]["geo"]["lat"], user["address"]["geo"]["lng"] # Accessing nested fields
        addresses[user["username"]] = user["address"]["city"] + " (" + lati + ", " + longi + ")"
    print("\nAddresses from API:")
    for entry in addresses.items(): print(entry)