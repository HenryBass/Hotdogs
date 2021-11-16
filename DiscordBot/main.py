import discord
import os
from keepup import keepup
import random

client = discord.Client()

messages = ["Message 1", "Message 2", "Message 1"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith("!hotdog"):
    with open('hotdogs/Hotdog#' + str(random.randrange(0, 155, 1)) + '.jpg', 'rb') as f:
      picture = discord.File(f)
      await message.channel.send(file=picture)
      await message.channel.send(random.choice(messages))
  

 
keepup()
client.run(os.getenv('TOKEN'))
