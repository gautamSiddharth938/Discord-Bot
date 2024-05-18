import discord
import os
import requests 
import random
import json
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
joyful_words = ["happy", "cheerful", "excited", "thrilled", "ecstatic"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]
happy_suggestions = [
  "Wonderfull! to hear that, Happy for you.",
  "You are a great person and always keep one thing in mind that there are always someone for ou who loves you and cares for you!"
]
# client = discord.Client()

def get_quote():
  # response = requests.get("https://zenquotes.io/api/random")
  response = requests.get("https://api.quotable.io/quotes/random?tags=history|civil-rights")
  # https://msrinitha.github.io/Quote-Generator/
  json_data = json.loads(response.text)
  quote = json_data[0]['content'] + " -" + json_data[0]['author']
  return(quote)

def get_joke():
  # response = requests.get("https://zenquotes.io/api/random")
  responses = requests.get("https://official-joke-api.appspot.com/random_joke")
  # https://msrinitha.github.io/Quote-Generator/
  json_data = json.loads(responses.text)
  joke = json_data[0]['setup'] + " -" + json_data[0]['punchline']
  return(joke)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$history'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('make me laugh'):
    joke = get_joke()
    await message.channel.send(joke)
    
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if any(word in msg for word in joyful_words):
    await message.channel.send(random.choice(happy_suggestions))

# client.run('MTIyOTgxODk4MDE4OTk5NTAxOA.GPp1Fp.b8MSFPWVXmQ4X9LI0wQxGhiZTNTp4HRDXp6FW0')
client.run(os.getenv('SECRET_KEY'))