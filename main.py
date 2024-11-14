from typing import Final
import os
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
- 19-24 Novembre : Tournois Oshimo
- 29 Novembre - 1 Décembre : Tournois Tiliwan 1
- 6/7/8 Décembre : Tournois Herdegrize
- 13/14/15 Décembre : Tournois Tiliwan 2
"""
    await interaction.response.send_message(resp)


# STEP 4: MAIN ENTRY POINT
def main() -> None:
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
