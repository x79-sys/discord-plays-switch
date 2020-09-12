import discord
from discord.ext import commands
import typing
import socket
import asyncio
import binascii
import time

bot = commands.Bot(command_prefix='>')

def sendCommand(s, content):
    content += '\r\n'
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("Local switch ip here", 6000))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def a(ctx, poop: typing.Optional[int] = 1):
    for x in range(0, poop):
        sendCommand(s, "click A")
        await asyncio.sleep(1)

@bot.command()
async def b(ctx, poop: typing.Optional[int] = 1):
    for x in range(0, poop):
        sendCommand(s, "click B")
        await asyncio.sleep(1)

@bot.command()
async def y(ctx):
    sendCommand(s, "click Y")

@bot.command()
async def x(ctx):
    sendCommand(s, "click X")

@bot.command()
async def dup(ctx):
    sendCommand(s, "click DUP")

@bot.command()
async def ddown(ctx):
    sendCommand(s, "click DDOWN")

@bot.command()
async def dleft(ctx):
    sendCommand(s, "click DLEFT")

@bot.command()
async def dright(ctx):
    sendCommand(s, "click DRIGHT")

@bot.command()
async def r(ctx):
    sendCommand(s, "click R")

@bot.command()
async def l(ctx):
    sendCommand(s, "click L")

@bot.command()
async def plus(ctx):
    sendCommand(s, "click PLUS")


@bot.command()
async def up(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick LEFT yVal 0x7FFF")
    await asyncio.sleep(poop)
    sendCommand(s, "setStick LEFT yVal 0x0000")

@bot.command()
async def down(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick LEFT yVal -0x8000")
    await asyncio.sleep(poop)
    sendCommand(s, "setStick LEFT yVal 0x0000")

@bot.command()
async def left(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick LEFT -0x8000 0x0")
    await asyncio.sleep(poop)
    sendCommand(s, "setStick LEFT 0x0 0x0")

@bot.command()
async def right(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick LEFT 0x7FFF 0x0")
    await asyncio.sleep(poop)
    sendCommand(s, "setStick LEFT 0x0 0x0")

@bot.command()
async def cup(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick RIGHT yVal 0x7FFF")
    await asyncio.sleep(poop)
    sendCommand(s, "setStick RIGHT yVal 0x0000")

@bot.command()
async def cdown(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick RIGHT yVal -0x8000")
    await asyncio.sleep(poop)
    sendCommand(s, "setStick RIGHT yVal 0x0000")

@bot.command()
async def cleft(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick RIGHT -0x8000 0x0")
    await asyncio.sleep(poop)
    sendCommand(s, "setStick RIGHT 0x0 0x0")

@bot.command()
async def cright(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick RIGHT 0x7FFF 0x0")
    await asyncio.sleep(poop)
    sendCommand(s, "setStick RIGHT 0x0 0x0")
    
@bot.command()
async def lreset(ctx):
    sendCommand(s, "setSTick LEFT 0x0")

@bot.command()
async def rreset(ctx):
    sendCommand(s, "setSTick RIGHT 0x0")
    
@bot.command()
async def ur(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick LEFT yVal 0x7FFF")
    time.sleep(poop)
    sendCommand(s, "setStick LEFT 0x7FFF 0x0")
    time.sleep(poop)
    sendCommand(s, "setStick LEFT 0x0 0x0")

@bot.command()
async def ul(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick LEFT yVal 0x7FFF")
    time.sleep(poop)
    sendCommand(s, "setStick LEFT -0x8000 0x0")
    time.sleep(poop)
    sendCommand(s, "setStick LEFT 0x0 0x0")

@bot.command()
async def dr(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick LEFT yVal -0x8000")
    time.sleep(poop)
    sendCommand(s, "setStick LEFT 0x7FFF 0x0")
    time.sleep(poop)
    sendCommand(s, "setStick LEFT 0x0 0x0")

@bot.command()
async def dl(ctx, poop: typing.Optional[float] = .25):
    sendCommand(s, "setStick LEFT yVal -0x8000")
    time.sleep(poop)
    sendCommand(s, "setStick LEFT -0x8000 0x0")
    time.sleep(poop)
    sendCommand(s, "setStick LEFT 0x0 0x0")
    
bot.run('your token here')
