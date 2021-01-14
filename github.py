from pymongo import MongoClient
import requests, datetime, pprint

simone_data = requests.get('https://api.github.com/users/sschneeberg')
jenny_data = requests.get('https://api.github.com/users/ruvvet')
jeremy_data = requests.get('https://api.github.com/users/jjuriz')

simone_obj = {
    'id': simone_data.json().get('id'),
    'name': simone_data.json().get('name'),
    'bio': simone_data.json().get('bio'),
    'location': simone_data.json().get('location'),
    'followers': simone_data.json().get('followers'),
    'date': datetime.date.day
}

jenny_obj = {
    'id': jenny_data.json().get('id'),
    'name': jenny_data.json().get('name'),
    'bio': jenny_data.json().get('bio'),
    'location': jenny_data.json().get('location'),
    'followers': jenny_data.json().get('followers'),
    'date': datetime.date.day
}

jeremy_obj = {
    'id': jeremy_data.json().get('id'),
    'name': jeremy_data.json().get('name'),
    'bio': jeremy_data.json().get('bio'),
    'location': jeremy_data.json().get('location'),
    'followers': jeremy_data.json().get('followers'),
    'date': datetime.date.day
}

print(simone_obj)
print(jenny_obj)
print(jeremy_obj)