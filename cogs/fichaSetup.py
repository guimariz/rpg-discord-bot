# cogs/ficha_setup.py

import discord
from discord.ext import commands
from database import db

class FichaSetup(commands.Cog):
    '''
    Escolher setup de fichas
    Templates disponíveis:
        D&D 5e - em desenvolvimento
    '''
    def __init__(self, bot):
        self.bot = bot
        self.bot.tree.add_command(self.setup_ficha)

    @commands.command(name='setup_ficha')
    @commands.has_role('Mestre')
    async def setup_ficha(self, ctx):
        templates = db.templates.find()
        template_options = "\n".join([f"{template['name']}" for template in templates])
        await ctx.send(f"Escolha um template:\n{template_options}")

async def setup(bot):
    await bot.add_cog(FichaSetup(bot))
