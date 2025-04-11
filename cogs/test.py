import discord
from discord.ext import commands
from discord.commands import slash_command

class Verify(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        self.client.add_view(Button())

    @slash_command()
    async def test(self, ctx):
        await ctx.respond("Hs")
        await ctx.channel.send("Text", view=Button())

def setup(client):
    client.add_cog(Verify(client))


class Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label="Hi", custom_id="hi", style=discord.ButtonStyle.green)
    async def hi(self, button, interaction):
        await interaction.response.send_message("Hello", ephemeral=True)