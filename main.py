import discord
from discord.ext import commands
from datetime import datetime
import embeds
import os
import json
from dotenv import load_dotenv
import random

load_dotenv('../.env')
token = os.environ.get("HELPER_DISCORD_TOKEN")
if not token:
    print("Token is unreachable")
    exit()
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix="--", intents=intents)

# making 

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} commands(s)')
    except Exception as e:
        print(e)


@client.command()
async def embedall(ctx):
    # Triggered via '--embedall'
    dev_role = discord.utils.get(ctx.guild.roles, name="Developer")
    if not dev_role in ctx.author.roles:
        await ctx.send("You don't have permission to do that!")
        return
    for embed, channel in embeds.embeds_list:
        await client.get_channel(channel).send(embed=embed)

@client.command()
async def flip(ctx):
    if not ctx.author == client.user:
        await ctx.reply(random.choice(['heads!', 'tails!']))

with open("dm_responses.json", "r") as f:
    responses = json.load(f)

async def problem():
    await client.get_channel(1214338432059441234).send(f"<@1141450692171665508> the bot ran into an issue with a user and needs ATTENTION ASAP")

@client.event
async def on_message(message):
    with open("user_dms.txt", 'r') as f:
        users = f.readlines()   # used to check if the user has messaged the bot before
    await client.process_commands(message) # process commands first if the message is a command (passes anyways)

    if not message.guild and message.author != client.user:     # rest of the function only runs if DM'ed
        time = message.created_at.strftime("%Y-%m-%d @ %H:%M:%S")
        await client.get_channel(1214337022022656102).send(f"User: <@{message.author.id}>\nMessage: `{message.content}`\nTime: `{time}`")
        if (str(message.author) not in [user.replace("\n", "") for user in users]) or message.content.upper() == "HELP": # if the user has not messaged the bot before or if the user said "HELP"
            try:
                # await message.channel.send("this is a reply to the dm")
                dm_embed = discord.Embed(title="Need Some Help?", description="If one of these questions applies to you, respond with the number next to your question!", color=discord.Color.blurple())
                dm_embed.add_field(name="", value='''
                    **1.** I don't have roles after joining Algo's Patreon\n
                    **2.** I don't see AlgoMod in my Plugin Manager\n
                    **3.** When I inject a mod and go into Labs Underpass in freeplay, it loads Labs Underpass instead of my mod\n
                    **4.** When I load in, it tells me "error 6" OR I crash\n
                    **5.** When I load in, it tells me I don't have access to this mod
                ''')
                await message.channel.send(embed=dm_embed)
                if message.content.upper() != "HELP":
                    with open("user_dms.txt", "a") as f:
                        f.write(f"{message.author}\n")      # add the user to the DM list
                        print(f"User \"{message.author}\" added to DMs list")
            except discord.errors.Forbidden:
                await problem()
                print("Forbidden Error!! idk whats happening lol")
                pass
        elif message.content.upper() in list(responses.keys()):
            try:
                if not responses[str(message.content.upper())]:
                    await message.channel.send(f"An error occurred, one sec lol")
                await message.channel.send(f"{responses[str(message.content.upper())]}")
            except discord.errors.Forbidden:
                await problem()
                print("Forbidden Error!! idk whats happening lol")
                pass
        else:
            try:
                await message.channel.send("Sorry, I can't understand that response. Please choose which number fits your question if applicable, and if none of the questions apply, respond with \"MORE HELP\"")
            except discord.errors.Forbidden:
                await problem()
                print("Forbidden Error!! idk whats happening lol")
                pass

client.run(token)