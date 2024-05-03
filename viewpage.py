from pymongo import MongoClient

# Connecting to the MongoDB client
client = MongoClient('localhost', 27017, username='crawlerUser', password='securePassword123')

# Selecting the database
db = client['web_analysis']

# Accessing the 'page_analysis' collection
page_analysis = db.page_analysis

# Fetching and printing documents
for document in page_analysis.find():
    print(document)
