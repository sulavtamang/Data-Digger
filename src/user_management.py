
import sqlite3
from display_manager import DisplayManager

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        print (f'{self.username}')


class UserManager:
    db_path = '../database/users.db'
    
    @staticmethod
    def create_user_table():
        with sqlite3.connect(UserManager.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            password TEXT NOT NULL
            
            );
            ''')

    @staticmethod
    def user_exists(user):
        with sqlite3.connect(UserManager.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(f'''
            SELECT 1 FROM users WHERE user_name = (?) AND password = (?) LIMIT 1;
            ''', (user.username, user.password))

            return bool(cursor.fetchone())
        
    @staticmethod
    def register_user():
        name = input(f'\n🔑 Enter your name: ').strip()
        password = input(f'🔒 Set password: ').strip()

        user = User(name, password)

        UserManager.create_user_table()

        with sqlite3.connect(UserManager.db_path) as conn:
            cursor = conn.cursor()

            if UserManager.user_exists(user):
                print(f"The user already exists in the database.")
                return
            
            cursor.execute('''
            INSERT INTO users (user_name, password)
            VALUES(?, ?)
            ''', (user.username, user.password))

            conn.commit()

            print(f"\nUser {user.username} successfully registered.")


    @staticmethod
    def update_user(new_username, new_password, user):
        with sqlite3.connect(UserManager.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
            UPDATE users
            SET user_name = (?), password = (?)
            WHERE user_name = (?) AND password = (?)
            ''', (new_username, new_password, user.username, user.password))

    
    @staticmethod
    def remove_user(user):
        with sqlite3.connect(UserManager.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
            DELETE FROM users 
            WHERE user_name = (?) AND password = (?)
            ''', (user.username, user.password))


class Login:
    
    @staticmethod
    def login():
        DisplayManager.display_login_message()
        attempts = 3

        while attempts > 0:
            username = input("🔑 Username: ").strip()
            password = input("🔒 Password: ").strip()

            login_user = User(username, password)

            if not username or not password:
                print("\n❌ Both fields are required. Try again.")
                continue

            if UserManager.user_exists(login_user):
                print(f"\n🏩 Welcome, {username}! You are now logged in.")
                return login_user

            else:
                attempts -= 1
                print(f"\n❌ Invalid credentials. {attempts} attempt(s) remaining.")

        print("\n⛔ Too many failed attempts. Returning to the main menu.")
        return