import random
import sqlite3
from flask import render_template
from clear import clear
from sweater import app


@app.route('/user')
def user():
    database = sqlite3.connect('blog2.db')
    cursor = database.cursor()
    qoute_id = cursor.execute('SELECT id FROM data_quotes').fetchall()
    random_id = random.randrange(int(clear(qoute_id[0])), int(clear(qoute_id[-1])))
    random_id = str(random_id)
    quote = cursor.execute('SELECT quote FROM data_quotes WHERE id == ?', (random_id,)).fetchone()
    quote = clear(quote)
    author = cursor.execute('SELECT author FROM data_quotes WHERE id == ?', (random_id,)).fetchone()
    author = clear(author)
    quotes = [quote, author, '']
    return render_template('user.html', quotes=quotes)
