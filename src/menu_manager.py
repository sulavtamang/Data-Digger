
class MenuManager:
    @staticmethod
    def display_main_menu():
        print("\n========================================")
        print("                 Main Menu               ")
        print("========================================")
        print("1️⃣ Register a new user")
        print("2️⃣ Log in")
        print("3️⃣ Exit")
        print("========================================")
    

    @staticmethod
    def display_login_menu():
        print("\n========================================")
        print("             Scraping Menu               ")
        print("========================================")
        print("1️⃣ Perform a new scrape")
        print("2️⃣ View scraped data")
        print("3️⃣ Account")
        print("4️⃣ Log Out")
        print("5️⃣ Exit")
        print("========================================")


    @staticmethod
    def display_account_centre_menu():
        print(f'\nWelcome to Account Centre.')

        print('1️⃣ Update usename and password ')
        print('2️⃣ Remove your account')
        print('3️⃣ Return back')



    @staticmethod
    def dynamic_user_choice(number_of_choices):
        choice = input(f"\n🕹️ Enter your choice (1-{number_of_choices}): ").strip()
        return choice
    


    menu_option_count = {
            'main_menu' : 3,
            'login_menu' : 5,
            'account_menu' : 3,
            'yes_no_menu' : 2
            }
    

    # main_menu = {
    #     'menu_name' : 'Main Menu',

    #     'options' : {
    #         '1' : 'register',
    #         '2' : 'log_in',
    #         '3' : 'exit'
    #     },

    #     'actions' : {
    #             '1' : lambda: UserManager.register_user(),
    #             '2' : lambda: Login.login(),    
    #             '3' : lambda: (DisplayManager.display_exit_message(), sys.exit())
    #     }
    # }


    # log_in_menu = {
    #     'menu_name' : 'Login Menu',
        
    #     'options' : {
    #         '1' : 'scrape',
    #         '2' : 'view_recently_scraped_data',
    #         '3' : 'account',
    #         '4' : 'log_out',
    #         '5' : 'exit'
    #     },

    #     'actions' : {
    #         '1' : lambda : Scraper.ask_for_search_item().scrape(),
    #         '2' : None,
    #         '3' : None,
    #         '4' : None,
    #         '5' : lambda: (DisplayManager.display_exit_message(), sys.exit())
    #     }
    # }
    

    # account_menu = {
    #     'menu_name' : 'Account Menu',

    #     'options' : {
    #         '1' : 'update user',
    #         '2' : 'remove user',
    #         '3' : 'log_out'
    #     },

    #     'actions' : {
    #         '1' : None,
    #         '2' : None,
    #         '3' : None
    #     }
    # }