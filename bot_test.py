import discord
import openai
from collections import deque

intents = discord.Intents.default()
intents.message_content =True
client = discord.client(intents=intents)

dc_bot_token = ""

@client.event
async def on_ready():
    print("bot is ready")


messages = [{"role": "system", "content": "You are a helpful assistant"}]
openai.api_key = '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'

@client.event
async def on_message(message):
    if message.author == client.user:
          return
    await message.channel.send(message)

    
# async def on_message(message):
#     if message.author == client.user:
#         return
#     messages.append({"role": "assistant", "content": message})
#     completion = openai.ChatCompletion.create(
#         model = 'gpt-3.5-turbo',
#         messages = messages
#     )
#     chat_response = completion.choices[0].message.content
#     await message.channel.send(chat_response)
    



