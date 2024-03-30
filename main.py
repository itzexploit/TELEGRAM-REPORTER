from requests import post
from os import system , name
from colorama import init , Fore
from threading import Thread

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = f'''
           {red}╔╦╗┌─┐┬  ┌─┐┌─┐┬─┐┌─┐┌┬┐  ╦═╗┌─┐┌─┐┌─┐┬─┐┌┬┐┌─┐┬─┐
            ║ ├┤ │  ├┤ │ ┬├┬┘├─┤│││  ╠╦╝├┤ ├─┘│ │├┬┘ │ ├┤ ├┬┘
            ╩ └─┘┴─┘└─┘└─┘┴└─┴ ┴┴ ┴  ╩╚═└─┘┴  └─┘┴└─ ┴ └─┘┴└─
                        {red}Created {green}By {blue}John {red}Wick
'''

print(banner)

url = 'https://telegram.org/support'

message = input(f'{red}[{yellow}+{red}] {cyan}Enter Your Message {red}:{green} ')
email = input(f'{red}[{yellow}+{red}] {cyan}Enter Your Email Addres {red}:{green} ')
cell = input(f'{red}[{yellow}+{red}] {cyan}Enter Your Cell Phone {red}:{green} ')

def supp():
    data = {'message':f'{message}','email':f'{email}','phone':f'{cell}'}
    post(url, data=data)
    print(f'{red}[{yellow}+{red}] {green}Report Sent to Support Telegram')

Thread(target=supp).start()
