# Cyber Attack Project By: Jeffrey Spencer
# mitigation.py

# This file is used to mitigate the attack and works like an IPS

import sqlite3
import os
import time

def run_mitigation():
    """Check the database for new incidents and then takes action"""
    conn = sqlite3.connect("attack_project.db")
    cursor = conn.cursor()

    # First action, kill priveledge escalation

    cursor.execute("SELECT pid, user_name FROM process_events ORDER BY id DESC LIMIT 1")
    proc_row = cursor.fetchone()
    if proc_row:
        pid, user = proc_row
        print(f"Killing process {pid} for user {user}")
        try:
            os.system(f"kill -9 {pid}")
            #os.system(f"passwd -l {user}") --> This would normally lock the user account
        except:
            pass

    # Second action, restore losses

    cursor.execute("SELECT event_type FROM file_events ORDER by id DESC LIMIT 1")
    file_row = cursor.fetchone()
    if file_row:
        print("Restoring /var/log/auth.log")

        #This will create a new log file and set standard root permission

        os.system("touch /var/log/auth.log && chmod 640 /var/log/auth.log")
    conn.close()

if __name__ == "__main__":
    print("Mitigation Active: Checking Database")
    try:
        while True:
            run_mitigation()
            time.sleep(5) # This will check the database every 5 seconds
    except KeyboardInterrupt:
        print("Stopping Mitigation")