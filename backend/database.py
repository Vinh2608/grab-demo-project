import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import json

uri = f"mongodb+srv://vinhluu2608:vuongtranlinhlinh123456789@cluster0.teog563.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
CLIENT = MongoClient(uri, server_api=ServerApi('1'))
CLIENT['grab-engineering-project']['Place_LatLong_API'].find_one_and_update({'id': 1},{"$unset": {'traffic_data': 1}})
CLIENT['grab-engineering-project']['Place_LatLong_API'].find_one_and_update({'id': 1},{"$unset": {'traffic_data': 1}})
CLIENT['grab-engineering-project']['Place_LatLong_API'].find_one_and_update(
    {'id': 1}, {"$unset": {'air_data': 1}})




