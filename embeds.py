import discord

# -------------------------------------------------------------------------------------------
# Step 1 Information Initialization
# -------------------------------------------------------------------------------------------
step1_title = {
    "title": "How to AlgoMod: Step 1",
    "description": "*(all mods are pc exclusive and are for freeplay only)*",
    "color": discord.Color.red()
}
step1_embed = discord.Embed(**step1_title)
step1_embed.set_thumbnail(url="https://i.postimg.cc/kgTfMfYs/helpimage.jpg")
# Add the Patreon Subscription Step
step1_embed.add_field(name="**→ Step 1. Subscribe to the Patron ←**", value='''
    **a.** Go to https://www.patreon.com/, create an account and log in.\n
    **b.** Connect your Discord to your Patreon account ➤ <#1066870090475253790>\n
    **c.** Go to https://www.patreon.com/Algo_RL\n
    **d.** Choose a subscription tier, and join it ➤ <#1066871021166149674>
''')


# -------------------------------------------------------------------------------------------
# Step 2 Information Initialization
# -------------------------------------------------------------------------------------------
step2_title = {
    "title": "Step 2",
    "color": discord.Color.green()
}
step2_embed = discord.Embed(**step2_title)
# Add the Setup Step
step2_embed.add_field(name="**→ Step 2. Setting Up AlgoMod ←**", value='''
    **a.** Download the setup file in <#1104250418600624218> and extract it anywhere using a file unzipper like 7Zip or WinRAR.\n
    **b.** Double-Click to run the exe file. Your PC might warn you about the file, but you can press __"more info"__ and then __"run anyway"__.\n
    **c.** Read the license agreement carefully.\n
    **d.** Open Rocket League and make sure that Bakkesmod is injected, then press F2 to open the bakkesmod menu.
''')
step2_embed.add_field(name=" ", value='''
    **e.** Navigate to the "Plugins" tab on the top right, then find "Plugin Manager (beta)" on the right, and click "Open pluginmanager".\n
    **f.** Find AlgoMod, and check the box next to it.\n
    **g.** Check <#1066649585486929931> and turn off any plugins listed there.
''')


# -------------------------------------------------------------------------------------------
# Step 3 Information Initialization
# -------------------------------------------------------------------------------------------
step3_title = {
    "title": "Step 3.",
    "color": discord.Color.blue()
}
step3_embed = discord.Embed(**step3_title)
# Add the Verifying / Downloading Step
step3_embed.add_field(name="**→ Step 3. Veryfing / Downloading AlgoMods ←**", value='''
    **a.** Choose which mod(s) you would like ➤ <#1049770353385275392>\n
    **b.** Find your Steam / Epic ID ➤ <#1062405855741481093>\n
    **c.** Send your ID into the <#1114749589053001829> channel.\n      ➛ **After sending your ID, if you are Tier 1 or 2, message the mod name(s) of your choice using the bolded names shown.**\n
    **d.** Once you are verified, open AlgoMod and paste your Steam / Epic ID into the "DOWNLOADER" box.\n
    **e.** Click the "Download Mods" button, and it will automatically download the mods you chose during verification.
''')
step3_embed.add_field(name=" ", value='''
    **ⓘ If you are __Tier 3 or X__, download the "AllMods" zip in <#1104250418600624218> and extract it into your AlgoMod folder `(rocketleague/AlgoMod)`**
''')


# -------------------------------------------------------------------------------------------
# Step 4 Information Initialization
# -------------------------------------------------------------------------------------------
step4_title = {
    "title": "Step 4.",
    "color": discord.Color.purple()
}
step4_embed = discord.Embed(**step4_title)
# Add the Verifying / Downloading Step
step4_embed.add_field(name="**→ Step 4. Playing with AlgoMods ←**", value='''
    **a.** Click the box under the "INJECTOR" text in AlgoMod.\n
    **b.** Select the mod that you want to play with.\n
    **c.** Click the "Inject" button.\n
    **d.** Open Rocket League and choose a car compatible with your loaded mod\n
    **e.** Play freeplay with the map "Underpass - SOCCAR" selected (the map will change to normal automatically)\n
    ➛ **You change your map by pressing `F6` and typing `algo_map_mannfield` (of course you can change the map name to the map you want)**
''')


# -------------------------------------------------------------------------------------------
# Final Embed Information Initialization
# -------------------------------------------------------------------------------------------
helpembed_title = {
    "title": "Having Issues?",
    "description": 'Go to <#1066884919353163836> or go to the "Help" button in AlgoMod.',
    "color": discord.Color.gold()
}
help_embed = discord.Embed(**helpembed_title)

# -------------------------------------------------------------------------------------------
# Link Discord Steps Information Initialization
# -------------------------------------------------------------------------------------------

link_discord_title = {
    "title": "Linking your Discord to Patreon",
    "color": discord.Color.teal(),
    "url": "https://www.patreon.com/Algo_RL"
}
link_discord_embed = discord.Embed(**link_discord_title)
link_discord_embed.add_field(name="", value='''
    **1.** On the Patreon website, go to __"Settings"__ on the left.\n
    **2.** Select __"More"__ at the top right.\n
    **3.** Select __"Connected Apps"__.\n
    **4.** Press __"Connect"__ for Discord.\n
    **5.** Make sure you're using the correct Discord account, and select __"Authorize"__.
''')

# -------------------------------------------------------------------------------------------
# Choosing A Tier Steps Information Initialization
# -------------------------------------------------------------------------------------------

choose_tier_title = {
    "title": "Choosing a Tier",
    "url": "https://www.patreon.com/Algo_RL",
    "color": discord.Color.pink()
}
choose_tier_embed = discord.Embed(**choose_tier_title)
choose_tier_embed.add_field(name='Choose a Mod', value='''
    **1.** Choose a mod from <#1049770353385275392>\n
    **2.** If the mod you want is classified as a **"Premium Mod"**, you're going to need a Tier that has Premium mod Credits (ex. Tier 2 & Tier 3)
''')
choose_tier_embed.add_field(name='Tiers', value='''
    **Tier 1:** With Tier 1, you get a single (1) basic mod.\n
    **Tier 2:** With Tier 2, you get 2 basic mods, and 1 premium mod.\n
    **Tier 3:** With Tier 3, you get unlimited access to all mods; basic and premium.
''')
choose_tier_embed.add_field(name='', value="")
choose_tier_embed.add_field(name='', value="*Note: Subscription is done on a per month basis. Unsubscribing from the Patreon will result in you being unverified.", inline=True)

# -------------------------------------------------------------------------------------------
# Incompatible Plugins Information Initialization
# -------------------------------------------------------------------------------------------

incompatible_plugins_title = {
    "title": "Incompatible Plugins",
    "color": discord.Color.blue()
}
incompatible_plugins_embed1 = discord.Embed(**incompatible_plugins_title)
incompatible_plugins_embed1.add_field(name="Crashes:", value="**TimeTrackerPlugin.dll** ➤ __https://bakkesplugins.com/plugins/view/315__", inline=True)

incompatible_plugins_embed2 = discord.Embed(color=discord.Color.blurple())
incompatible_plugins_embed2.add_field(name="Stops Verification (error 6):", value='''
    **CustomBindingsPlugin2.dll** ➤ __https://bakkesplugins.com/plugins/view/228__\n
    **MapExpansionPlugin.dll** ➤ __https://bakkesplugins.com/plugins/view/294__\n
    **RipCore.dll** ➤ *(private mod)*
''', inline=True)

incompatible_plugins_embed3 = discord.Embed(color=discord.Color.purple())
incompatible_plugins_embed3.add_field(name="Causes Lag:", value="**SpeedrunTools.dll** ➤ __https://bakkesplugins.com/plugins/view/165__ *(turns off automatically)*", inline=True)

incompatible_plugins_extra = discord.Embed(description="*If you find any more, please tell Salad or Ruasi in <#1049785049358278676>")

# -------------------------------------------------------------------------------------------
# Mods List Information Initialization
# -------------------------------------------------------------------------------------------
mods_list_title = {
    "title": "Mods List",
    "color": discord.Color.blue(),
    "description": "Choose from a list of mods to use!"
}
mods_list_embed1 = discord.Embed(**mods_list_title)
mods_list_embed1.add_field(name="**Custom Cosmetics**", value='''
    <#1049774247108690041>
    <#1049774356181557399>
''')
mods_list_embed2 = discord.Embed(color=discord.Color.blurple())
mods_list_embed2.add_field(name="**Workshop Maps**", value='''
    <#1049774870822670377>
    <#1049774952619970571>
    <#1049780110338822184>
''')
mods_list_embed3 = discord.Embed(color=discord.Color.purple())
mods_list_embed3.add_field(name="**Premium Mods** ➤ *Patreon Exclusive*", value='''
    <#1049779757056802916>
    <#1080680116117569546>
    <#1049778723408330884>
    <#1049779883892539462>
''')
mods_list_embed4 = discord.Embed(color=discord.Color.dark_purple())
mods_list_embed4.add_field(name="**Basic Mods** ➤ *Patreon Exclusive*", value='''
    <#1185927198453018765>
    <#1049778212391104563>
    <#1080680041056317441>
    <#1062410219755421727>
    <#1049778002004811917>
    <#1080679947414274139>
    <#1049777490551394384>
    <#1049777713113735209>
    <#1049774556212105268>
''')
mods_list_embed5 = discord.Embed(color=discord.Color.dark_embed())
mods_list_embed5.add_field(name="", value="More mods coming soon!")