
import asyncio
import sys

import discord
from discord.ext import commands, tasks

import time

owners = [401849772157435905, 876488885419520020] # Owner account IDs

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '()', help_command=None, intents=intents) #Makes the bot prefix.



@client.event
async def on_ready():
    print("========")
    print(f"current UNIX time is {time.time()}.")
    print("========")
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('========')



@client.event
async def on_message_delete(message):
    deleted = discord.Embed(description="Message deleted in {msgchannel}".format(msgchannel=message.channel.mention), color=0xFF0000)
    channel=client.get_channel(1092435780095451236)
    if(message.channel.id != 1092435780095451236 and message.channel.id != 1091118930749309008):
        
        if message.attachments:
            if(len(message.attachments) == 1):
                if message.attachments[0].url.endswith(('.jpg', '.png', '.jpeg', '.gif')):
                    deleted.set_image(url=message.attachments[0].url)
                else:
                    deleted.add_field(name="Attachment", value=message.attachments[0].url) # No attachment or unsupported file     
        deleted.add_field(name="Author", value=message.author)
        deleted.add_field(name="Message", value=message.content)
        deleted.timestamp = message.created_at
        await channel.send(embed=deleted)
    
    
@client.event
async def on_message_edit(message_before, message_after):
    edited = discord.Embed(description="Message edited in {msgchannel}".format(msgchannel=message_before.channel.mention), color=0xFFFF00)
    channel=client.get_channel(1092435780095451236)
    if(message_before.channel.id != 1092435780095451236 and message_before.channel.id != 1091118930749309008):
        
        if message_before.attachments:
            if(len(message_before.attachments) == 1):
                if message_before.attachments[0].url.endswith(('.jpg', '.png', '.jpeg', '.gif')):
                    edited.set_image(url=message_before.attachments[0].url)
                else:
                    edited.add_field(name="Attachment", value=message_before.attachments[0].url) # No attachment or unsupported file     
        edited.add_field(name="Author", value=message_before.author)
        edited.add_field(name="Message Before", value=message_before.content)
        edited.add_field(name="Message After", value=message_after.content)
        edited.timestamp = message_before.created_at
        await channel.send(embed=edited)
    
@client.command()
async def resetbot(ctx):
    if ctx.message.author.id in owners:
        await ctx.send("Bot is reloading, please wait a few seconds before sending commands.")
        exit()
    else:
        await ctx.send("hey, wait a minute, you're not the owner! you can't do that! >:(")        

@client.command()
async def ownersonly(ctx):
    if ctx.message.author.id in owners:
        await ctx.send("You are the owner of this application.")
        exit()
    else:
        await ctx.send("You're not the owner of this application.")         
        
client.run(bottoken)
