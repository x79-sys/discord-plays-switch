import discord
from discord.ext import commands
import typing
import socket
import time
import binascii

bot = commands.Bot(command_prefix='>')

def sendCommand(s, content):
    content += '\r\n'
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.67", 6000))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def a(ctx):
    sendCommand(s, "click A")

@bot.command()
async def b(ctx):
    sendCommand(s, "click B")

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
async def up(ctx):
    sendCommand(s, "setStick LEFT yVal 0x7FFF")
    time.sleep(1)
    sendCommand(s, "setStick LEFT yVal 0x0000")

@bot.command()
async def down(ctx):
    sendCommand(s, "setStick LEFT yVal -0x8000")
    time.sleep(1)
    sendCommand(s, "setStick LEFT yVal 0x0000")

@bot.command()
async def left(ctx):
    sendCommand(s, "setStick LEFT -0x8000 0x0")
    time.sleep(1)
    sendCommand(s, "setStick LEFT 0x0 0x0")

@bot.command()
async def right(ctx):
    sendCommand(s, "setStick LEFT 0x7FFF 0x0")
    time.sleep(1)
    sendCommand(s, "setStick LEFT 0x0 0x0")

bot.run('your token here')
