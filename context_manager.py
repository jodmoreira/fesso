import sqlite3
import datetime

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS data (
                        id INTEGER PRIMARY KEY,
                        text TEXT,
                        timestamp DATETIME
                    )""")

    conn.commit()

def insert_data(text):
    query = "INSERT INTO data (text, timestamp) VALUES (?, ?)"
    cursor.execute(query, (text, datetime.datetime.now()))
    conn.commit()

def retrieve_data():
    query = "SELECT * FROM data WHERE timestamp >= date('now', '-1 day')"
    cursor.execute(query)
    return cursor.fetchall()


conn.close()