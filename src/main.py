from db_operations import DatabaseManager
from user import User, UserManager
from data_scraper import Scraper
from bs4 import BeautifulSoup
import requests
import sqlite3

def display_welcome_message():
    print("############################################")
    print("     🎶 Welcome to AudioShop Scraper! 🎶")
    print("############################################")
    print("\nHello, and thank you for choosing our application!\n")
    print("This tool allows you to:")
    print("✨ Search for musical instruments and audio gear.")
    print("✨ Save and manage your search results in a database.")
    print("✨ Perform user account operations like registration and login.\n")
    print("🔑 Please register or log in to access all features.")
    print("🎯 Let's get started!")
    print("\n############################################\n")

def display_menu():
    print("\n========================================")
    print("                 Main Menu               ")
    print("========================================")
    print("1️⃣ Register a new user")
    print("2️⃣ Log in")
    print("3️⃣ Exit")
    print("========================================")

def login():
    print("\n========================================")
    print("                 Login                   ")
    print("========================================")
    print("\nPlease log in to access your account.")
    attempts = 3

    while attempts > 0:
        username = input("🔑 Username: ").strip()
        password = input("🔒 Password: ").strip()

        login_user = User(username, password)
        usermanager_login = UserManager('database/users.db')

        if not username or not password:
            print("\n❌ Both fields are required. Try again.")
            continue

        if usermanager_login.authenticate_user(login_user):
            print(f"\n🏩 Welcome, {username}! You are now logged in.")
            return True

        else:
            attempts -= 1
            print(f"\n❌ Invalid credentials. {attempts} attempt(s) remaining.")

    print("\n⛔ Too many failed attempts. Returning to the main menu.")
    return False

def main():
    display_welcome_message()

    while True:
        display_menu()

        choice = input(f'\n🕹️ Please enter your choice from the menu: ')

        if choice == '1':
            name = input(f'\n🔑 Enter your name: ')
            password = input(f'🔒 Set password: ')

            user_register = User(name, password)
            usermanager_register = UserManager('database/users.db')
            usermanager_register.create_user_table()
            usermanager_register.register_user(user_register)
            print("\n✅ Registration successful! Please log in.")

        elif choice == '2':
            if login():
                login_status = True

                while login_status:
                    print("\n========================================")
                    print("             Scraping Menu               ")
                    print("========================================")
                    print("1️⃣ Perform a new scrape")
                    print("2️⃣ View scraped data")
                    print("3️⃣ Log out")
                    print("4️⃣ Exit program")
                    print("========================================")

                    choice = input("\n🕹️ Enter your choice (1-4): ").strip()

                    if choice == '1':
                        print("\n=== 🎯 Data Scraping Interface ===")
                        print("\nYou've chosen to scrape data. Let's get started!")

                        search_term = input("\n🔍 Enter the item you want to search for: ").lower().strip()

                        scraper = Scraper(search_term)
                        scraper.fetch_page()
                        scraper.parse_page()
                        extracted_data = scraper.scrape()

                        print(f'\n🔸 Displaying the extracted data for your search key "{search_term}":\n')
                        scraper.display_extracted_data()
                    
                    elif choice == '2':
                        print(f'\n🔸 Displaying the recently scraped data:\n{extracted_data}')

                        print(f'\nDo you want to store the data in the database?\n1️⃣ Yes\n2️⃣ No')

                        store_in_db = input(f'\n🕹️ Enter your choice: ')

                        if store_in_db == '1':
                            db_manager = DatabaseManager('database/extracted_items.db')
                            db_manager.create_table()
                            db_manager.insert_items(extracted_data)
                            print("\n✅ Data successfully stored in the database!")
                        else:
                            print("\n⚠️ Returning to previous menu.")

                    elif choice == '3':
                        login_status = False
                        print("\n🔓 Logging out. Returning to the main menu.")

                    elif choice == '4':
                        print("\n🚪 Exiting the program. Goodbye!")
                        return

        elif choice == '3':
            print("\n🚪 Exiting the program. Goodbye!")
            return

if __name__ == "__main__":
    main()
