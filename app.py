from flask import Flask, request
import sqlite3
from dotenv import load_dotenv
from pathlib import Path
import os
from db import db_connect
from flask_bcrypt import bcrypt

app = Flask(__name__, instance_relative_config = True)

bcrypt(app)


inst_path = os.path.join(app.instance_path, "config.env")
load_dotenv(inst_path)
app.config["DATABASE"] = os.environ.get("DATABASE")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

#routes

@app("/login", method = "POST")
def login():
    username = request.form.get("username").strip()
    password = request.form.get("password")
    email = request.form.get("email").strip()

    conn = db_connect
    cursor = conn.cursor()
    sql = """INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)"""
    cursor.execute(sql, (username, email, bcrypt.generate_password_hash(password)))

    conn.commit()
    conn.close()
































app.cli.add_command(db.db_init_cli)

if __name__ == "__main__":
    app.run()
