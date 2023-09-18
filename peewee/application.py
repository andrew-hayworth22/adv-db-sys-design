from bottle import route, run, template, redirect, post, request
import sqlite3
import database

connection = sqlite3.connect('shopping-list.db')

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    items = database.get_items()
    return template("list.tpl", shopping_list = items)

@route("/add")
def get_add():
    return template("add_item.tpl")

@post("/add")
def post_add():
    database.add_item(request.forms.get("description"))
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    item = database.get_item(id)
    return template("update_item.tpl", item=item)

@post("/update")
def post_update():
    id = request.forms.get("id")
    description = request.forms.get("description")
    database.update_item(id, description)

    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/list")

run(host='localhost', port=8080)