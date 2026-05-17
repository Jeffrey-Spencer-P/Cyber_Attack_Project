# Cyber_Attack_Project

This project was used to simulate and attacker who is trying to gain access to control
to a system by use of sudo codes and how they might cover up this attack with the use of log how cyber security experts can monitor and mitigate
such attacks

This project requires the use of SQLite3 and python3 and was created and ran in a Linux virtual enviorment.
The virutal enviorment I ran this code in had 6 GB of RAM, 4 Processors and 25 GB of disk storage, while this
was enough to show the working of the code, in practical use more storage and processors would be necessary.
I ran this code on a Host-Only adapter network, but if you are on a private network Bridge or NAT should work fine.

# Database.py

Database.py represents a database that would collect information about possible attacks and what the 
monitoring system and mitigaton system would be doing.

EDITS:

On line 13 you can change the name of the databse if you would like but you'll need to change
the name in future parts of the code.

# Monitor.py

Monitor.py represents and IDS (Intrusion Detection System), this file monitors when users are trying to use sudo commands
that they do not have access to and when log files are edited. The code checks if log files have been truncated or fully deleted
and reports them to the database. 

EDITS:

Line 18 was the path that I used for my log files you can change this if needed.

You can edit line 19 and 20 to set your own email address and password so you are 
able to recive emails alerts for attacks instead of having to watch the terminal the whole time.

On line 39 you will need to change the "domain" to whatever email domain you are using.

On line 50 and 59 you'll need to change the name of the databse if you happened to change it earlier,
on line 59 you may need to change the path to the database.

On line 94 the code "time.sleep(2)" represents how often the code checks for an attack, this line
specifically means that it checks every 2 seconds. While this was what I used for my project realistically
you would want something constantly checking.

# Mitigate.py

Mitigate.py represents an IPS (Intrustion Prevention System), this file checks the database for entries
of log evasion or privlege escalation and then kills that users connection based on thier PID. 

EDITS:

On line 12 if you changed the name of the database earlier you'll need to change it here. 

On line 24 there is an commented out code that would normally lock the user accound after detecting
an attack. For testing purposes it is commented out but for an actual use it would be in the code.

On line 45 the code "time.sleep(5)" represents how oftern the database is checked for a new report,
due to having a small amount of resources I only checked the database every 5 seconds however if
your device can handle it you can change this.





