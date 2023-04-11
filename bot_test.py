import discord
import openai
from discord.ext import commands

dc_bot_token = "MTA5NTMzNzQ3ODk3NTY3MjM2Mg.Glimpa.SHyTFnBOTlJiWWCh5VsN2PBybhC2vhfZm5ZUxw"

messages = [{"role": "system", "content": "You are a helpful assistant"}]
openai.api_key = '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'

intents = discord.Intents.default()
intents.message_content =True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(client.user, "bot is ready！！")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user_input = message.content
    messages.append({"roel": "user", "content": user_input})
    completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages
        )
    chat_response= completion.choices[0].message.content
    await message.channel.send(chat_response)

client.run(dc_bot_token)