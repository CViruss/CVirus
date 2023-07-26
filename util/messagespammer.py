import discord
import asyncio
from colorama import Fore, Style

async def send_message(client, channel_id, message_content, num_messages):
    try:
        channel = client.get_channel(channel_id)
        if not channel:
            print(f"{Fore.LIGHTPURPLE_EX}Channel with ID {channel_id} not found.{Style.RESET_ALL}")
            return

        for _ in range(num_messages):
            await channel.send(message_content)
        print(f"{Fore.LIGHTBLUE_EX}{num_messages} messages sent to channel {channel.name}{Style.RESET_ALL}")
    except discord.errors.Forbidden:
        print(f"{Fore.LIGHTPURPLE_EX}Unable to send messages to channel {channel_id}. The bot may not have permission to send messages in that channel.{Style.RESET_ALL}")
    except discord.NotFound:
        print(f"{Fore.LIGHTPURPLE_EX}Channel with ID {channel_id} not found.{Style.RESET_ALL}")

async def main():
    bot_token = input(f"{Fore.LIGHTBLUE_EX}Enter your bot token: {Style.RESET_ALL}")

    if not bot_token:
        print(f"{Fore.LIGHTRED_EX}Error: No bot token provided. Please enter your bot token.{Style.RESET_ALL}")
        return

    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"{Fore.LIGHTGREEN_EX}We have logged in as {client.user}{Style.RESET_ALL}")

        while True:
            choice = input(f"{Fore.LIGHTBLUE_EX}Do you want to send messages? (y/n): {Style.RESET_ALL}").lower()

            if choice == "n":
                await client.logout()
                print(f"{Fore.LIGHTGREEN_EX}Logged out. Exiting the program.{Style.RESET_ALL}")
                return

            elif choice == "y":
                try:
                    channel_id = int(input(f"{Fore.LIGHTBLUE_EX}Enter the target channel ID: {Style.RESET_ALL}"))
                except ValueError:
                    print(f"{Fore.LIGHTRED_EX}Invalid channel ID. Please enter a numerical ID.{Style.RESET_ALL}")
                    continue

                message_content = input(f"{Fore.LIGHTBLUE_EX}Enter the message content: {Style.RESET_ALL}")

                try:
                    num_messages = int(input(f"{Fore.LIGHTBLUE_EX}Enter the number of messages to send: {Style.RESET_ALL}"))
                except ValueError:
                    print(f"{Fore.LIGHTRED_EX}Invalid number of messages. Please enter a numerical value.{Style.RESET_ALL}")
                    continue

                # Start sending the requested messages
                await send_message(client, channel_id, message_content, num_messages)

            else:
                print(f"{Fore.LIGHTPURPLE_EX}Invalid choice. Please enter 'y' or 'n'.{Style.RESET_ALL}")

    try:
        await client.start(bot_token)
    except discord.LoginFailure:
        print(f"{Fore.LIGHTRED_EX}Invalid bot token. Please check the bot token and try again.{Style.RESET_ALL}")

def run_main():
    if hasattr(asyncio, "run"):  # Check if asyncio.run is available (Python 3.7+)
        asyncio.run(main())
    else:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

if __name__ == "__main__":
    run_main()
