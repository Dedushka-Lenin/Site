import sqlite3
import os

DB_PATH = "Auction_Site/db.sqlite3"

db_exists = os.path.exists(DB_PATH)

connection = sqlite3.connect(DB_PATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS offers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL,
        price_per_meter INTEGER NOT NULL,
        square INTEGER NOT NULL,
        description TEXT NOT NULL,
        url TEXT NOT NULL    
    );
"""
)

connection.close()
