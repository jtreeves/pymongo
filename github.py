from pymongo import MongoClient
import requests, datetime, pprint

response = requests.get('https://api.github.com/users/facebook')

print(response.json().get('bio'))