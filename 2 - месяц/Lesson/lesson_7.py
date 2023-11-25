import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_employee(conn, employee):
    sql = '''INSERT INTO employees 
    (full_name, salary, hobby, birth_date, is_married)
    VALUES (?, ?, ?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, employee)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_employees(conn):
    sql = '''SELECT * FROM employees'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_employees_by_salary(conn, salary_limit):
    sql = '''SELECT * FROM employees WHERE salary >= ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (salary_limit,))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def update_employee(conn, employee):
    sql = '''UPDATE employees SET salary = ?, is_married = ? 
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, employee)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_employee(conn, id_products):
    sql = '''DELETE from employees WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id_products,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(200) NOT NULL,
    salary FLOAT(8, 2) NOT NULL DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
)
'''

connection = create_connection('group_36.db')
if connection is not None:
    print('Successfully connected to DB!')
    # create_table(connection, sql_to_create_employees_table)
    # insert_employee(connection, ('John Smith', 1000, 'Programming', '2000-01-01', True))
    # insert_employee(connection, ('Mark Daniels', 1500.0, 'Football', '1999-01-02', False))
    # insert_employee(connection, ('Alex Brilliant', 2300.5, None, '1989-12-31', True))
    # insert_employee(connection, ('Diana Julls', 1800.0, 'Programming', '2005-01-22', True))
    # insert_employee(connection, ('Michael Corse', 1800.0, 'Football', '2001-09-17', True))
    # insert_employee(connection, ('Jack Moris', 2100.2, 'Programming', '2001-07-12', True))
    # insert_employee(connection, ('Viola Manilson', 1750.82, None, '1991-03-01', False))
    # insert_employee(connection, ('Joanna Moris', 1000.0, 'Football', '2004-04-13', False))
    # insert_employee(connection, ('Peter Parker', 2000.0, 'Programming', '2002-11-28', False))
    # insert_employee(connection, ('Paula Parkerson', 800.09, None, '2001-11-28', True))
    # insert_employee(connection, ('George Newel', 1320.0, 'Programming', '1981-01-24', True))
    # insert_employee(connection, ('Miranda Alistoun', 2500.55, 'Football', '1997-12-22', False))
    # insert_employee(connection, ('Valeria Hillton', 2000, 'Football', '1977-10-28', True))
    # insert_employee(connection, ('Jannet Miler', 2100.9, 'Programming', '1997-02-02', True))
    # insert_employee(connection, ('William Tokenson', 1500, None, '1999-12-12', False))
    # insert_employee(connection, ('Shanty Morani', 1200.6, None, '1989-08-13', False))
    # insert_employee(connection, ('Fiona Giordano', 900.12, 'Football', '1977-01-15', True))
    # select_all_employees(connection)
    # select_employees_by_salary(connection, 2300)

    # update_employee(connection, (1555, True, 2))
    delete_employee(connection, 2)
    connection.close()
