# Cyber Attack Project By: Jeffrey Spencer
# database.py

# Here I'm creating a Database that will keep track of logs incase an attacker 
# edits or changes the logs I will still have a "paper-trail".

# sqlite3 is an in-house python supported database so I don't have to create a database

import sqlite3

# I've given the name "attack_project" to my database 

DB_NAME = "attack_project.db"

# Here I'm initalizing the database if it doesn't already exist

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # This table will be logging any proccess that are changed and logging them.
    # If a user does priviledge escalation it will be logged here and so will the
    # information of the user (pid) and what tool/command they used.

    cursor.execute('''CREATE TABLE IF NOT EXISTS process_events (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        user_name TEXT,
                        pid INTEGER,
                        proc_name TEXT,
                        details TEXT)''')
    
    # This table will be logging any changes to the log files and recording
    # what paths the attacker used as well as what was changed in the file
    # (deletion/truncation/edited...)
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS file_events(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        event_type TEXT,
                        file_path TEXT)''')
    
    #Here I'm saving the changes and then closing the connection to the database.

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Database {DB_NAME} ready.")