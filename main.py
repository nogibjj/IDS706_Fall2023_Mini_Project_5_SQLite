import sqlite3


def add(a, b):
    return a + b


if __name__ == "__main__":
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    # Create a table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"""
    )

    # Insert data
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))

    # Commit the changes
    conn.commit()

    # Query data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("-------print all records-------")
    for row in rows:
        print(row)
    
    cursor.execute("SELECT * FROM users WHERE users.name=='Alice'")
    rows = cursor.fetchall()
    print("-------print records with name=='Alice'-------")
    for row in rows:
        print(row)
