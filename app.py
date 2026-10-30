from flask import Flask, request, session, jsonify
import sqlite3
from dotenv import load_dotenv
from pathlib import Path
import os
from db import db_connect, db_init_cli
from flask_bcrypt import Bcrypt

app = Flask(__name__, instance_relative_config = True)

bcrypt = Bcrypt(app)
#config

config_path = os.path.join(app.instance_path, "config.env")
load_dotenv(config_path)
db_name = os.environ.get("DB_NAME")
app.config["DB_PATH"] = os.path.join(app.instance_path, db_name)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


#routes

@app.route("/login", methods = ["GET", "POST"])
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

@app.route("/register", methods = ["GET", "POST"])
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
        cursor.execute(sql, (username, email, bcrypt.generate_password_hash(password).decode("utf-8")))

        conn.commit()
        conn.close()
        return f"User {username} registered"
    except Exception as e:
        return jsonify(e)
    except sqlite3.Error as e:
        return jsonify(e)

@app.route("/show-all", methods = ["GET"])
def show_all():
    error = None
    
    try:
    
        conn = db_connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM users"""
        result = cursor.execute(sql)
        rows = result.fetchall()

        conn.commit()
        conn.close()
        print(rows)
        return jsonify(rows)
    except:
        error = "Could not connect to database"
        return jsonify(error)




























app.cli.add_command(db_init_cli)

if __name__ == "__main__":
    app.run()
