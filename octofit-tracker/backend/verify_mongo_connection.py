from pymongo import MongoClient

try:
    # Connect to the MongoDB instance running on localhost:27017
    client = MongoClient("mongodb://localhost:27017/")
    # Run a command to check the connection
    server_info = client.server_info()
    print("MongoDB connection successful:", server_info)
except Exception as e:
    print("Failed to connect to MongoDB. Error details:")
    print(e)
