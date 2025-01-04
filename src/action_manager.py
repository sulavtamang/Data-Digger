from db_operations import DatabaseManager
from user_management import UserManager, Login
from data_scraper import Scraper
from display_manager import DisplayManager 
from menu_manager import MenuManager
import sys


def handle_registration():
    UserManager.register_user()
    DisplayManager.display_registration_successfull_message()


def handle_login():
    logged_in_user = Login.login()

    if logged_in_user:
        return logged_in_user
    
    return None



def handle_logged_in_user(logged_in_user):
    login_status = True

    while login_status:
        MenuManager.display_login_menu()
        choice = MenuManager.dynamic_user_choice(MenuManager.menu_option_count['login_menu'])

        if choice == '1':
            perform_scrape()

        elif choice == '2':
            view_scraped_data()

        elif choice == '3':
            user_removed = account_management(logged_in_user)
            if user_removed:
                break

        elif choice == '4':
            login_status = False
            print("\n🔓 Logging out. Returning to the main menu.")

        elif choice == '5':
            DisplayManager.display_exit_message()
            sys.exit()
        
        else:
            DisplayManager.display_invalid_choice_message()



def perform_scrape():
    print("\n=== 🎯 Data Scraping Interface ===")
    print("\nYou've chosen to scrape data. Let's get started!")

    search_term = input("\n🔍 Enter the item you want to search for: ").lower().strip()

    scraper = Scraper(search_term)
    scraper.fetch_page()
    scraper.parse_page()
    extracted_data = scraper.scrape()

    print(f'\n🔸 Displaying the extracted data for your search key "{search_term}":\n')
    scraper.display_extracted_data()

    store_in_db = MenuManager.dynamic_user_choice(MenuManager.menu_option_count['yes_no_menu'])

    if not store_in_db or store_in_db is not '1':
        DisplayManager.display_invalid_choice_message()

    elif store_in_db == '1':
        db_manager = DatabaseManager('../database/extracted_items.db')
        db_manager.create_table()
        db_manager.insert_items(extracted_data)
        print("\n✅ Data successfully stored in the database!")


#TODO
def view_scraped_data():
    pass



def account_management(logged_in_user):
    inside_account_centre = True
    while inside_account_centre:
        print(f'\nWelcome to Account Centre.')
        MenuManager.display_account_centre_menu()
        account_op_choice = MenuManager.dynamic_user_choice(MenuManager.menu_option_count['account_menu'])

        if account_op_choice == '1':
            print(f'\nChange your username and password')

            new_username = input(f'\nEnter new username: ')
            new_pword = input(f'Enter new password: ')

            if not new_username or not new_pword:
                print(f'\nUsername or password field cannot be empty.')
            
            UserManager.update_user(new_username, new_pword, logged_in_user)
            print(f'\nSuccessfully updated')
            return

        elif account_op_choice == '2':
            print(f'\nAre you sure you want to delete your account?\n')

            print(f'1. Yes')
            print(f'2. No')

            confirm = input(f'\nEnter your choice: ').strip()

            while True:
                if not confirm:
                    DisplayManager.display_invalid_choice_message()

                elif confirm == '2':
                    break

                elif confirm == '1':
                    UserManager.remove_user(logged_in_user)
                    print(f'\nUser {logged_in_user.username} successfully deleted!')
                    user_removed = True
                    return user_removed

        elif account_op_choice == '3':
            return