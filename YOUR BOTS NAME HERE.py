import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
#your prefix here
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'YOUR COMMENT HERE')
    print('Sent message to ' + member.name)
    
@client.event   
async def on_ready():
    await client.change_presence(game=Game(name='YOUR GAME OR MUSIC HERE'))
    print('Running...PUT LITTERALY ANYTHING YOU WANT HERE ') 

#Simple text response 
#switch ping for your input message 
#switch pong for the output message
@client.event
async def on_message(message):
    if message.content == 'ping':
        await client.send_message(message.channel,'pong')   

#the bot can recognize help anywhere in the message
#switch "help" for your input message 
#switch "what do you need help with good sir?" for the output message
    if ('help') in message.content:
        await client.send_message(message.channel,'what do you need help with good sir?')
        
#the bot can recognize "hey" if it's the first word in the message
#switch "hey" for your input message 
#switch "heeellloooo there" for the output message
    if message.content.startswith ('hey'):
        await client.send_message(message.channel,'heeellloooo there')

#making your bot delete messages
 @client.command(pass_context = True, aliases=['Clear'])
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an 
    integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
    
#bot mentions other users  
    if ('frick') in message.content:
        msg = '{0.author.mention}+ HEY!!!! \nNo bad words!!!'.format(message)
        await client.send_message(message.channel,msg)
        await client.delete_message(message)
client.run('token')
