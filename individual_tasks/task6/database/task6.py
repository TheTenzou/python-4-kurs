import sqlite3
import os
import pprint

dirname = os.path.dirname(__file__)
db_name = os.path.join(dirname, 'computers.db')

connection = sqlite3.connect(db_name) 

cursor = connection.cursor()

cursor.execute('''
    create table if not exists cpu(
        id integer primary key autoincrement,
        name text,
        core_count integer,
        core_clock double,
        hash integer
    )
''')

cursor.execute('''
    create table if not exists gpu(
        id integer primary key autoincrement,
        name text,
        core_count integer,
        core_clock double,
        vram integer
    )
''')

cursor.execute('''
    create table if not exists computers(
        id integer primary key autoincrement,
        name text,
        cpu_id integer not null,
        gpu_id integer not null,

        foreign key (cpu_id)
            references cpu (id)
                on delete cascade
                on update no action,
        
        foreign key (gpu_id)
            references gpu (id)
                on delete cascade
                on update no action
    )
''')

cpu = [
    ('intel core i5-4570', 4, 3.4, 126),
    ('amd razen 5 3600', 6, 3.5, 148),
    ('эльбрус 5', 12, 2.1, 256)
]

cursor.executemany('insert into cpu values(null,?,?,?,?)', cpu)
 
gpu = [
    ('nvidia geforce gtx 1060', 1024, 1.6, 6148),
    ('nvidia geforce gtx 3080', 1224, 1.9, 8172)
]

cursor.executemany('insert into gpu values(null,?,?,?,?)', gpu)

pcs = [
    ('pc1', 1, 1),
    ('pc2', 3, 2),
    ('pc3', 2, 1)
]

cursor.executemany('insert into computers values(null,?,?,?)', pcs)

connection.commit()

cursor.execute("select * from cpu")
pprint.pprint(cursor.fetchall())

cursor.execute("select * from gpu")
pprint.pprint(cursor.fetchall())

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
pprint.pprint(cursor.fetchall())