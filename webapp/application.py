from bottle import route, run, template

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
    return template('views/pets.tpl', pets=pets)


run(host='localhost', port=8080)