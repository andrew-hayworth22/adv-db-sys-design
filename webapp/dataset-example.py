import dataset

db = dataset.connect('sqlite:///pets.db')

table = db['pet']
data = [dict(item) for item in list(table.find())]
print(data)