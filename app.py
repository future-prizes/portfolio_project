from flask import Flask
import sqlite3
from dotenv import load_dotenv
from pathlib import Path
import os
import db

app = Flask(__name__, instance_relative_config = True)


inst_path = os.path.join(app.instance_path, "config.env")
load_dotenv(inst_path)
app.config["DATABASE"] = os.environ.get("DATABASE")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

#routes































app.cli.add_command(db.db_init_cli)

if __name__ == "__main__":
    app.run()
