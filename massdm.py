import discord
import termcolor
import sys
import colorama
from discord.ext import commands
import asyncio
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored, cprint

intents = discord.Intents.all()
client=commands.Bot(command_prefix='//', self_bot=True, intents=intents)

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prGrey(skk): print("\033[90m {}\033[00m" .format(skk))

@client.command()
async def dmall(ctx, *, message):
    #dms all users in your current guild
    await ctx.message.delete()
    for member in ctx.guild.members:
        
        if member == client.user:
            continue
            
        try:
            await member.send(message)
        except discord.Forbidden:
            prRed(f"[-] {member.name} could not be dmed")
        else:
            prGreen(f"[+] {member.name} has recieved a dm with the content [-{message}-]")
            await ctx.send(f'`dmed {member.name}`', delete_after=2)
            
    prGrey("[>] dmall complete")

@client.command()
async def spampin(ctx, count=15):
    #spam pin a certain amount of messages default is 15 but can be changed e.g //spampin 5
    await ctx.message.delete()
    if count == None:
        count = 15
    else:
        async for message in ctx.message.channel.history(limit=int(count)):
            try:
                await message.pin()
                prGreen('[+] pinned messages')
            except:
                prRed('[-] failed to pin messages')
                pass
    prGrey('[>] spampin complete')

@client.event
async def on_ready():
    prGrey(f'[>] mass dm online')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#hi sorry for self promo but check out my bot here = https://discord.ly/knife ;)++#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

client.run('your-token-here', bot=False)