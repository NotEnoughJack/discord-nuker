# Discord "Kill Command" Bot (for Testing Purposes Only)

> ⚠️ **Disclaimer**: This bot is for **educational/testing purposes only** and should only be used in **your own servers** with appropriate permissions. Misuse of Discord bots to harm, disrupt, or spam other servers violates [Discord's Terms of Service](https://discord.com/terms) and may result in account or bot suspension.

## 📋 What It Does

This bot performs the following actions:

- Sends a **webhook notification** when it joins a new server.
- Waits until you send a `!kill` command in **your control server**.
- Upon command, it:
  - Randomly selects **one channel to keep** in the joined server.
  - **Deletes all other text channels**.
  - Starts a rapid `@everyone` spam in the remaining channel.

You can also use `!stop` to end the spam.

---

## ⚙️ Setup Guide

### 1. Clone the Code

Save the Python bot script to a file, for example:

"nuke.py"

### 2. Install Dependencies

Make sure you have Python 3.8+ installed.

Install the required packages:

```bash
pip install nextcord request
```
### 3. Create a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application and add a bot
3. Copy the bot token and replease "YOUR_NEW_BOT_TOKEN" in the script
4. Enable the required intents under the **Bot > Privileged Gateway Intents** section:

- Server Members
- Message Content

### 4. Create a Webhook
Create a webhook in your server to get notified when the bot joins a new server. Paste its URL into the script where it says:
```
WEBHOOK_URL = 'YOUR_WEBHOOK_URL'
```
### 5. Set Your Control Server ID 
Replace "GUILD_ID" with the **ID of the server you control**, from which you want to send the !kill "SERVER_ID" (Without the "")

### 6. Run the bot
```
py nuke.py
```
## Bot Commands

| Command             | Description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| !kill| Triggers the deletion of channels in the targeted server and starts @everyone spam |
| !stop | stops the @everyone spam |
**Note: The !kill command only works from your specified control server.**
# Required Bot Permissions
When adding the bot, make sure it has these permissions
- Administrator
- Manage channels
- Send messages

**You can use this OAuth2 permissions link (replace with your bot's client ID):**
```
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=8
```
# Disclaimer
- Discord uses rate limits, Rapid spamming will get rate limited
- deleting channels is irreversible
- always test in a controlled environment
