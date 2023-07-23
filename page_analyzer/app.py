import os
import logging
import requests
import psycopg2

from datetime import datetime
from psycopg2.extras import NamedTupleCursor
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from flask import (
    Flask,
    render_template,
    redirect,
    request,
    flash,
    url_for,
)

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET

@app.route("/")
def index():
    return render_template("index.html")