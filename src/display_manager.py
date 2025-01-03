
class DisplayManager:
    @staticmethod

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
    
    @staticmethod
    def display_login_message():
        print("\n========================================")
        print("                 Login                   ")
        print("========================================")
        print("\nPlease log in to access your account.")
    
    @staticmethod
    def display_registration_successfull_message():
        print("\n✅ Registration successful! Please log in.")

    
    @staticmethod
    def display_exit_message():
        print("\n🚪 Exiting the program. Goodbye!")

    
    @staticmethod
    def display_invalid_choice_message():
        print('\nInvalid choice!')