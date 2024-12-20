
import sqlite3
from display_manager import DisplayManager
# from user_management import UserManager

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
    

    def remove_user(self, user):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
            DELETE FROM users 
            WHERE user_name = (?) AND password = (?)
            ''', (user.username, user.password))



class Login:
    usermanager = UserManager('database/users.db')
    
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

            if Login.usermanager.user_exists(login_user):
                print(f"\n🏩 Welcome, {username}! You are now logged in.")
                return True, login_user

            else:
                attempts -= 1
                print(f"\n❌ Invalid credentials. {attempts} attempt(s) remaining.")

        print("\n⛔ Too many failed attempts. Returning to the main menu.")
        return False