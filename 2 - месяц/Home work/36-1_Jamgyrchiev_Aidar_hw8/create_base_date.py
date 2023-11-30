import sqlite3


def create_connection(countries):
    conn = None
    try:
        conn = sqlite3.connect(countries)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_table(conn, countries):
    sql = '''INSERT INTO countries (title) VALUES (?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, countries)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_table_cities(conn, countries):
    sql = '''INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, countries)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_table_students(conn, countries):
    sql = '''INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, countries)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


sql_countries_table = '''
CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT(200) NOT NULL
    )
'''

sql_cities_table = '''
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT(200) NOT NULL,
    area FLOAT DEFAULT 0,
    country_id INTEGER, 
    FOREIGN KEY(country_id) REFERENCES countries (id)
    )
'''

sql_students_table = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT(200) NOT NULL,
    last_name TEXT(200) NOT NULL,
    city_id INTEGER, 
    FOREIGN KEY(city_id) REFERENCES cities (id)
    )
'''

connection = create_connection('base_date_students')
if connection is not None:
    # print('Successfully connected to db')
    # create_table(connection, sql_cities_table)
    # create_table(connection, sql_countries_table)
    # create_table(connection, sql_students_table)
    # insert_table_students(connection, ('Nazarbek', 'Tajibaev', 1))
    # insert_table_students(connection, ('Syrga', 'Taalaibekova', 1))
    # insert_table_students(connection, ('Mairambek', 'Nurbekov', 2))
    # insert_table_students(connection, ('Baktybek', 'Sabyrov', 2))
    # insert_table_students(connection, ('Hanzada', 'Omorova', 3))
    # insert_table_students(connection, ('Aidar', 'Jamgyrchiev', 3))
    # insert_table_students(connection, ('Almaz', 'Abdiev', 4))
    # insert_table_students(connection, ('Elbars', 'Asykbelov', 4))
    # insert_table_students(connection, ('Amantai', 'Borubaev', 5))
    # insert_table_students(connection, ('Ramazan', 'Kurmanaliev', 5))
    # insert_table_students(connection, ('Muhammed', 'Beishebaev', 6))
    # insert_table_students(connection, ('Jazeera', 'Temirova', 6))
    # insert_table_students(connection, ('Yrysbek', 'Kurmanbekov', 7))
    # insert_table_students(connection, ('Isabek', 'Bakirov', 7))
    # insert_table_students(connection, ('Bolot', 'Samidinov', 8))
    # insert_table_cities(connection, ('Berlin', 891.85, 1))
    # insert_table_cities(connection, ('Hamburg', 755.22, 1))
    # insert_table_cities(connection, ('Munich', 310.43, 1))
    # insert_table_cities(connection,  ('Bishkek', 169.9, 2))
    # insert_table_cities(connection, ('Osh', 182.6, 2))
    # insert_table_cities(connection, ('Tokyo', 2187.66, 3))
    # insert_table_cities(connection, ('Osaka', 225.21, 3))
    # insert_table_cities(connection, ('Kyoto', 827.83, 3))
    # insert_table(connection, ('Germany',))
    # insert_table(connection, ('Kyrgyzstan',))
    # insert_table(connection, ('Tokyo',))
    connection.close()


def print_cities():
    try:
        conn = sqlite3.connect('base_date_students')
        cursor = conn.cursor()

        cursor.execute('SELECT id, title FROM cities')
        cities = cursor.fetchall()

        print("Список городов:")
        for city in cities:
            print(f"{city[0]}. {city[1]}")

        conn.close()
    except sqlite3.Error as e:
        print(e)


def find_students_by_city(city_id):
    sql = '''SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                      FROM students
                      INNER JOIN cities ON students.city_id = cities.id
                      INNER JOIN countries ON cities.country_id = countries.id
                      WHERE cities.id = ?'''

    print(f"Ученики в выбранном городе:")
    try:
        conn = sqlite3.connect('base_date_students')
        cursor = conn.cursor()
        cursor.execute(sql, (city_id,))
        students = cursor.fetchall()
        conn.close()

        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, "
                f"Город: {student[3]}, Площадь города: {student[4]}")

    except sqlite3.Error as e:
        print(e)


while True:
    print(f"\nВы можете отобразить список учеников по выбранному id города из "
          f"перечня городов ниже, для выхода из программы введите 0:")
    print_cities()
    selected_city_id = input("Введите id города: ")

    if selected_city_id == '0':
        break

    try:
        selected_city_id = int(selected_city_id)
        find_students_by_city(selected_city_id)
    except ValueError:
        print("Пожалуйста, введите целочисленный id города.")
