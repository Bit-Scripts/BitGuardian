import json
import discord
from discord.ext import commands
from auto_role import on_member_join
#from log import log_message  # Importez la fonction log_message depuis log.py

# Charger la configuration à partir du fichier config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)  # Utilisez des crochets ici

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}!')

@bot.event
async def on_message(message):
    print(f'Message de {message.author}: {message.content}')
    
    # Quitter la fonction si le message provient d'un salon privé (DMChannel) pour éviter une boucle infinie
    if isinstance(message.channel, discord.DMChannel):
        return

    # Vérifier si le message est envoyé par le bot
    if message.author.bot:
        return

    #await log_message(message)  # Utilisez la fonction log_message pour enregistrer les messages

    await bot.process_commands(message)  # Ajouté pour traiter les commandes du bot

bot.add_listener(on_member_join, 'on_member_join')

bot.run(config['token'])