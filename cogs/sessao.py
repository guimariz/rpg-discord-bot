import discord
from discord.ext import commands
from database import db

class Sessao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.tree.add_command(self.iniciar_sessao)

    @commands.command(name='iniciar_sessao')
    @commands.has_role('Mestre')
    async def iniciar_sessao(self, ctx):
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            discord.utils.get(ctx.guild.roles, name="Mestre"): discord.PermissionOverwrite(read_messages=True)
        }
        session_channel = await ctx.guild.create_text_channel(name=f'sessao-{ctx.author.name}', overwrites=overwrites)
        await session_channel.send('Sessão iniciada!')

        for member in ctx.guild.members:
            if discord.utils.get(member.roles, name="Jogador"):
                await session_channel.set_permissions(member, read_messages=True, send_messages=True)
                gameplay_channel = await ctx.guild.create_text_channel(name=f'gameplay-{member.name}', overwrites=overwrites)
                await gameplay_channel.send('Bem-vindo ao chat de gameplay!')
                await gameplay_channel.set_permissions(ctx.author, read_messages=False, send_messages=False)

async def setup(bot):
    await bot.add_cog(Sessao(bot))
