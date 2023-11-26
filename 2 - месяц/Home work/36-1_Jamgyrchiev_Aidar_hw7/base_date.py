import sqlite3


def create_connection(hw_db):
    conn = None
    try:
        conn = sqlite3.connect(hw_db)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(conn, products):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_products_quantity(conn, products):
    sql = '''UPDATE products SET quantity = ?
    WHERE id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_products_price(conn, products):
    sql = '''UPDATE products SET price = ?
    WHERE id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(conn, id_products):
    sql = '''DELETE from products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id_products,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products(conn, products):
    sql = '''SELECT * FROM products WHERE price >= ? AND quantity > ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_title(conn):
    sql = '''SELECT * FROM products WHERE product_title LIKE 'ba%'
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        row_list = cursor.fetchall()

        for row in row_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT(200) not NULL,
    price FLOAT(8, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
    )
'''


connection = create_connection('hw_db')
if connection is not None:
    print('Successfully connected to DB')
    # create_table(connection, sql_products_table)
    # insert_products(connection, ('banana', 270, 6))
    # insert_products(connection, ('apple', 180, 15))
    # insert_products(connection, ('milk', 210, 20))
    # insert_products(connection, ('bread', 180, 24))
    # insert_products(connection, ('honey', 540, 1))
    # insert_products(connection, ('rice', 300, 7))
    # insert_products(connection, ('chicken', 360, 9))
    # insert_products(connection, ('carrots', 150, 15))
    # insert_products(connection, ('tomatoes', 250, 21))
    # insert_products(connection, ('buckwheat', 400, 13))
    # insert_products(connection, ('salmon', 1000, 5))
    # insert_products(connection, ('tea', 160, 20))
    # insert_products(connection, ('yogurt', 240, 14))
    # insert_products(connection, ('oranges', 400, 25))
    # insert_products(connection, ('cheese', 280, 18))
    # update_products_quantity(connection, (3, 2))
    # update_products_price(connection, (380, 14))
    # delete_products(connection, 10)
    # select_all_products(connection)
    select_products(connection, (200, 5))
    # select_products_title(connection)
    connection.close()
