import sqlite3
from sqlite3 import Connection

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self, db_name: str) -> Connection:
        """Establish a database connection if it doesn't already exist."""
        if self.connection is None:
            self.connection = sqlite3.connect(db_name)
            print(f"Database connection established to {db_name}.")
        return self.connection
    
    def _initialize_tables(self):
        with self.connection as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
                         id INTEGER PRIMARY KEY,
                         type TEXT NOT NULL,
                         title TEXT,
                         description TEXT
                         )
                         """)
            
    def insert_task(self, task_type: str, title: str, description: str):
        with self.connection as conn:
            conn.execute("INSERT INTO tasks (type, title, description) VALUES (?, ?, ?)",
                         (task_type, title, description)
            )

    def get_tasks(self):
        with self.connection as conn:
            cursor = conn.execute("SELECT * FROM tasks")
            return cursor.fetchall()

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Database connection closed.")
