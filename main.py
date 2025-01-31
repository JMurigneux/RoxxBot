from typing import Final
import os
import signal
from dotenv import load_dotenv
from discord import Intents, Interaction
from discord.ext import commands
from responses import help_response,stuff_response

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

@bot.event
async def on_disconnect():
    print("My battery is low and it's getting dark.")

## STEP 2.1 : HANDLING THE SHUTDOWN
async def shutdown_handler():
    """Sends a message to the target channel before shutting down."""
    channel = bot.get_channel(1308510294506606623)
    if channel is not None:
        try:
            await channel.send("My battery is low and it's getting dark.")
            print("Shutdown message sent successfully.")
        except Exception as e:
            print(f"Failed to send shutdown message: {e}")

def handle_exit(signum, frame):
    """Capture termination signals and shut down gracefully."""
    print("Shutting down bot...")
    loop = bot.loop
    if loop.is_running():
        loop.create_task(shutdown_handler())
    loop.stop()

# Register signals (e.g., SIGINT for Ctrl+C)
signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

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
