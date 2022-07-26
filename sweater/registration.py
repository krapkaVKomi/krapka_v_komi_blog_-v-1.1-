import sqlite3
import random
import datetime
from flask import request, render_template
from sweater import app
from clear import clear
from werkzeug.security import generate_password_hash#, check_password_hash





@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        email_test = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.!@"
        erors = []

        if len(name) < 1 or len(name) > 33:
            erors.append('ПОМИЛКА!   логін не може бути пустим полем, та має бути не довшим 33 символів')
        else:
            pass

        database = sqlite3.connect('blog2.db')
        cursor = database.cursor()
        names_db = cursor.execute('SELECT name FROM users').fetchall() # масив з кортеджами 
        names = []
        for i in names_db:
            names.append(clear(i))
        a = False
        for i in names:
            if i == name:
                a = True
                break
        if a == True:
            erors.append('ПОМИЛКА!   цей логін зайнятий')
        else:
            pass

        for i in email:
            if i not in email_test:
                erors.append('ПОМИЛКА!   не коректні данні електронної пошти')
            else:
                pass
        if len(email) < 1 or len(email) > 33:
            erors.append('ПОМИЛКА!   email не може бути пустим полем, та має бути не довшим 33 символів')
        else:
            pass

        if len(password) < 6 or len(password) > 33:
            erors.append('ПОМИЛКА!   пароль не може бути коротшим 6 символів, та має бути не довшим 33 символів')
        else:
            pass
        if password2 != password:
            erors.append('ПОМИЛКА!   паролi в обох полях не співпадають')
        else:
            pass
        if len(erors) > 0:
            return render_template('registration.html', erors=erors)
        else:
            #
                
            password_hash = generate_password_hash(password)

            user_id = cursor.execute('SELECT id FROM users').fetchall()
            if len(user_id) != 0:
                id = str(user_id[-1])
                id = clear(id)
                new_id = str(int(id) + 1)
            else:
                id = '0'
            
            author_rating = 'test_rating'

            time = []
            a = str(datetime.datetime.now())
            for i in range(16):
                time.append(a[i])
            date = ''
            for i in time:
                date += i
            
            cursor.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)', (new_id, name, email, password_hash, date, author_rating))
            database.commit()
            
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
        return render_template('registration.html', erors='')        

        
    