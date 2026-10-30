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

@app("/login", methods = ["GET, POST"])
def login():
    error = None

    try:
        username = request.form.get("username").strip()
        password = request.form.get("password")

        
        conn = db_connect()
        cursor = conn.cursor()
        sql = """SELECT username, password_hash FROM users WHERE username = ?"""
        cursor.execute(sql, (username, ))
        
        if username is None:
            error = "Wrong username"
        if password is None:
            error = "Wrong password"
        elif not (bcrypt.check_password_hash(password), password):
            error = "Wrong password"
        if error is None:
            session.clear()
            session["user"] = username

        conn.commit()
        conn.close()
    except:
        error = "Could not connect to database"
        return jsonify(error)

@app("/register", methods = ["GET", "POST"])
def register():
    error = None

    try:
        username = request.form.get("username").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password")

        if len(username) <3:
            error ="Username too short"
        if len(password) <6:
            error = "Password must be at least 6 characters"

        conn = db_connect()
        cursor = conn.cursor()

        sql = """INSERT INTO users (username, email, password_hash)
                VALUES (?,?,?)"""
        cursor.execute(sql, (username, email, bcrypt.generate_pass_hash(password).decode("utf-8")))

        conn.commit()
        conn.close()
    except:
        error = "Could not connect to database"
        return jsonify(error)






























app.cli.add_command(db.db_init_cli)

if __name__ == "__main__":
    app.run()
