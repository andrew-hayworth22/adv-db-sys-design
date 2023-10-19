from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://mhaywort:F4oggeRBz3RyDV38@example-cluster.3ykyd8t.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

shopping_list_db = client.shopping_list_db

def set_up_database() :
    shopping_list_db.drop_collection(shopping_list_db.items_collection)
    items_collection = shopping_list_db.items_collection

    for description in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes']:
        items_collection.insert_one({'description': description})

def get_items() :
    items_collection = shopping_list_db.items_collection
    items = items_collection.find({})
    return [ {"id": str(item['_id']), "description": item['description']} for item in list(items) ]

def add_item(description) :
    item_collection = shopping_list_db.items_collection
    item_collection.insert_one({'description': description})

def get_item(id) :
    item_collection = shopping_list_db.items_collection
    item = list(item_collection.find({ '_id': ObjectId(id) }))[0]
    return {"id": str(item['_id']), "description": item['description']};

def update_item(id, description) :
    item_collection = shopping_list_db.items_collection
    item_collection.update_one({'_id': ObjectId(id)}, {'$set': {'description': description}})

def delete_item(id) :
    item_collection = shopping_list_db.items_collection
    item_collection.delete_one({'_id': ObjectId(id)})

def test_set_up_database() :
    print("Testing set up database...")
    set_up_database()

    items = get_items()
    assert len(items) == 5

    descriptions = [item['description'] for item in items]
    for description in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes'] :
        assert description in descriptions

def test_get_items() :
    print("Testing get items...")
    items = get_items();

    assert type(items) is list
    assert len(items) > 0
    for item in items:
        assert type(item) is dict

        assert 'id' in item
        assert type(item['id']) is str

        assert 'description' in item
        assert type(item['description']) is str

def test_add_item() :
    print("Testing add item...")
    set_up_database()

    items = get_items();
    original_length = len(items)

    add_item("Mango")

    items = get_items();
    descriptions = [ item['description'] for item in items ]

    assert len(items) == original_length + 1
    assert "Mango" in descriptions

def test_get_item() :
    print("Testing get item...")
    set_up_database()

    items = get_items()

    for item in items :
        fetched_item = get_item(item["id"])
        assert type(fetched_item) is dict
        assert fetched_item["id"] == item["id"]
        assert fetched_item["description"] == item["description"]

def test_update_item() :
    print("Testing update item...")
    set_up_database()

    items = get_items()
    original_length = len(items)

    for item in items :
        update_item(item["id"], item["description"] + " UPDATED")
    
    items = get_items()
    assert len(items) == original_length

    descriptions = [item['description'] for item in items]
    for description in ['apples UPDATED', 'broccoli UPDATED', 'pizza UPDATED', 'tangerine UPDATED', 'potatoes UPDATED'] :
        assert description in descriptions

def test_delete_item() :
    print("Testing delete item...")
    set_up_database()

    items = get_items()
    original_length = len(items)

    item_to_delete = items[0]

    delete_item(item_to_delete["id"])

    items = get_items()
    descriptions = [ item["description"] for item in items ]

    assert len(items) == original_length - 1
    assert item_to_delete["description"] not in descriptions

if __name__ == "__main__" :
    test_set_up_database()
    test_get_items()
    test_add_item()
    test_get_item()
    test_update_item()
    test_delete_item()
    print("Done.")