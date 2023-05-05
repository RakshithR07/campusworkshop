"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa7dik728r8862d0bg-a.oregon-postgres.render.com",
        database="todo_kq3s",
        user="todo_kq3s_user",
        password="cdVkjL7nRJV0yQvZ7r0a8wHdMWDFxX0S")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
