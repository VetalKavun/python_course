import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(item):
	conn = sqlite3.connect("lite.db")
	cursor = conn.cursor()
	cursor.execute("DELETE FROM store WHERE item = ?", (item,))
	conn.commit()
	conn.close()


def update(item, quantity, price):
	conn = sqlite3.connect("lite.db")
	cursor = conn.cursor()
	cursor.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
	conn.commit()
	conn.close()

# insert("book1", 14, 12.4)
insert("book2", 34, 45.3)
insert("book3", 23, 34.5)
update("book2", 45, 49.3)
print(view())

