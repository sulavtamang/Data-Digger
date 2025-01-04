
# 1. Project Overview

This project, "Music Gear Digger", is a web scraping tool designed to fetch data from 
[Audioshopnepal](https://audioshopnepal.com) about audio gear and musical instruments. 
It features user authentication, data management in a database, and a user-friendly menu interface for operations.


# 2. Features

- 🎯 **Scraping:** Search for specific items and extract data
- 💾 **Data Management:** Save scraped data into a SQLite database.
- 🔑 **User Management:** Register, log in, update, and delete user accounts.
- 📊 **View Scraped Data:** Display the most recently scraped results.


# 3. Technologies Used
- **Programming Language:** *Python*

- **Libraries:**
    - *requests* and *BeautifulSoup* for web scraping
    - *sqlite3* for database management

- **Other Tools:** *Git* for version control


# 4. Setup and Installation
- **Prerequisites**
    1. Python 3.x installed
    2. pip for managing Python packages

- **Steps**
    1. Clone the repository:
    ```
    git clone git@github.com:sulavtamang/Music-Gear-Digger-audioshopnepal.git
    cd 'Music-Gear-Digger-audioshopnepal'
    ```

    2. Create and activate virtual environment:
    ```
    python -m venv env
    source env/bin/activate  # Linux/Mac
    env\Scripts\activate     # Windows

    ```

    3. Install dependencies:
    ```
    pip install -r requirements.txt

    ```

    4. Ensure the database files are in correct location:
    ```
    Music-Gear-Digger-audioshopnepal/
    ├── database/
    │   ├── users.db
    |   |── extractd_items.db
    ├── src/
    │   ├── main.py
    │   ├── ...
    └── README.md

    ```

# 5. Usage
- **Running the Project**
    1. Navigate to the *src* directory
    ``` cd src ```
    
    2. Run the main script
    ``` python main.py ```

- **Features Guide**
    - **Register:** Create a new user account.
    - **Log In:** Access the scraping and data management features.
    - **Scrape Data:** Enter a search term to fetch and view results.
    - **Save Data:** Optionally save results to the database.
    - **Account Management:** Update or delete your account.

# 6. Folder Structure
```plaintext
Music-Gear-Digger-audioshopnepal/
├── database
│   ├── users.db               # Database for user management
│   ├── extracted_items.db     # Database for storing scraped data
├── src
│   ├── db_operations.py       # Handles database operations for scraped data
│   ├── action_manager.py      # Contains utility functions for handling core actions
│   ├── user_management.py     # Manages user-related functionalities
│   ├── display_manager.py     # Manages display messages and user prompts
│   ├── menu_manager.py        # Manages menu displays and user choices
│   ├── data_scraper.py        # Scraper module for extracting data from web pages
│   ├── main.py 
├── .gitignore                 # to specify files and directories to ignore in Gi
├── LICENSE                    # for the project's license details
├── README.md                  # Project documentation (this file)
├── requirements.txt           # Required Python packages
```

# 7. Future Improvements
- **🌐 Add support for multiple websites.**
- **📊 Enhance database schema to track historical searches.**
- **🔍 Include advanced search filters for scraping.**
- **🛡️ Implement API integration for secure and scalable data scraping.**


# 8. License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/sulavtamang/Music-Gear-Digger-audioshopnepal/blob/main/LICNESE) file for details.

