# -*- coding: utf-8 -*-
"""ДЗ№6_Шахров МС.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jHrmGkhtaD_T5PRPwKzWd9AElgxWveND
"""

from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

def create_db():
    connection = sqlite3.connect('gifts.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gifts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        gift_name TEXT NOT NULL,
        price REAL NOT NULL,
        status TEXT NOT NULL
    )
    ''')

    cursor.execute('SELECT COUNT(*) FROM gifts')
    if cursor.fetchone()[0] == 0:
        gifts_data = [
        ('Иван Иванович', 'Санки', 2000, 'куплен'),
        ('Ирина Сергеевна', 'Книга', 3000, 'не куплен'),
        ('Петр Петрович', 'Игрушка', 1500, 'куплен'),
        ('Анна Анатольевна', 'Конструктор', 2500, 'не куплен'),
        ('Сергей Сергеевич', 'Настольная игра', 1200, 'куплен'),
        ('Ольга Владимировна', 'Подарочная карта', 5000, 'не куплен'),
        ('Дмитрий Дмитриевич', 'Кофемашина', 8000, 'куплен'),
        ('Елена Викторовна', 'Смартфон', 30000, 'не куплен'),
        ('Алексей Алексеевич', 'Часы', 10000, 'куплен'),
        ('Мария Николаевна', 'Флешка', 800, 'не куплен')
        ]
        cursor.executemany('INSERT INTO gifts (full_name, gift_name, price, status) VALUES (?, ?, ?, ?)', gifts_data)
        connection.commit()

    connection.close()

def get_gifts():
    connection = sqlite3.connect('gifts.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM gifts')
    gifts = cursor.fetchall()
    connection.close()
    return gifts

@app.route('/')
def index():
    gifts = get_gifts()
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Список подарков</title>
    </head>
    <body>
        <h1>Список подарков</h1>
        <table border="1">
            <tr>
                <th>ID</th>
                <th>ФИО</th>
                <th>Название подарка</th>
                <th>Стоимость</th>
                <th>Статус</th>
            </tr>
            {% for gift in gifts %}
            <tr>
                <td>{{ gift[0] }}</td>
                <td>{{ gift[1] }}</td>
                <td>{{ gift[2] }}</td>
                <td>{{ gift[3] }}</td>
                <td>{{ gift[4] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    ''', gifts=gifts)

if __name__ == '__main__':
    create_db()
    from google.colab import output
    output.serve_kernel_port_as_window(5000)
    app.run(host='0.0.0.0', port=5000)