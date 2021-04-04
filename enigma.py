#this one is just importing stuff
import random
import discord
from discord.ext import commands

#setting prefix to the command
client = commands.Bot(command_prefix = "pepe!")

#this only starts the app without waiting for stuff to load
@client.event
async def on_ready():
    print('pepe is here')

@client.event
async def on_member_join(member):
    print(f'{member} has joined')

@client.event
async def on_member_remove(member):
    print(f'{member} has been yeeted')


#sends a message after recieving a question (requires a question)
@client.command()
async def tell_me(ctx,*,question):
    responses = [
        "yes",
        "no",
        "ofc",
        "look at dis dood ... ofc not, tf",
        "idk idc, I'm just a bot",
        "lmfao"]

    await ctx.send(f'{random.choice(responses)}')

#returns a boolean value for a "can i" sort of questions
@client.command()
async def can_i(ctx,*,question):
    responses = [
        "you know you're in Algeria, right?",
        "by the will of Allah",
        "possible",
        "stop dreaming"]
    await ctx.send(f'{random.choice(responses)}')
#spams input
@client.command()
async def spam(ctx,*,question):
    for i in range(5):
            await ctx.send(f'{question}') 


#deletes messages adding an amount is optional, if it's not set it deletes 10 messages
@client.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount)

#gtfo
#kick
@client.command()
async def kick(ctx, member : discord.Member, * , reason=None):
    await member.kick(reason=reason) 

#ban
@client.command()
async def ban(ctx, member : discord.Member, * , reason=None):
    await member.ban(reason=reason) 

#this is my special token every bot has one, get yours.

client.run('')
