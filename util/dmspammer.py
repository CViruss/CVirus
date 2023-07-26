import discord
import asyncio
from colorama import Fore, Style

async def send_message(client, target_user_id, message_content):
    while True:
        try:
            user = await client.fetch_user(target_user_id)
            await user.send(message_content)
            print(f"{Fore.LIGHTBLUE_EX}Message sent to {user.name}#{user.discriminator}{Style.RESET_ALL}")
        except discord.errors.Forbidden:
            print(f"{Fore.LIGHTPURPLE_EX}Unable to send a message to {user.name}#{user.discriminator}. The user may have blocked the bot or disabled direct messages.{Style.RESET_ALL}")
        except discord.NotFound:
            print(f"{Fore.LIGHTPURPLE_EX}User with ID {target_user_id} not found.{Style.RESET_ALL}")
        
        # Wait for 1000 seconds before sending the next message
        await asyncio.sleep(0.1)

async def main():
    while True:
        bot_token = input(f"{Fore.LIGHTBLUE_EX}Enter the bot's token: {Style.RESET_ALL}")

        client = discord.Client()

        @client.event
        async def on_ready():
            print(f"{Fore.LIGHTGREEN_EX}We have logged in as {client.user}{Style.RESET_ALL}")

            while True:
                choice = input(f"{Fore.LIGHTBLUE_EX}What do you want next? Enter the number of your choice:\n1. Send messages to user\n2. log out\n{Style.RESET_ALL}")

                if choice == "2":
                    await client.logout()
                    print(f"{Fore.LIGHTGREEN_EX}Logged out. Exiting the program.{Style.RESET_ALL}")
                    return

                elif choice == "1":
                    target_user_id = int(input(f"{Fore.LIGHTBLUE_EX}Enter the target user's ID: {Style.RESET_ALL}"))
                    message_content = input(f"{Fore.LIGHTBLUE_EX}Enter the message content: {Style.RESET_ALL}")

                    # Start sending messages to the target user
                    await send_message(client, target_user_id, message_content)

                else:
                    print(f"{Fore.LIGHTPURPLE_EX}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}")

        try:
            await client.start(bot_token)
        except discord.LoginFailure:
            print(f"{Fore.RED}Invalid bot token. Please check and try again.{Style.RESET_ALL}")
            continue

if __name__ == "__main__":
    asyncio.run(main())
