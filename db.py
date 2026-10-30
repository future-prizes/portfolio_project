import sqlite3
import click
from flask import current_app

def get_db_path():
    return current_app.config["DB_PATH"]

def db_init():
    with open("db.sql", "r", encoding = "utf-8") as s:
        schema = s.read()

    with sqlite3.connect(get_db_path()) as con:
        con.executescript(schema)

def db_connect():
    return  sqlite3.connect(get_db_path(), detect_types=sqlite3.PARSE_DECLTYPES)


@click.command('db_init')
def db_init_cli():
    db_init()
    print("Database started")
