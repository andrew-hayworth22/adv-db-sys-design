from bottle import route, run, template
import sqlite3

@route('/')
def get_index():
    return template('views/index.tpl')

@route('/hello/<name>')
def get_hello(name):
    return template('views/hello.tpl', name=name)

pets = [
    {
        'id': 1,
        'name': 'Buddy',
        'kind': 'Cat'
    },
    {
        'id': 2,
        'name': 'Minnie',
        'kind': 'Cat'
    },
    {
        'id': 3,
        'name': 'Wiki',
        'kind': 'Dog'
    }
]

@route('/pets')
def get_pets():
    connection = sqlite3.connect("pets.db")
    cursor = connection.cursor()

    result = cursor.execute("select * from pet")
    data = result.fetchall()
    names = [item[0] for item in list(cursor.description)]

    return template('views/pets.tpl', names=names, data=data)


run(host='localhost', port=8080)