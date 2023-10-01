# IDS706_Fall2023_Mini_Project_5_SQLite

 IDS706 week 5 mini project: create a Python script that interacts with a SQL database.

It contains:

- ``.devcontainer`` includes a `Dockerfile` that specifies the configurations of container, and a `devcontainer.json` which is a configuration file used in the context of Visual Studio Code

- ``workflows`` includes `GitHub Actions`, enables automated build, test and deployment for the project

- ``Makefile`` specifies build automation on Linux

- ``requirements.txt`` lists the dependencies, libraries, and specific versions of Python packages required for the project

It also includes ``main.py`` and ``test_main.py`` as sample files to show the functionality of the CI pipeline.

## Interact with SQLite database
To interact with SQLite database, first we need to establish a connection:
```
conn = sqlite3.connect("my_database.db")
```
Then create a cursor object to execute any operations we want. For example, we insert two records to the newly created table:
```
cursor = conn.cursor()
cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"""
    )
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
```
After the operations are commited, the cursor can be used to execute SQL queries:
```
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
cursor.execute("SELECT * FROM users WHERE users.name=='Alice'")
rows = cursor.fetchall()
```
The results are printed out:<br>

![query_result](demo_img/query_result.png)