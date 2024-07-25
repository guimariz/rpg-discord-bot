import discord
from discord.ext import commands
from config import TOKEN
import os

# Configuração do bot
COGS = ("cogs.tisUser",)
INTENTS = discord.Intents.default()
INTENTS.message_content = True

bot = commands.Bot(command_prefix='.', intents=INTENTS)

# def carregar_cogs():
#     for arquivo in os.listdir('cogs'):
#         if arquivo.endswith('.py'):
#             bot.load_extension(f"cogs.{arquivo[:-3]}")
#             print(f'Cog {arquivo} carregado.')

@bot.event
async def setup_hook():
    # carregar_cogs()
    for cog in COGS:
        await bot.load_extension(cog)
bot.run(TOKEN)


# @bot.command(name='tis', description='Mostra os comandos disponíveis')
# async def tis(ctx: commands.Context):
#     comandos = """
#     Comandos disponíveis:
#     .mestrar
#     .criar_ficha - Crie ficha de personagens, objetos, cidades...
#     """
#     await ctx.send(comandos)

# @bot.command(name='mestrar', description='Abre o chat de mestragem')
# async def mestrar(ctx: commands.Context):
#     comandos = """
#     Comandos disponíveis:
#     .template - Escolha o template de ficha para a próxima sessão.
#     .criar_ficha - Crie ficha de personagens, objetos, cidades...
#     .criar_setup - Criar cenas, itens, opções de ficha...
#     .atribuir_ficha - Atribua uma ficha a algum jogador.
#     .salvar_setup - Salve!!!!!
#     .iniciar_sessao - Iniciar sessão!
#     """
#     await ctx.send(comandos)

# @bot.command(name='info')
# async def info(ctx: commands.Context):
#     await ctx.send('Eu sou um bot de RPG criado para ajudar a gerenciar suas sessões de jogo!')
