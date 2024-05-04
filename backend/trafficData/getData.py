import requests
import time
from PIL import Image
from detect import *
from datetime import datetime
#from urls import *

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def getData(path, db, collection):

    url = path[2]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    
    # Save image
    k = './trafficData/data/images/' + f'{path[0]}.jpg'
    timepoint = str(datetime.now())
    try:
        #print(requests.get(url, headers=headers).content)
        if (requests.get(url, headers=headers).headers['Content-Type']):
            with open(k, 'wb') as f:
                f.write(requests.get(url, headers=headers).content)
            #Resizing image
            im = Image.open(k)
            imB = im.resize((1024,576))
            imB.save(k)
            s = run(source=k, nosave=True)
            x = s.split()
            count, car, bike, truck, bus, person, motorbike = 0, 0, 0, 0, 0, 0, 0
            for part in x:
                if (count >= 3):
                    if ("car" in part):
                        car = int(temp)
                    elif ("truck" in part):
                        truck = int(temp)
                    elif ("bus" in part):
                        bus = int(temp)
                    elif ("motorcycle" in part):
                        motorbike = int(temp)
                    elif ("bicycle" in part):
                        bike = int(temp)
                temp = part
                count += 1

            data = {
                    "time": timepoint,
                    "car": car,
                    "bike": bike,
                    "truck": truck,
                    "bus": bus,
                    "person": person,
                    "motorbike": motorbike
            }
            print("data is: ", data)
            db['Place_LatLong_API'].find_one_and_update({"id": path[0]}, {"$push": {'traffic_data': data}})
            return data
    except:
        return {
            "location": path[1],
            "time": timepoint,
            "message": "cannot load data from this locaton"
        }
    
if __name__ == '__main__':

    # Create a new client and connect to the server

    uri = "mongodb+srv://vinhluu2608:vuongtranlinhlinh123456789@cluster0.teog563.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    CLIENT = MongoClient(uri, server_api=ServerApi('1'))

    db = CLIENT['grab-engineering-project']
    collection = db['Place_LatLong_API']
    paths = []
    
    for document in collection.find({"id": 1}):
        paths.append([document['id'], document['place'], document['request']])



        

