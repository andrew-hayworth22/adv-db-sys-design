import sqlite3

connection = sqlite3.connect('shopping-list.db')

def set_up_database() :
    cursor = connection.cursor()

    try:
        cursor.execute("drop table list")
    except:
        pass

    cursor.execute("create table list(id integer primary key, description text)")

    for item in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes']:
        cursor.execute(f"insert into list (description) values ('{item}')")

    connection.commit()

def get_items() :
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id': row[0], 'description': row[1]} for row in rows ]
    return rows

def add_item(description) :
    cursor = connection.cursor()
    cursor.execute(f"insert into list(description) values ('{description}')")
    connection.commit()

def get_item(id) :
    cursor = connection.cursor()
    rows = cursor.execute(f"select id, description from list where id = {id}")
    rows = list(rows)
    rows = [ {'id': row[0], 'description': row[1]} for row in rows ]
    return rows[0];

def update_item(id, description) :
    cursor = connection.cursor()
    cursor.execute(f"update list set description = '{description}' where id = {id}")
    connection.commit()

def delete_item(id) :
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id = {id}")
    connection.commit()

def test_set_up_database() :
    print("Testing set up database...")
    set_up_database()

    items = get_items();
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
        assert type(item['id']) is int

        assert 'description' in item
        assert type(item['description']) is str

def test_add_item() :
    print("Testing add item...")
    set_up_database()

    items = get_items();
    original_length = len(items)

    add_item("Mango")

    items = get_items();
    descriptions = [ item["description"] for item in items ]

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