import discord
import time
import json

client = discord.Client()
print("bot online")

with open("config.json","r")as filt:
    data = json.load(filt)
ID1 = data["id1"]
ID2 = data["id2"]
WORD = data['word']
TOKEN = data["token"]

@client.event
async def on_message(message):
    if message.channel.id == int(ID1):
        if message.author == client.user:
            return
        if message.content == "w":
            await message.add_reaction("⭕")
        else:
            await message.add_reaction("❌")
            time.sleep(0.5)
            await message.delete()
            channel = client.get_channel(int(ID2))
            await channel.send(f"{message.author.mention} 剛剛手殘輸入了: `{message.content}`")
            
client.run(TOKEN)
