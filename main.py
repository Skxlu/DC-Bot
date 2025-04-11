import discord, os
from discord.ext import commands

intents = discord.Intents.default()

bot = discord.Bot(intent=intents, debug_guilds=[None])

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Error")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error")
    elif isinstance(error, discord.errors.DiscordServerError):
        await ctx.send("Error")
    else:
        await ctx.send("unexpected error")
        print(f"Error: {error}")


if __name__ == '__main__':
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    bot.run('TOKEN')

