import discord

async def on_member_join(member):
    try:
        role = discord.utils.get(member.guild.roles, name='Utilisateur')
        if role is None:
            print("Le rôle 'Utilisateur' n'a pas été trouvé. Veuillez créer ce rôle sur votre serveur.")
            return
        await member.add_roles(role)
        print(f"Le rôle 'Utilisateur' a été attribué à {member}.")
    except Exception as error:
        print(f"Erreur lors de l'attribution du rôle : {error}")