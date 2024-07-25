import discord
from discord.ext import commands
from config import TOKEN
import os

# Configuração do bot
intents = discord.Intents.all()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='.', intents=intents)

def carregar_cogs():
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            bot.load_extension(f"cogs.{arquivo[:-3]}")
            print(f'Cog {arquivo} carregado.')

@bot.event
async def on_ready():
    try:
        carregar_cogs()
        await bot.tree.sync()  # Sincronizar os comandos de interação (slash commands)
        print(f'Bot conectado como {bot.user}')
    except:
        print("erro ao carregar")
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
