class MenuManager:
    menu_option_count = {
            'main_menu' : 3,
            'login_menu' : 5,
            'account_menu' : 3,
            'yes_no_menu' : 2
            }
    
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
