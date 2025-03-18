import sqlite3
from datetime import datetime

def init_db():
    """
    Initialize the SQLite database and create the chats table if it doesn't exist.
    """
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chats
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  user_input TEXT,
                  emotion TEXT,
                  bot_response TEXT)''')
    conn.commit()
    conn.close()

def store_chat(user_input, emotion, bot_response):
    """
    Store a chat entry in the database.
    """
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO chats (timestamp, user_input, emotion, bot_response) VALUES (?, ?, ?, ?)",
              (timestamp, user_input, emotion, bot_response))
    conn.commit()
    conn.close()

def get_chat_history():
    """
    Retrieve all chat history from the database.
    """
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("SELECT timestamp, user_input, emotion, bot_response FROM chats ORDER BY timestamp DESC")
    history = c.fetchall()
    conn.close()
    return history

if __name__ == "__main__":
    # Test the database functions
    init_db()
    store_chat("I’m excited!", "joy", "Great to hear!")
    history = get_chat_history()
    for entry in history:
        print(entry)