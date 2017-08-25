import discord, random
from discord.ext.commands import Bot
from discord.ext import commands

rollbot = Bot(command_prefix="!")

def getRoll():
    roll = random.randint(10000000,99999999)
    return roll

def has_doubles(n,dub):
    return(len(set((str(n))[-dub:])) < 2)

def get():
    f = getRoll()

    #dubs,trips,quads,quints
    if (has_doubles(f,5)):
        return("You rolled %s - you get QUINTS!!!"%(str(f)))
    elif (has_doubles(f,4)):
        return("You rolled %s - you get QUADS!!!"%(str(f)))
    elif (has_doubles(f,3)):
        return("You rolled %s - you get TRIPS!!"%(str(f)))
    elif (has_doubles(f,2)):
        return("You rolled %s - you get DUBS!"%(str(f)))
    else:
        return("You rolled %s!"%(str(f)))

@rollbot.event
async def on_ready():
        print("Client logged in!")
        await rollbot.change_presence(game=discord.Game(name='Roll Simulator 2017'))

@rollbot.command("roll")
async def roll():
        return await rollbot.say(get())

rollbot.run(#your key here)
