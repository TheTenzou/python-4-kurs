#!/usr/bin/env python3
import cgi
import html
import sys
import codecs
import sqlite3
import os

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

dirname = os.path.dirname(__file__)
db_name = os.path.join(dirname, 'computers.db')

form = cgi.FieldStorage()
text1 = form.getfirst("NAME")
text2 = form.getfirst("CPU")
text3 = form.getfirst("GPU")
text1 = html.escape(text1)
text2 = html.escape(text2)
text3 = html.escape(text3)

connection = sqlite3.connect(db_name)
cursor = connection.cursor()

cursor.execute(
    'insert into computers values(null,?,?,?)',
    (text1, text2, text3)
)
connection.commit()

print("Content-type: text/html\n")
print(
    """
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Обработка данных форм</title>
    </head>
    <body>
    """
)

print("<h1>Обработка данных форм!</h1>")
print("<p>Name: {}</p>".format(text1))
print("<p>CPU: {}</p>".format(text2))
print("<p>GPU: {}</p>".format(text3))

cursor.execute(
    '''
        select
            pc.name,
            cpu.name,
            gpu.name
        from 
            computers pc
            left join cpu on pc.cpu_id = cpu.id
            left join gpu on pc.gpu_id = gpu.id
    '''
)

print(
    '''
    <table border="1">
        <caption>Персональный компьютеры</caption>
            <tr>
                <th>Название</th>
                <th>cpu</th>
                <th>gpu</th>
            </tr>
    '''
)

for name, cpu, gpu in cursor.fetchall():
    print(
        f'''
        <tr>
            <td>{name}</td>
            <td>{cpu}</td>
            <td>{gpu}</td>
        </tr>
        '''
    )

print(
    """
            </table>
        </body>
    </html>
    """
)