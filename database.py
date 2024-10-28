from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect_mongodb():
    uri = "mongodb+srv://trongkha08022k4:tk08022004@cluster0.ni1bo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        return client
    except Exception as e:
        print(e)
        return None
