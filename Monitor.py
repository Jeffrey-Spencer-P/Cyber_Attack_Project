# Cyber Attack Project By: Jeffrey Spencer
# Monitor.py

# This file is used to monitor any changes and then report those changes to me
# and my email address. 
# This file acts like an IDS

import time
import os
import psutil
import sqlite3
import smtplib
from email.mime.text import MIMEText


# These are the set configurations of what it will watch and how it will contact me

TARGET_LOG = "/var/log/auth.log"                  # Path to Log
SENDER_EMAIL = "example123@domain.com"            # Email address
APP_PASSWORD = "123 456 789 ABC"                  # Password to push the email

# Here will be the layout of the email

def send_alert(subject, body):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = SENDER_EMAIL

        # The 'with' statement creates the 'server' variable.

        with smtplib.SMTP('smtp.domain.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
            
    except Exception as c:
        print(f"Email not sent: {c}")

def check_file_integrity():
    """Checks if the log file has been deleted or truncated"""
    if not os.path.exists(TARGET_LOG):
        report_incident("LOG_DELETION, TARGET_LOG)")
    elif os.path.getsize(TARGET_LOG) == 0:
        report_incident("LOG_TRUNCATION",TARGET_LOG)

def report_incident(e_type, path):
    """Log file alerts to Database and sends email """
    conn = sqlite3.connect("attack_project.db")
    conn.execute("INSERT INTO file_events (event_type, file_path) VALUE (?,?)", (e_type,path))
    conn.commit()
    conn.close()
    print(f"ALERT: {e_type} on {path}")
    send_alert(f"ALERT: {e_type}", f"Log teampering detected: {path}")

def check_privileges():
    """Way to check for escalation by reading /proc filesystem"""
    conn = sqlite3.connect("/home/path/path/attack_project.db")
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    for pid in pids:
        try:
            with open(f'/proc/{pid}/status', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('Uid'):
                        uids = line.split()[1:]
                        real_uid = int(uids[0])
                        eff_uid = int(uids[1])

                        if real_uid !=0 and eff_uid ==0:
                            with open(f'/proc/{pid}/comm', 'r') as f_name:
                                name = f_name.read().strip()

                                conn.execute("INSERT INTO process_events (user_name, pid, proc_name, details) VALUES (?,?,?,?)",
                                    ("Unknown", pid, name, "Root escalation detected via /proc"))
                            conn.commit()
                            print(f"ALERT: Escalation Detected PID: {pid} Name: {name}")
                            send_alert("Alert: Privelege Escalation", f"PID {pid} ({name}) gained root")
        except (IOError, OSError):
            continue
    conn.close

if __name__ == "__main__":
    if os.getuid() != 0:
        exit("Must run as sudo.")

    print("Monitor Active, monitoring /var/log and porcess UIDs")
    try:
        while True:
            check_privileges()
            check_file_integrity()
            time.sleep(2)
    except KeyboardInterrupt:
        print("Monitor Stopping")
