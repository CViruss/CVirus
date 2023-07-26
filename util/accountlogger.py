import os
import requests
import threading
from colorama import Fore
from time import sleep

def getheaders(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    return headers

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def TokenLogin(token):
    print(f"\nLogged in with token: {token}")

def account_logger_action():
    print(f"{Fore.LIGHTRED_EX}(the token you input is the account that will be checked){Fore.RESET}")
    token = str(input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))

    r = requests.get('https://discord.com/api/v6/users/@me', headers=getheaders(token))
    if r.status_code == 200:
        clear_console()
        threads = 100
        if threading.active_count() < threads:
            threading.Thread(target=TokenLogin, args=(token,)).start()
            return
    else:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1)

if __name__ == "__main__":
    account_logger_action()
