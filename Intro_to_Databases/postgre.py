import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='barsKii..007' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='barsKii..007' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES ('{}', {}, {})".format(item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='barsKii..007' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='barsKii..007' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item='{}'".format(item))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='barsKii..007' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity={}, price={} WHERE item='{}'".format(quantity, price, item))
    conn.commit()
    conn.close()


#create_table()
#insert("Wine Glass", 11, 5)
#delete("Coffee Cup")
#update(22, 12.99, "Wine Glass")
print(view())
