import pymongo

DATABASE = "csc1033"
COLLECTION = "online_retail"

# connect to mongodb server: USERNAME, PASSWORD, HOST, PORT, DATABASE
client = pymongo.MongoClient("mongodb://csc1033:csc1033@cs-mongodb06.ncl.ac.uk:27017/?authSource=admin")
print(client.list_database_names())

# connect to database
db = client[DATABASE]

print(db.name, ",", db.list_collection_names())

# connect to database collection
col = db[COLLECTION]
print(col.name, ",", col.estimated_document_count())

# create query
# query = {"Invoice": 489434}

# more "complex" query
# query = {"$or": [{"Invoice": 489434}, {"Country": "France"}]}

# ex 1
# query = {"Description": "Edwardian Toilet Roll Unit".upper()}

# ex 2
# query = {"Price": {"$gt": 10}}

# ex 3
# query = {"Customer ID": 14000}

# ex 4
# query = {"Quantity": {"$lt": 6}}

# ex 5
query = {"Country": "United Kingdom", "Quantity": {"$lt": 10}}

# run query on collection
doc = col.find(query)

# print results of query
for record in doc:
    print(record)

"""
# the following were attempts at sanity checks to ensure the database was READ_ONLY
# all returns a "pymongo.errors.OperationFailure: not authorized on test_database to execute command ..." error

# attempt to create new database
db = client["test_database"]

new_record = {"Invoice": 489434,
              "StockCode": 85048,
              "Description": "Testing if this works.",
              "Quantity": 1,
              "InvoiceDate": "01/12/2019 07:45",
              "Price": 6.99,
              "Customer ID": 13085,
              "Country": "United Kingdom"}

# attempt to create new collection
test_col = db["test_col1"]
w = test_col.insert_one(new_record)

# try inserting new record
db = client[DATABASE]
x = col.insert_one(new_record)
doc = col.find(query)

for record in doc:
    print(record)

# try deleting a record
y = col.delete_one(new_record)
doc = col.find(query)

for record in doc:
    print(record)

# try creating a new collection
new_col = db["test_col2"]
z = new_col.insert_one(new_record)
doc = new_col.find(query)

for record in doc:
    print(record)
"""
