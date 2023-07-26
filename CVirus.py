import os
import discord
import asyncio
from colorama import Fore, Style
import sys
sys.path.append("/path/to/CVirus_module_directory")

# Importing TokenLogin from accountlogger.py
from util.accountlogger import TokenLogin

def getheaders(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    return headers

def generate_header():
    # Define the number of steps in the gradient
    num_steps = 15

    # Generate the gradient from light blue to dark blue to purple
    gradient = ""
    for i in range(num_steps):
        # Calculate the ratio of light blue to dark blue to purple (ranges from 0 to 1)
        ratio = i / (num_steps - 1)

        # Calculate the RGB values for the current step
        r = int(135 + (ratio * (68 - 135)))
        g = int(206 + (ratio * (85 - 206)))
        b = int(235 + (ratio * (139 - 235)))

        # Convert the RGB values to a color string in RGB format
        color_code = f'\033[38;2;{r};{g};{b}m'

        # Add the colored text to the header
        gradient += f'{color_code}█'

    return gradient

def nitrogen_action():
    os.system("python util/nitrogen.py")

def tokengen_action():
    os.system("python main.py")

def account_logger_action():
    os.system("python util/accountlogger.py")
    main()

def autoclicker_action():
    os.system("python util/autoclicker.py")

def massdm_action():
    os.system("python util/massdm.py")
def accountlogger():
    os.system("python util/accountlogger.py")

def massreport_action():
    os.system("python util/massreport.py")

def nuker_action():
    os.system("python util/nuker.py")

def boosting_action():
    os.system("python util/boosting.py")

def dmspammer_action():
    os.system("python util/dmspammer.py")

def messagespammer_action():
    os.system("python util/messagespammer.py")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console()

        header = generate_header()

        print(f"""{Fore.LIGHTBLUE_EX}
                                         ██████╗██╗   ██╗██╗██████╗ ██╗   ██╗███████╗
                                        ██╔════╝██║   ██║██║██╔══██╗██║   ██║██╔════╝
                                        ██║     ██║   ██║██║██████╔╝██║   ██║███████╗
                                        ██║     ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║
                                        ╚██████╗ ╚████╔╝ ██║██║  ██║╚██████╔╝███████║   2.5.1
                                         ╚═════╝  ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                            
                                            [1] - Nitrogen/checker  [8] - Auto Clicker  
                                            [2] - Nuker             [9] - TokenGen          
                                            [3] - boost tool        [10] - Exit   
                                            [4] - dm spammer        
                                            [5] - message spammer   
                                            [6] - mass dm           
                                            [7] - Account Logger 
                                                                                                                                                                                                                    https://github.com/CViruss                    
        """)

        user_input = input(">>>: ")

        if user_input == "1":
            nitrogen_action()
        elif user_input == "2":
            nuker_action()
        elif user_input == "3":
            boosting_action()
        elif user_input == "4":
            dmspammer_action()
        elif user_input == "5":
            messagespammer_action()
        elif user_input == "6":
            massdm_action()
        elif user_input == "7":
            accountlogger()
        elif user_input == "8":
            autoclicker_action()
        elif user_input == "9":
            tokengen_action()
        elif user_input == "9s":
            print("Exiting...")
            choice = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Are you sure you want to exit? (Y to confirm): {Fore.LIGHTRED_EX}')
            if choice.upper() == 'Y':
                clear_console()
                Style.RESET_ALL
                Fore.RESET
                os._exit(1)
            else:
                continue
        else:
            print("\nNot Valid Option")

        input("Press Enter to continue")

if __name__ == "__main__":
    main()