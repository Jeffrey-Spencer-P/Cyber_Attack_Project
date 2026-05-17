# Cyber_Attack_Project

This project was used to simulate and attacker who is trying to gain access to control
to a system by use of sudo codes and how cyber security experts can monitor and mitigate
such attacks

This project requires the use of SQLite3 and python3 and was created and ran in a Linux virtual enviorment.
The virutal enviorment I ran this code in had 6 GB of RAM, 4 Processors and 25 GB of disk storage, while this
was enough to show the working of the code, in practical use more storage and processors would be necessary.
I ran this code on a Host-Only adapter network, but if you are on a private network Bridge or NAT should work fine.

# Database.py



# Monitor.py

Monitor.py represents and IDS (Intrusion Detection System), this file monitors when users are trying to use sudo commands
that they do not have access to and when log files are edited. The code checks if log files have been truncated or fully deleted
and reports them to the terminal.

Line 18 was the path that I used for my log files you can change this if needed.

You can edit line 19 and 20 to set your own email address and password so you are 
able to recive emails alerts for attacks instead of having to watch the terminal the whole time.

On line 59 you'll need to change the path to the database and if you changed the name of the databse you'll need
to change that too.




