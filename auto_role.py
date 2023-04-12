import discord

async def on_member_join(member):
    role_id = 1095447703749677269 
    try:
        role = discord.utils.get(member.guild.roles, id=role_id)
        if role is None:
            print(f"Le rôle avec l'ID {role_id} n'a pas été trouvé. Veuillez vérifier que l'ID est correct.")
            return
        await member.add_roles(role)
        print(f"Le rôle {role.name} a été attribué à {member}.")
    except Exception as error:
        print(f"Erreur lors de l'attribution du rôle : {error}")