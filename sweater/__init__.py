import sqlite3
from flask import Flask



app = Flask(__name__)
database = sqlite3.connect('blog2.db')
cursor = database.cursor()
database.execute('CREATE TABLE IF NOT EXISTS {}(id, title, intro, text, date, user)' .format('data2'))
database.commit()
database.execute('CREATE TABLE IF NOT EXISTS {}(id, quote, author)' .format('data_quotes'))
database.commit()
database.execute('CREATE TABLE IF NOT EXISTS {}(id, name, email, password, date_registration, author_rating)' .format('users'))
database.commit()

from sweater import about, create_article, index, post, posts, user, registration, login