from pymongo import MongoClient
import requests, datetime, pprint

client = MongoClient()
db = client.github_users
db.drop_collection = 'classmates'
classmates = db.classmates

simone_data = requests.get('https://api.github.com/users/sschneeberg')
jenny_data = requests.get('https://api.github.com/users/ruvvet')
jeremy_data = requests.get('https://api.github.com/users/jjuriz')

simone_obj = {
    'id': simone_data.json().get('id'),
    'name': simone_data.json().get('name'),
    'bio': simone_data.json().get('bio'),
    'location': simone_data.json().get('location'),
    'followers': simone_data.json().get('followers'),
    'date': datetime.date.today().strftime('%Y-%m-%d')
}

jenny_obj = {
    'id': jenny_data.json().get('id'),
    'name': jenny_data.json().get('name'),
    'bio': jenny_data.json().get('bio'),
    'location': jenny_data.json().get('location'),
    'followers': jenny_data.json().get('followers'),
    'date': datetime.date.today().strftime('%Y-%m-%d')
}

jeremy_obj = {
    'id': jeremy_data.json().get('id'),
    'name': jeremy_data.json().get('name'),
    'bio': jeremy_data.json().get('bio'),
    'location': jeremy_data.json().get('location'),
    'followers': jeremy_data.json().get('followers'),
    'date': datetime.date.today().strftime('%Y-%m-%d')
}

print(simone_obj)
print(jenny_obj)
print(jeremy_obj)

classmates.insert_many([simone_obj, jenny_obj, jeremy_obj])
found_classmate = classmates.find_one({'id': simone_obj['id']})

print(found_classmate)