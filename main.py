import discord
import embeds
from discord.ext import commands
from discord import app_commands
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
with open("channels.json") as f:
    channels = json.load(f)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} commands(s)')
    except Exception as e:
        print(e)
print(discord.Color.red())

@client.command()
async def embedall(ctx):
    dev_role = discord.utils.get(ctx.guild.roles, name="Developer")
    if not dev_role in ctx.author.roles:
        await ctx.send("You don't have permission to do that!")
        return
    howto = client.get_channel(channels['how-to-algomod'])
    link_discord = client.get_channel(channels['link-discord'])
    choosing_a_tier = client.get_channel(channels['choosing-a-tier'])
    incompatible_plugins = client.get_channel(channels['incompatible-plugins'])
    mods_list = client.get_channel(channels['mods-list'])
    # Triggered via '--embedall'
    # Sending embeds to How To Algomod Channel
    await howto.send(embed=embeds.step1_embed)
    await howto.send(embed=embeds.step2_embed)
    await howto.send(embed=embeds.step3_embed)
    await howto.send(embed=embeds.step4_embed)
    await howto.send(embed=embeds.help_embed)

    # Sending embeds to Link Discord Channel
    await link_discord.send(embed=embeds.link_discord_embed)

    # Sending embeds to Choosing a Tier Channel
    await choosing_a_tier.send(embed=embeds.choose_tier_embed)

    # Sending embeds to Incompatible Plugins Channel
    await incompatible_plugins.send(embed=embeds.incompatible_plugins_embed1)
    await incompatible_plugins.send(embed=embeds.incompatible_plugins_embed2)
    await incompatible_plugins.send(embed=embeds.incompatible_plugins_embed3)
    await incompatible_plugins.send(embed=embeds.incompatible_plugins_extra)
    
    # Sending embeds to Mods List Channel
    await mods_list.send(embed=embeds.mods_list_embed1)
    await mods_list.send(embed=embeds.mods_list_embed2)
    await mods_list.send(embed=embeds.mods_list_embed3)
    await mods_list.send(embed=embeds.mods_list_embed4)
    await mods_list.send(embed=embeds.mods_list_embed5)

client.run(token)