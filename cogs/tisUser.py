import discord
from discord import app_commands
from discord.ext import commands

class Interacao(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("ready")
        # pass

    @commands.command(name='tis', description='Mostra os comandos disponíveis')
    async def tis(self, ctx: commands.Context) -> None:
        comandos = """
        Comandos disponíveis:
        .mestrar
        .criar_ficha - Crie ficha de personagens, objetos, cidades...
        """
        await ctx.send(comandos)

    @commands.command(name='mestrar', description='Abre o chat de mestragem')
    async def mestrar(self, ctx: commands.Context) -> None:
        comandos = """
        Comandos disponíveis:
        .template - Escolha o template de ficha para a próxima sessão.
        .criar_ficha - Crie ficha de personagens, objetos, cidades...
        .criar_setup - Criar cenas, itens, opções de ficha...
        .atribuir_ficha - Atribua uma ficha a algum jogador.
        .salvar_setup - Salve!!!!!
        .iniciar_sessao - Iniciar sessão!
        """
        await ctx.send(comandos)

    @commands.command(name='info')
    async def info(self, ctx: commands.Context) -> None:
        await ctx.send('Eu sou um bot de RPG criado para ajudar a gerenciar suas sessões de jogo!')

    @app_commands.command(name="tis", description="Mostra os comandos disponíveis")
    async def tis_slash(self, interaction: discord.Interaction) -> None:
        comandos = """
        Comandos disponíveis:
        .mestrar
        .criar_ficha - Crie ficha de personagens, objetos, cidades...
        """
        await interaction.response.send_message(comandos)

async def setup(bot):
    await bot.add_cog(Interacao(bot))
