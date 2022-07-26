import datetime
import sqlite3
from flask import request, render_template
from sweater import app
from clear import clear


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        database = sqlite3.connect('blog2.db')
        cursor = database.cursor()
        art_id = cursor.execute('SELECT id FROM data2').fetchall()
        if len(art_id) != 0:
            id = str(art_id[-1])
            new_id = ''
            for i in id:
                if i != '(':
                    if i != ')':
                        if i != ',':
                            if i != "'":
                                if i != '"':
                                    new_id += i
            id = str(int(new_id) + 1)
        else:
            id = '0'

        user = 'test_name'
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        time = []
        a = str(datetime.datetime.now())
        for i in range(16):
            time.append(a[i])
        date = ''
        for i in time:
            date += i

        artitle = [title, intro, date, text]

        cursor.execute('INSERT INTO data2 VALUES(?, ?, ?, ?, ?, ?)', (id, title, intro, text, date, user))
        database.commit()
        return render_template('post.html', artitle=artitle)

    else:
        return render_template('create-article.html')