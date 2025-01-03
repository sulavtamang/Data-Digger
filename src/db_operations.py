
import sqlite3

class DatabaseManager:
    # db_path = 

    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        
    
    def create_table(self):
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS extracted_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL UNIQUE,
            Category TEXT NOT NULL,
            Brand TEXT NOT NULL,
            Rating TEXT NOT NULL,
            Availability TEXT NOT NULL,
            Original_price TEXT NOT NULL,
            Discount TEXT NOT NULL,
            Current_price TEXT NOT NULL,
            Detail_url TEXT NOT NULL UNIQUE,
            Image_url TEXT NOT NULL UNIQUE
        );
        ''')

        self.conn.commit()
        self.conn.close()

    def already_exists(self, name):
        cursor = self.conn.cursor()

        cursor.execute('''
            SELECT 1 FROM extracted_items WHERE Name = (?)
        ''', (name,))

        if cursor.fetchone():
            return True
        return False
    
    def insert_items(self, extracted_items):
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()

        for instrument in extracted_items:
            if self.already_exists(instrument['Name']):    
                print(f"The item {instrument['Name']} already exists in the database!")
                continue
            
            cursor.execute('''
            INSERT INTO extracted_items (Name, Category, Brand, Rating, Availability, Original_price, Discount, Current_price, Detail_url, Image_url)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (instrument['Name'], instrument['Category'], instrument['Brand'], instrument['Rating'], instrument['Availability'],
            instrument['Original Price'], instrument['Discount'], instrument['Current Price'], instrument['Detail URL'], instrument["Image URL"])
            )
            print(f'"{instrument['Name']}" inserted into the database.')
    
        self.conn.commit()
        self.conn.close()

    

