import sqlite3
from flask import render_template
from sweater import app


@app.route('/posts')
def posts():
    database = sqlite3.connect('blog2.db')
    cursor = database.cursor()
    art_title = cursor.execute('SELECT title FROM data2').fetchall()
    art_intro = cursor.execute('SELECT intro FROM data2').fetchall()
    art_time = cursor.execute('SELECT date FROM data2').fetchall()
    art_id = cursor.execute('SELECT id FROM data2').fetchall()
    article = []
    for i in range(len(art_title)-1, -1, -1):
        box = []
        box.append(art_title[i])
        box.append(art_intro[i])
        box.append(art_time[i])
        id = str(art_id[i])
        page_id = ''
        for i in id:
            if i != '(':
                if i != ')':
                    if i != ',':
                        if i != "'":
                            if i != '"':
                                page_id += i
        box.append(page_id)
        article.append(box)
    return render_template('posts.html', article=article)