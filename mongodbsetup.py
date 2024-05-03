from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure

def main():
    try:
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        print("Connected to MongoDB successfully.")

        # Create or switch to the new database
        db = client.web_analysis
        
        # Create collections and setup indexes
        setup_collections(db)
        
        # Setup users (optional)
        setup_users(client)

    except ConnectionFailure:
        print("Failed to connect to MongoDB. Check if the MongoDB service is running.")

def setup_collections(db):
    # Create the 'page_analysis' collection if it doesn't already exist
    if "page_analysis" not in db.list_collection_names():
        db.create_collection("page_analysis")
        print("Collection 'page_analysis' created.")
    
    # Creating indexes
    db.page_analysis.create_index([("url", ASCENDING)], unique=True)
    db.page_analysis.create_index([("crawl_date", ASCENDING)])
    db.page_analysis.create_index([("total_images", ASCENDING)])
    print("Indexes created on 'page_analysis' collection.")

def setup_users(client):
    # Switch to the admin database to create users
    admin_db = client.admin
    # Create a new user with readWrite role on the 'web_analysis' database
    admin_db.command("createUser", "crawlerUser",
                     pwd="securePassword123",
                     roles=[{"role": "readWrite", "db": "web_analysis"}])
    print("User 'crawlerUser' created with readWrite permissions.")

if __name__ == "__main__":
    main()
