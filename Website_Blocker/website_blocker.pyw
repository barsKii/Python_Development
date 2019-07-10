import time
from datetime import datetime as dt

#temp_hosts_path="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com","www.reddit.com", "reddit.com", "youtube.com", "www.youtube.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8, 30) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "\t" + website + "\n")


    else:
        print("You are in fun hours...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                else:
                    pass
            file.truncate()

    time.sleep(150)