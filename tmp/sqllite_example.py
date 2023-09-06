import sqlite3

connection = sqlite3.connect("sqlite-py.db")

cursor = connection.cursor()

cursor.execute("create table if not exists pet(id int primary key, name text, age int, kind_id int);")
cursor.execute("create table if not exists kind(id int primary key, name text, sound text);")

cursor.execute("delete from kind")
cursor.execute("insert into kind values(1, \"Cat\", \"Meow\")")
cursor.execute("select * from kind")
