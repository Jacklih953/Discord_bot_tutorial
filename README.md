# Discord_bot_tutorial
## 4/12 國北教大 Discord Bot 教學

### 下載清單 

- Miniconda--https://docs.conda.io/en/latest/miniconda.html

- Vscode--https://code.visualstudio.com/

- requirement.txt

### Anaconda Prompt 指令
- conda create -n "環境名字" python=3.9     
- conda activate "環境名字"

### Pip 指令
- pip install -r requirement.txt


### Discord_bot_api
https://discord.com/developers/applications

#### 點擊New Application
![螢幕擷取畫面 2023-04-11 211844](https://user-images.githubusercontent.com/85166729/231175230-ee2eeda2-01a3-4eed-a58a-a966ce5ed4b1.png)
### 點擊Bot -> Add Bot
![螢幕擷取畫面 2023-04-11 212044](https://user-images.githubusercontent.com/85166729/231175787-e72d1268-7f4a-4d5e-8c15-20b4f70f595c.png)

![image](https://user-images.githubusercontent.com/85166729/231176456-ba6c49f7-296a-4269-90ca-e43dd2df7d94.png)
### 點擊View Token，將Token儲存起來
![image](https://user-images.githubusercontent.com/85166729/231176768-0186c0ed-ef55-49f9-960a-549ba1b78b7f.png)

### 將Administrator勾選
![螢幕擷取畫面 2023-04-11 212630](https://user-images.githubusercontent.com/85166729/231177510-4ecbb75d-8747-400a-a0ac-b064d4425497.png)

### 點選OAuth2 -> URL Generator -> 勾取 Bot -> 勾取 Administrator
![螢幕擷取畫面 2023-04-11 212914](https://user-images.githubusercontent.com/85166729/231178291-51a41f4c-9faf-44b6-b3ed-80db824e7f01.png)


### Openai API key
https://platform.openai.com/account/api-keys
![螢幕擷取畫面 2023-04-11 220010](https://user-images.githubusercontent.com/85166729/231187111-5e62457b-5d8c-472e-9a58-a64e5a0ccc92.png)


### Discordbot api
https://discordpy.readthedocs.io/en/stable/api.html

```python
import discord
import openai
from discord.ext import commands

dc_bot_token = "Your token "

messages = [{"role": "system", "content": "You are a helpful assistant"}]
openai.api_key = 'Your api key'

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

```
