#!/usr/bin/env python3

# Import the MongoClient class
from pymongo import MongoClient

# Connection URL and database name
url = 'mongodb://localhost:27017/'
dbName = 'admin'

# Create a MongoClient object
client = MongoClient(url)

# List all databases
dbList = client.list_database_names()

# Print the list of databases
print("Databases:")
for db in dbList:
    print(db)

# Close the client
client.close()
