import sqlite3
import random
from flask import request, render_template
from sweater import app
from clear import clear
from werkzeug.security import check_password_hash


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        erors = []
        # перевірка логіна
        database = sqlite3.connect('blog2.db')
        cursor = database.cursor()
        names_db = cursor.execute('SELECT name FROM users').fetchall() 
        names = []
        for i in names_db:
            names.append(clear(i))
        a = False
        for i in names:
            if i == name:
                a = True
                break
        if a != True:
            erors.append('Помилка! акаунт не знайдений')
        else:
            pass
        # перевірка паролю
        password_hash = cursor.execute('SELECT password FROM users WHERE name == ?', (name,)).fetchone()
        password_hash = clear(password_hash)
        a = check_password_hash(password_hash, password)
        if a == False:
            erors.append('Помилка! пароль не вірний')
        else:
            pass

        if len(erors) > 0:
            return render_template('login.html', erors=erors)
        else:
            qoute_id = cursor.execute('SELECT id FROM data_quotes').fetchall()
            random_id = random.randrange(int(clear(qoute_id[0])), int(clear(qoute_id[-1])))
            random_id = str(random_id)
            quote = cursor.execute('SELECT quote FROM data_quotes WHERE id == ?', (random_id,)).fetchone()
            quote = clear(quote)
            author = cursor.execute('SELECT author FROM data_quotes WHERE id == ?', (random_id,)).fetchone()
            author = clear(author)
            quotes = [quote, author, name]
            return render_template('user.html', quotes=quotes)
            
    else:
        return render_template('login.html', erors='')
