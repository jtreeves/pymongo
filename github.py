from pymongo import MongoClient
import requests, datetime, pprint

simone_data = requests.get('https://api.github.com/users/facebook')
jenny_data = requests.get('https://api.github.com/users/facebook')
alan_data = requests.get('https://api.github.com/users/facebook')

simone_obj = {
    'bio': simone_data.json().get('bio')
}

jenny_obj = {
    'bio': simone_data.json().get('bio')
}

alan_obj = {
    'bio': simone_data.json().get('bio')
}

print(simone_obj)
print(jenny_obj)
print(alan_obj)