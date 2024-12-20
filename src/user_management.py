
import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        print (f'{self.username}')


class UserManager:
    def __init__(self, db_path):
        self.db_path = db_path
    

    def create_user_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            password TEXT NOT NULL
            
            );
            ''')

    def user_exists(self, user):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(f'''
            SELECT 1 FROM users WHERE user_name = (?) AND password = (?) LIMIT 1;
            ''', (user.username, user.password))

            return bool(cursor.fetchone())
        
        
    def register_user(self, user):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            if self.user_exists(user):
                print(f"The user already exists in the database.")
                return
            
            cursor.execute('''
            INSERT INTO users (user_name, password)
            VALUES(?, ?)
            ''', (user.username, user.password))

            conn.commit()

            print(f"\nUser {user.username} successfully registered.")

    def update_user(self, new_username, new_password, user):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
            UPDATE users
            SET user_name = (?), password = (?)
            WHERE user_name = (?) AND password = (?)
            ''', (new_username, new_password, user.username, user.password))
