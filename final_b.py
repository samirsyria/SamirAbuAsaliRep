import sqlite3
import os

# Allow user to specify the database directory
db_directory = input("Enter the directory where the database should be created: ")

# Ensure the directory exists
os.makedirs(db_directory, exist_ok=True)

# Specify the database path (SQLite)
db_path = os.path.join(db_directory, "example_database.sqlite")

# Connect to or create the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a new table named Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Age INTEGER
)
""")

# Insert sample data
cursor.execute("INSERT INTO Users (Name, Email, Age) VALUES (?, ?, ?)", ('John Doe', 'john@example.com', 30))
cursor.execute("INSERT INTO Users (Name, Email, Age) VALUES (?, ?, ?)", ('Jane Doe', 'jane@example.com', 25))
conn.commit()

# Fetch data to display
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

# Display data
for row in rows:
    print(row)

# Close the connection
cursor.close()
conn.close()

print(f"SQLite database created at {db_path} and populated with sample data successfully!")
