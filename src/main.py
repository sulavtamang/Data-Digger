from db_operations import DatabaseManager
from user_management import User, UserManager, Login
from data_scraper import Scraper
from display_manager import DisplayManager 
from menu_manager import MenuManager

usermanager = UserManager('database/users.db')

def main():
    DisplayManager.display_welcome_message()

    while True:
        MenuManager.display_main_menu()
        choice = MenuManager.dynamic_user_choice(MenuManager.menu_option_count['main_menu'])

        if choice == '1':
            name = input(f'\n🔑 Enter your name: ').strip()
            password = input(f'🔒 Set password: ').strip()

            user_register = User(name, password)

            usermanager.create_user_table()
            usermanager.register_user(user_register)

            DisplayManager.display_registration_successfull_message()

        elif choice == '2':
            logged_in, logged_in_user = Login.login()

            if logged_in:
                login_status = True

                while login_status:
                    MenuManager.display_login_menu()
                    choice = MenuManager.dynamic_user_choice(MenuManager.menu_option_count['login_menu'])

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

                        store_in_db = MenuManager.dynamic_user_choice(MenuManager.menu_option_count['yes_no_menu'])

                        if store_in_db == '1':
                            db_manager = DatabaseManager('database/extracted_items.db')
                            db_manager.create_table()
                            db_manager.insert_items(extracted_data)
                            print("\n✅ Data successfully stored in the database!")
                        else:
                            print("\n⚠️ Returning to previous menu.")

                    elif choice == '3':
                        MenuManager.display_account_centre_menu()
                        account_op_choice = MenuManager.dynamic_user_choice(MenuManager.menu_option_count['account_menu'])

                        if account_op_choice == '1':
                            print(f'\nChange your username and password')

                            new_username = input(f'\nEnter new username: ')
                            new_pword = input(f'Enter new password: ')

                            if not new_username or not new_pword:
                                print(f'\nUsername or password field cannot be empty.')
                            
                            usermanager.update_user(new_username, new_pword, logged_in_user)
                            print(f'\nSuccessfully updated')
                        
                        elif account_op_choice == '2':
                            print(f'\nAre you sure you want to delete your account?\n')

                            print(f'1. Yes')
                            print(f'2. No')

                            delete_user_choice = input(f'\nEnter your choice: ').strip()

                            while True:
                                if delete_user_choice == '2':
                                    break

                                elif delete_user_choice == '1':
                                    usermanager.remove_user(logged_in_user)
                                    print(f'\nUser {logged_in_user.username} successfully deleted!')
                                    break
                            break
                        
                        elif account_op_choice == '3':
                            break
                        break

                    elif choice == '4':
                        login_status = False
                        print("\n🔓 Logging out. Returning to the main menu.")

                    elif choice == '5':
                        DisplayManager.display_exit_message()
                        return

        elif choice == '3':
            DisplayManager.display_exit_message()
            return

if __name__ == "__main__":
    main()
