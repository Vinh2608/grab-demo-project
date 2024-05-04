
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://vinhluu2608:vuongtranlinhlinh123456789@cluster0.teog563.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
paths = []
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['grab-engineering-project']
collection = db['Place_LatLong_API']

for document in collection.find():
    paths.append((document['id'], document['place'], document['request']))
print(paths)
    
