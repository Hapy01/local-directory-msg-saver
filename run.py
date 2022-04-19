#LIBS---
from asyncio import wait
from cgi import print_form
from email import message
from urllib import response
import discord
import json
from urllib.request import urlopen
import os
import discord
from pathlib import *
from discord.ext import commands

#VARIABLES---
client = discord.Client()
prefix = "."

#MAIN SCRIPT

print("Loaded Prefix - " + "> " + prefix + " <")

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if message.content.startswith(prefix + 'giveupdate'):
        parts = message.content.split(' ')
        del parts[0]
        number = 1
        msg = ' '.join(parts)
        for k in range(number):
            await message.channel.send(file=discord.File("message.txt"))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if message.content.startswith(prefix + 'writefile'):
        parts = message.content.split(' ')
        del parts[0]
        number = 1
        msg = ' '.join(parts)
        for k in range(number):
            f = open("message.txt", "a")
            f.write(msg + "\n")
            await message.channel.send(msg + " has been sent to database ")


#f = open("message.txt", "a")
#f.write(msg + "\n")
#wait message.channel.send(msg + " has been sent to database ")


#await ctx.send(file=discord.File(“path_to_text_file”))
#apiurl = "https://dog-api.kinduff.com/api/facts"
#response = urlopen(apiurl)
#data_json = json.loads(response.read())
#wait message.channel.send(data_json["facts"])
            
client.run('OTY1MTIwMDM4MzI5ODAyODAy.YlukFA.tbFMKdozSa8iPUABPWatjh3T-Ns')