# Cyber_Attack_Project

This project was used to simulate and attacker who is trying to gain access to control
to a system by use of sudo codes and how cyber security experts can monitor and mitigate
such attacks

This project requires the use of SQLite3 and python3 and was created and ran in a Linux virtual enviorment.
The virutal enviorment I ran this code in had 6 GB of RAM, 4 Processors and 25 GB of disk storage, while this
was enough to show the working of the code, in practical use more storage and processors would be necessary.
I ran this code on a Host-Only adapter network, but if you are on a private network Bridge or NAT should work fine.

# Monitor.py

Monitor.py represents and IDS (Intrusion Detection System), this file monitors when users are trying to use sudo commands
that they do not have access to and...

In the Monitor.py file you can edit line 19 and 20 to set your own email address and password so 
