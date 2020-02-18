import asyncio
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="1")

@bot.event
async def on_ready():
    print("Connected and ready to use")

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(pass_context=True)
async def magic8ball(ctx):
    await ctx.send(random.choice(["shorline",
                                  "customs",
                                  "reserve",
                                  "interchange",
                                  "woods"]))

bot.run("Njc5MTcwNDczODQ1NTg3OTc4.XkuLoQ.OdynXQ13aEmAh7mnx9EK5VR_qv0")
