import sqlite3
import click



def db_init():
    with open("db.sql", "r", encoding = "utf-8") as s:
        schema = s.read()

    with sqlite3.connect(".\\instance\\task.db") as con:
        con.executescript(schema)

def db_connect():
    try:
        with sqlite3.connect(".\\instance\\task.db", detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            return conn

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)

@click.command('db_init')
def db_init_cli():
    db_init()
    print("Database started")
