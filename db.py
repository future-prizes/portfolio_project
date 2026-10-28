import sqlite3



def db_init():
    with open("db.sql", "r", ecoding = "utf-8") as s:
        schema = s.read()

    with sqlite3.connect(".\\instance\\task.db") as con:
        con.executescript(schema)

def db_connect():
    con = sqlite3.connect(".\\instance\\task.db")
    cursor = con.cursor()

    con.close()