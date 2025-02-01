from typing import Final
import os
import signal
from dotenv import load_dotenv
# import discord
from discord import Intents, Interaction, InteractionType
from discord.ext import commands
from responses import help_response,stuff_response
import signal
import asyncio
import sys

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

# STEP 2: HANDLING THE STARTUP FOR OUR BOT
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')
    # Sync the slash commands once the bot is ready
    try:
        await bot.tree.sync()
        print("Slash commands have been synced successfully!")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

    channel = bot.get_channel(1308510294506606623)
    if channel is not None:
        try:
            await channel.send("Hello World!")
            # liste des serveurs dans lesquels le bot est présent
            for guild in bot.guilds:
                print(f"Server: {guild.name} | Members count: {guild.member_count}")
                # print(guild.icon)
                # print(guild.owner)
                # print(guild.banner)
                # print(guild.members)
                # print(guild.preferred_locale)
                # for member in guild.members:
                #     print(member) # prints all members names one by one
                print('_________')
            print("Activation message sent successfully.")
            
        except Exception as e:
            print(f"Failed to send activation message: {e}")

# Commands logging
@bot.event
async def on_interaction(interaction):
        # Vérifie si l'interaction est une commande
    if interaction.type == InteractionType.application_command:
        channel = bot.get_channel(1335368709157421056)
        server = interaction.guild.name
        user = interaction.user
        command = interaction.command.name
        cmd_channel = interaction.channel
        
        # Récupération des arguments
        options = []
        if interaction.data.get('options'):
            for option in interaction.data['options']:
                option_name = option['name']
                option_value = option['value']
                options.append(f"{option_name}: {option_value}")
        
        # Création du message avec les arguments si présents
        if options:
            args_str = ' | '.join(options)
            log_message = f'{user} used /{command} with args: {args_str} in server {server} channel {cmd_channel}'
        else:
            log_message = f'{user} used /{command} in server {server} channel {cmd_channel}'
        
        # print(log_message)
        await channel.send(log_message)

############################################################################################
# @bot.event
# async def on_disconnect():
#     print("My battery is low and it's getting dark.")

# ## STEP 2.1 : HANDLING THE SHUTDOWN
# async def shutdown_handler():
#     """Sends a message to the target channel before shutting down."""
#     channel = bot.get_channel(1308510294506606623)
#     if channel is not None:
#         try:
#             await channel.send("My battery is low and it's getting dark.")
#             print("Shutdown message sent successfully.")
#         except Exception as e:
#             print(f"Failed to send shutdown message: {e}")

# def handle_exit(signum, frame):
#     """Capture termination signals and shut down gracefully."""
#     print("Shutting down bot...")
#     loop = bot.loop
#     if loop.is_running():
#         loop.create_task(shutdown_handler())
#     loop.stop()

# # Register signals (e.g., SIGINT for Ctrl+C)
# signal.signal(signal.SIGINT, handle_exit)
# signal.signal(signal.SIGTERM, handle_exit)
############################################################################################
# Flag global pour suivre si le message a été envoyé
shutdown_message_sent = False

class GracefulExit(SystemExit):
    pass

async def shutdown_handler():
    """Sends a message to the target channel before shutting down."""
    global shutdown_message_sent
    print("Initiating shutdown sequence...")
    
    if not shutdown_message_sent:
        channel = bot.get_channel(1308510294506606623)
        if channel is not None:
            try:
                await channel.send("My battery is low and it's getting dark.")
                shutdown_message_sent = True
                print("Shutdown message sent successfully.")
            except Exception as e:
                print(f"Failed to send shutdown message: {e}")
    
    try:
        await bot.close()
        print("Bot connection closed successfully.")
    except Exception as e:
        print(f"Error during bot shutdown: {e}")
    
    raise GracefulExit()

def signal_handler(signum, frame):
    """Handle termination signals."""
    print(f"Received signal {signum}")
    if asyncio.get_event_loop().is_running():
        asyncio.create_task(shutdown_handler())
    else:
        sys.exit(0)

# Register signal handlers
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

@bot.event
async def on_disconnect():
    global shutdown_message_sent
    print("Bot disconnected from Discord.")
    
    if not shutdown_message_sent:
        channel = bot.get_channel(1308510294506606623)
        if channel is not None and bot.is_ready():
            try:
                await channel.send("My battery is low and it's getting dark.")
                shutdown_message_sent = True
                print("Disconnection message sent successfully.")
            except Exception as e:
                print(f"Failed to send disconnection message: {e}")
############################################################################################
# STEP 3: SLASH COMMAND IMPLEMENTATION

# Stuff command
@bot.tree.command(name="stuff", description="Répond avec mes recommandations de stuff.")
async def stuff(interaction: Interaction, element: str, classe: str="vide"):
    resp=stuff_response(element.strip().lower(),classe.strip().lower())
    await interaction.response.send_message(resp)

# wbhelp command
@bot.tree.command(name="wbhelp", description="Besoin d'aide sur l'utilisation du bot?")
async def wbhelp(interaction: Interaction, commande: str ='vide'):
    resp=help_response(commande.strip().lower())
    await interaction.response.send_message(resp)

# twitch command
@bot.tree.command(name="twitch", description="Pour avoir des infos sur les prochains streams de Warp.")
async def twitch(interaction: Interaction):
    resp= f"""
Je stream la majorité des tournois pvp sur dofus touch, sauf quand je participe bien sur !
Au programme :
- 20-24 janvier : Tournois clandestin Oshimo
- 24-26 janvier : Tournois clandestin Herdegrize (je participe)
Après normalement c'est la fusion !
"""
    await interaction.response.send_message(resp)


# STEP 4: MAIN ENTRY POINT
def main() -> None:
    bot.run(TOKEN)


if __name__ == '__main__':
    main()
