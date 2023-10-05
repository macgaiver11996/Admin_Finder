import sys, os, time, requests, pyfiglet

black="\033[1;90m"
white="\033[1;97m"
red="\033[1;91m"
green="\033[1;92m"
yellow="\033[1;93m"
blue="\033[1;94m"
purple="\033[1;95m"
cyan="\033[1;96m"  
rst="\033[0m"

os.system("clear")

def animetion (text):
  for i in text:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.005)

banner = f'''
{red} _____   _       _        _____                         
{green}|  _  |_| |_____|_|___   |   __|___ ___ ___ ___ ___ ___ 
{blue}|     | . |     | |   |  |__   |  _| .'|   |   | -_|  _|
{yellow}|__|__|___|_|_|_|_|_|_|  |_____|___|__,|_|_|_|_|___|_|\n\n  
'''



details = f"""{green}                  Author   : Macgaiver
                  Github   : https://github.com/macgaiver11996
                  Telegram : t.me/macgaiver_official{rst}\n"""
           

symbol = f"{green}\n****************************************************************{rst}"

animetion (banner)
animetion (details)
animetion (symbol)


site = input(f"{yellow}\n➤➤➤ Enter your terget site : {rst}")


with open ('admin.txt','r') as mac:
  exploit = mac.read().splitlines()
  for line in exploit:
    url = f"{site}/{line}"
    try:
      response = requests.get(url)
      if response.status_code == 200:
        print (f"{green}Found >> {url}")
      else:
        print (f"{red}Not Found >> {url}{rst}")
    except:
      pass
