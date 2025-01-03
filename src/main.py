from db_operations import DatabaseManager
from user_management import User, UserManager, Login
from data_scraper import Scraper
from display_manager import DisplayManager 
from menu_manager import MenuManager
from action_manager import *

def main():
    DisplayManager.display_welcome_message()

    while True:
        MenuManager.display_main_menu()
        choice = MenuManager.dynamic_user_choice(MenuManager.menu_option_count['main_menu'])

        if not choice or choice not in ['1', '2', '3']:
            DisplayManager.display_invalid_choice_message()
        
        elif choice == '1':
            handle_registration()

        elif choice == '2':
            logged_in_user = handle_login()
            
            if logged_in_user:
                handle_logged_in_user(logged_in_user)
        
        elif choice == '3':
            DisplayManager.display_exit_message()
            return

if __name__ == '__main__':
    main()

