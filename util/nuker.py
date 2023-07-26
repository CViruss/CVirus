import discord
import asyncio
from colorama import Fore, Style

async def delete_channels(guild):
    async def delete_channel(channel):
        try:
            await channel.delete()
            print(f"{Fore.LIGHTMAGENTA_EX}Deleted channel: {channel.name}{Style.RESET_ALL}")
        except discord.errors.Forbidden:
            print(f"{Fore.RED}Unable to delete channel: {channel.name}. The bot may not have permission to delete channels.{Style.RESET_ALL}")

    tasks = [delete_channel(channel) for channel in guild.channels]
    await asyncio.gather(*tasks)

async def ban_all_members(guild):
    ban_reason = input(f"{Fore.LIGHTCYAN_EX}Enter the ban reason: {Style.RESET_ALL}")

    for member in guild.members:
        try:
            await member.ban(reason=ban_reason)
            print(f"{Fore.LIGHTRED_EX}Banned member: {member.name}#{member.discriminator} | Reason: {ban_reason}{Style.RESET_ALL}")
        except discord.errors.Forbidden:
            print(f"{Fore.RED}Unable to ban member: {member.name}#{member.discriminator}. The bot may not have permission to ban members.{Style.RESET_ALL}")

async def create_channels(guild):
    num_channels = int(input(f"{Fore.LIGHTCYAN_EX}Enter the number of channels to create: {Style.RESET_ALL}"))
    channel_name = input(f"{Fore.LIGHTCYAN_EX}Enter the name for the channels: {Style.RESET_ALL}")

    channel_type = input(f"{Fore.LIGHTCYAN_EX}Enter the channel type ({Fore.LIGHTYELLOW_EX}1: Voice, 2: Text{Fore.LIGHTCYAN_EX}): {Style.RESET_ALL}")

    if channel_type == "1":
        channel_type = discord.ChannelType.voice
    elif channel_type == "2":
        channel_type = discord.ChannelType.text
    else:
        print(f"{Fore.RED}Invalid choice. Defaulting to text channel creation.{Style.RESET_ALL}")
        channel_type = discord.ChannelType.text

    for i in range(num_channels):
        try:
            print(f"{Fore.BLUE}Creating channel: {channel_name}{i + 1}{Style.RESET_ALL}")
            if channel_type == discord.ChannelType.voice:
                await guild.create_voice_channel(f"{channel_name}{i + 1}")
            else:
                await guild.create_text_channel(f"{channel_name}{i + 1}")
        except discord.errors.Forbidden:
            print(f"{Fore.RED}Unable to create channel: {channel_name}{i + 1}. The bot may not have permission to create channels.{Style.RESET_ALL}")

    print(f"{Fore.LIGHTGREEN_EX}Channel creation completed.{Style.RESET_ALL}")

async def main():
    bot_token = input(f"{Fore.LIGHTCYAN_EX}Enter the bot's token: {Style.RESET_ALL}")
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"{Fore.GREEN}We have logged in as {client.user}{Style.RESET_ALL}")

        while True:
            guild_id = input(f"{Fore.LIGHTCYAN_EX}Enter the Discord Guild ID or 'exit' to quit: {Style.RESET_ALL}")

            if guild_id.lower() == "exit":
                await client.close()
                break

            try:
                guild_id = int(guild_id)
                guild = client.get_guild(guild_id)

                if guild:
                    print(f"{Fore.GREEN}Selected Guild: {guild.name}{Style.RESET_ALL}")
                    await delete_channels(guild)
                    await ban_all_members(guild)
                    await create_channels(guild)
                    print(f"{Fore.LIGHTCYAN_EX}All channels have been deleted, all members have been banned, and new channels have been created.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Invalid Guild ID or the bot is not on this server.")
                    print(f"Guild ID: {guild_id}")
                    print(f"All Guilds: {client.guilds}{Style.RESET_ALL}")

            except ValueError:
                print(f"{Fore.RED}Invalid Guild ID. Please make sure to enter a numerical ID.{Style.RESET_ALL}")

    await client.start(bot_token)

if __name__ == "__main__":
    asyncio.run(main())
