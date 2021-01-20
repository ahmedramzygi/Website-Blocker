import time
from datetime import datetime as dt

hosts_file= r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp=r"C:\Users\aeram\Desktop\Projects\PythonBlocker\hosts"
redirect="127.0.0.1"
blocked_sites=["www.facebook.com","www.instagram.com"]


while(True):
    if dt(dt.now().year,dt.now().month,dt.now().day,17) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19): # We want to block these sites in this range
        print('Working Hours')
        with open (hosts_file,'r+') as file:
            content=file.read()
            for website in blocked_sites:
                if website in content:
                    pass
                else:
                    file.write(redirect+"      "+website+"\n")

    else:
        with open(hosts_file,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_sites):
                    file.write(line)
            file.truncate()
        print('fun')
    time.sleep(5)

    



