import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'welcome i am the BFG info bot')
    print('Sent message to ' + member.name)
@client.event   
async def on_ready():
    await client.change_presence(game=Game(name='war Robots'))
    print('Running... ') 


@client.event
async def on_message(message):
    if message.content == 'ping':
        await client.send_message(message.channel,'pong')
    if message.content == 'Ping':
        await client.send_message(message.channel,'pong')
      

        #intro base commands: "!intro, !help" output comands: "!stats, !bots, !weapons"
    if message.content == '!intro':
        await client.send_message(message.channel,'welcome to BFGs headquarters for stats on our guild ask "!stats". \n for info on bots ask"!bots". \n for info on weapons ask "!weapons"')
    if message.content == '!help':
        await client.send_message(message.channel,'welcome to BFGs headquarters for stats on our guild ask "!stats". \n for info on bots ask"!bots". \n for info on weapons ask "!weapons"')
    if message.content == 'help':
        await client.send_message(message.channel,'welcome to BFGs headquarters for stats on our guild ask "!stats". \n for info on bots ask"!bots". \n for info on weapons ask "!weapons"')    
    if ('help') in message.content:
        await client.send_message(message.channel,'welcome to BFGs headquarters for stats on our guild ask "!stats". \n for info on bots ask"!bots". \n for info on weapons ask "!weapons"')
        
        #bots base commands: "!bots" output commands: "!bot [bot name],!bots [light], [medium], [heavy] "
    if message.content == '!bots':
        await client.send_message(message.channel,'there are many types of bots catagorized by the following. \n light \n Medium \n heavy \n for info on the catagories ask "!bots [light], [medium], [heavy]" \n for info on a specific bot ask "!bot [bot name]')



    if message.content == '!bot [bot name]':
        await client.send_message(message.channel,'pong')


        

    if message.content == '!bots light':
        await client.send_message(message.channel,'JESSE\nGARETH\nGEPARD\nDESTRIER\nSTALKER\nCOSSACK\nSCHUTZE')
    if message.content == '!bots medium':
        await client.send_message(message.channel,'NEMESIS\nHADES\nRAYKER\nBLITZ\nARES\nWAYLAND\nINVADER\nMENDER')
    if message.content == '!bots heavy':
        await client.send_message(message.channel,'BUTCH\nLANCELOT\nNATASHA\nGRIFFIN\nRHINO\nFURY\nRAIJIN\nLEO')


     #stats base commands: "!stats" output commands:
        
    if message.content == '!stats':
        await client.send_message(message.channel,'In beta testing')

     #waepons base commands: "!weapons" output commands:   

    if message.content == '!weapons':
        await client.send_message(message.channel,'in beta testing')

    if ('frick') in message.content:
        await client.send_message(message.channel,'HEY!!!! \nNo bad words!!!')




    if message.content.startswith ('hey'):
        msg = '{0.author.mention}'.format(message)
        await client.send_message(message.channel,msg)
        
  
        
client.run('NTEwMjE1NzA5NjUzOTkxNDM1.DsjDeQ.3zYvau7sA42qyt_nKjmyQbE_7h0')
