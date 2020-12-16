import sqlite3
import datetime

def get_insert_format(table, params):
    req = "INSERT INTO {} VALUES (".format(table)
    for item in params:
        req += '"{}",'.format(item)
    req = req[0:-1] + ");"
    return req

class DataBase:
    """Создавать и использовать только в одной функции. Нельзя делать свойством другого класса."""
    def __init__(self):
        self.conn = sqlite3.connect("work.db")
        self.cursor = self.conn.cursor()
        self.create_all_tables()

    def create_all_tables(self):
        """Создает все необходимые таблицы"""
        # # Сотрудник
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS workers
        # (id INTEGER PRIMARY KEY AUTOINCREMENT,
        # name TEXT,
        # description TEXT,
        # contacts TEXT,
        # education TEXT,
        # salary_id INTEGER,
        # workplace_id INTEGER
        # );""")
        # # Место работы
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS workplace
        # (id INTEGER PRIMARY KEY AUTOINCREMENT,
        # monitor INTEGER,
        # level INTEGER,
        # build_id INTEGER
        # );""")
        # # Здание работы
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS building
        # (id INTEGER PRIMARY KEY AUTOINCREMENT,
        # address TEXT
        # );""")
        # # Должность
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS post
        # (id INTEGER PRIMARY KEY AUTOINCREMENT,
        # name TEXT,
        # salary REAL,
        # vacancy_rate TEXT,
        # salary_id INTEGER
        # );""")
        # # Сотрудник-Должность
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS worker_post
        # (worker_id INTEGER PRIMARY KEY,
        # post_id INTEGER PRIMARY KEY
        # );""")
        # # Зарплата
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS salary
        # (id INTEGER PRIMARY KEY AUTOINCREMENT,
        # count REAL,
        # prize_id INTEGER
        # );""")
        # # Премия
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS prize
        # (id INTEGER PRIMARY KEY AUTOINCREMENT,
        # progress_plan REAL,
        # month INTEGER
        # );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS bonus(
            bonus_id INT NOT NULL,
            month_number INT NOT NULL,
            percentage_of_completed INT NOT NULL,
            CONSTRAINT PK_Bonus PRIMARY KEY (bonus_id)
        );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS salary(
            salary_id INT NOT NULL,
            bonus_id INT NOT NULL,
            amount_in_month INT NOT NULL,
            CONSTRAINT FK_Bonus FOREIGN KEY (bonus_id) REFERENCES bonus(bonus_id),
            CONSTRAINT PK_Salary PRIMARY KEY (salary_id)
        );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS building(
            building_id INT NOT NULL,
            addres VARCHAR(255) NOT NULL,
            CONSTRAINT PK_Building PRIMARY KEY (building_id)
        );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS workplace(
            workplace_id INT NOT NULL,
            building_id INT NOT NULL,
            monitor_availability TEXT NOT NULL,
            floor INT NOT NULL,
            CONSTRAINT PK_Workplace PRIMARY KEY (workplace_id),
            CONSTRAINT FK_Building FOREIGN KEY (building_id) REFERENCES
            building(building_id)
        );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS worker(
            worker_id INT NOT NULL,
            workplace_id INT NOT NULL,
            salary_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            education VARCHAR(255) NOT NULL,
            contacts VARCHAR(255) NOT NULL,
            passport VARCHAR(255) NOT NULL,
            confidential_information INT NOT NULL,
            CONSTRAINT PK_Worker PRIMARY KEY (worker_id),
            CONSTRAINT FK_Salary FOREIGN KEY (salary_id) REFERENCES salary(salary_id),
            CONSTRAINT FK_Workplace FOREIGN KEY (workplace_id) REFERENCES
            workplace(workplace_id)
        );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS position(
            position_id INT NOT NULL,
            salary_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            wages INT NOT NULL,
            vacancy INT NOT NULL,
            CONSTRAINT PK_Position PRIMARY KEY (position_id),
            CONSTRAINT FK_Salary FOREIGN KEY (salary_id) REFERENCES salary(salary_id)
        );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS applicant(
            applicant_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            education VARCHAR(255) NOT NULL,
            contacts VARCHAR(255) NOT NULL,
            CONSTRAINT PK_Applicant PRIMARY KEY (applicant_id)
        );""")

    def execute_and_commit(self, request):
        self.cursor.execute(request)
        self.conn.commit()

    def telegram_channel_delete(self, channel_url):
        """Удаляет канал"""
        request_insert = ""
        self.execute_and_commit(request_insert)

    def telegram_stats_delete(self, channel_url):
        """Удаляет одну статистику канала"""
        request_insert = ""
        self.execute_and_commit(request_insert)