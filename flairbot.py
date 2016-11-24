import discord
import asyncio
import botinfo

client = discord.Client() # initialize client
client.start(botinfo.token) # log in

@client.event
async def on_message(message):
    server = client.get_server(botinfo.serverid) # I have to do this here because scope
    args = message.content.split(" ") # split message into command and args
    isDM = message.channel.is_private # check if the message was sent in a dm

    serverMember = server.get_member(message.author.id) # get member instance
    memberRoles = serverMember.roles # get roles of the member
    isOperator = False
    
    for role in memberRoles:
        isOperator = (role.name == botinfo.operatorRole) or isOperator # Determine if the user has op

    if args[0] == "!getrole":
        
        if not serverMember: # better safe than sorry
            await client.send_message(message.channel, "You are not in the server!")

        elif not isDM: # this should be a DM only command
            await client.send_message(message.channel, "This command is DM only!") # may remove this

        elif len(args) < 2:
            await client.send_message(message.channel, "Please include a role name!")

        elif not args[1] in botinfo.roleList:
            await client.send_message(message.channel, args[1] + " is not a valid role!")

        else:
            oldRoles = []
            for role in memberRoles:
                if role.name in botinfo.roleList:
                    oldRoles.append(role) # This loop determines the roles that the user already has
            
            await client.remove_roles(serverMember, *oldRoles)

            for role in server.roles:
                if role.name == args[1]:
                    newRole = role

            await client.add_roles(serverMember, newRole)
            
            await client.send_message(message.channel, "The role has been sucessfully granted!")

client.run(botinfo.token)
