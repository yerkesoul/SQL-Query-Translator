import sqlite3

def create_sample_db():
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_name TEXT,
        order_date TEXT,
        followers_amount REAL
    )
    ''')

    cursor.execute('DELETE FROM orders')

    sample_data = [
        (1, 'Yerkezhan', '2023-07-01', 1.0),
        (2, 'Abdullayeva', '2023-07-15', 2.0),
        (3, 'Data Engineer', '2023-08-01', 3.0)
    ]
    cursor.executemany('INSERT INTO orders VALUES (?, ?, ?, ?)', sample_data)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_sample_db()
