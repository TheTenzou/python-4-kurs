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

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Name: {}</p>".format(text1))
print("<p>CPU: {}</p>".format(text2))
print("<p>GPU: {}</p>".format(text3))

cursor.execute('''
    select
        pc.name,
        cpu.name,
        gpu.name
    from 
        computers pc
        left join cpu on pc.cpu_id = cpu.id
        left join gpu on pc.gpu_id = gpu.id
''')

print('''
    <caption>Таблица размеров обуви</caption>
        <tr>
            <th>Название</th>
            <th>cpu</th>
            <th>gpu</th>
        </tr>
''')
for row in cursor.fetchall():
    print('<tr><td>34,5</td><td>3,5</td><td>36</td><td>23</td></tr>')

print("""</body>
        </html>""")