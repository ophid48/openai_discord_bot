import random

from api_secrets import API_KEY, discord_bot_api
import openai
import discord
from discord.ext import commands

openai.api_key = API_KEY

config = {
    'token': discord_bot_api,
    'prefix': '$'
}
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def q(ctx, *args):
    q = ' '.join([str(elem) for elem in args])
    print(q)
    await ctx.reply(generate_request(q))


def generate_request(q):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=q,
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text
bot.run(config['token'])

