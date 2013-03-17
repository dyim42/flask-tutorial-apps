import sqlite3
con = sqlite3.connect("todo.db")
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS tasks")
    cur.execute("CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)")
    cur.execute('INSERT INTO tasks (name,due_date,priority,status) VALUES("Finish this tutorial", "3/16,2013", 10, 1)')
    cur.execute('INSERT INTO tasks (name,due_date,priority,status) VALUES("Start next tutorial", "3/16/2013", 10, 1)')
con.close()