import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('pokemon_data.db')
cursor = connection.cursor()

# Delete all rows in the table
cursor.execute("DELETE FROM pokemon")

# Commit changes and close the connection
connection.commit()
connection.close()

print("Database cleared successfully!")