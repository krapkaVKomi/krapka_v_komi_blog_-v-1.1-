import sqlite3
from flask import render_template
from clear import clear
from sweater import app


@app.route('/posts/<string:id>')
def post(id):
    database = sqlite3.connect('blog2.db')
    cursor = database.cursor()
    art_title = cursor.execute('SELECT title FROM data2 WHERE id == ?', (id,)).fetchone()
    art_title = clear(art_title)
    art_intro = cursor.execute('SELECT intro FROM data2 WHERE id == ?', (id,)).fetchone()
    art_intro = clear(art_intro)
    art_time = cursor.execute('SELECT date FROM data2 WHERE id == ?', (id,)).fetchone()
    art_time = clear(art_time)
    art_text = cursor.execute('SELECT text FROM data2 WHERE id == ?', (id,)).fetchone()
    art_text = clear(art_text)
    artitle = [art_title, art_intro, art_time, art_text]
    return render_template('post.html', artitle=artitle)