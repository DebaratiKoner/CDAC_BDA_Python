"""
### Assignment 4: Relational SQLite User Management System
#### Scenario
An internal employee directory stores user contact details in a SQLite database. The application must search for users, display existing details, or register new users.

#### Problem Description
Create a class `UserDatabaseManager` that connects to a SQLite database file:
1. **`__init__(self, db_path)`**: Connects to the database and creates a table `users` if it doesn't already exist:
   - Columns: `id INTEGER PRIMARY KEY AUTOINCREMENT`, `username TEXT UNIQUE NOT NULL`, `address TEXT`, `mobile TEXT`, `email TEXT`.
2. **`find_user(self, username)`**:
   - Queries the database for the given `username` using a parameterized SQL query.
   - If found, returns a dictionary: `{"id": row[0], "username": row[1], "address": row[2], "mobile": row[3], "email": row[4]}`.
   - If not found, returns `None`.
3. **`add_or_update_user(self, username, address, mobile, email)`**:
   - Checks if `username` exists.
   - If user exists, updates their `address`, `mobile`, and `email` values and returns `"UPDATED"`.
   - If user does not exist, inserts a new record and returns `"INSERTED"`.
4. **`list_all_users(self)`**: Returns a list of dictionaries for all registered users ordered alphabetically by `username`.

#### Example Walkthrough
```python
db = UserDatabaseManager("company.db")

# Insert new user
status1 = db.add_or_update_user("arham_k", "Pune, MH", "9876543210", "arham@cdac.in")
print(status1)  # Output: INSERTED

# Search user
user_info = db.find_user("arham_k")
print(user_info["email"])  # Output: arham@cdac.in

# Update existing user
status2 = db.add_or_update_user("arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
print(status2)  # Output: UPDATED
```
"""
import sqlite3

class UserDatabaseManager:
    def __init__(self,db_path):
        self.conn=sqlite3.connect(db_path)
        self.cursor=self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            address TEXT,
            mobile TEXT,
            email TEXT
        )
        """)

        self.conn.commit()

    def find_user(self,username):
        self.cursor.execute(
            "SELECT * FROM users WHERE username=?",(username,)
        )
        row=self.cursor.fetchone()

        if row:
            return {
                "id":row[0],
                "username":row[1],
                "address":row[2],
                "mobile":row[3],
                "email":row[4]
            }

        return None

    def add_or_update_user(self,username,address,mobile,email):
        user=self.find_user(username)

        if user:
            self.cursor.execute(
                "UPDATE users SET address=?,mobile=?,email=? WHERE username=?",
                (address,mobile,email,username)
            )
            self.conn.commit()
            return "UPDATED"

        self.cursor.execute(
            "INSERT INTO users(username,address,mobile,email) VALUES(?,?,?,?)",
            (username,address,mobile,email)
        )
        self.conn.commit()
        return "INSERTED"

    def list_all_users(self):
        self.cursor.execute(
            "SELECT * FROM users ORDER BY username"
        )

        rows=self.cursor.fetchall()
        users=[]

        for row in rows:
            users.append({
                "id":row[0],
                "username":row[1],
                "address":row[2],
                "mobile":row[3],
                "email":row[4]
            })

        return users


db=UserDatabaseManager("company.db")

status1=db.add_or_update_user(
    "arham_k",
    "Pune, MH",
    "9876543210",
    "arham@cdac.in"
)

print(status1)

user_info=db.find_user("arham_k")
print(user_info["email"])

status2=db.add_or_update_user(
    "arham_k",
    "Bengaluru, KA",
    "9876543210",
    "arham@cdac.in"
)

print(status2)

print(db.list_all_users())