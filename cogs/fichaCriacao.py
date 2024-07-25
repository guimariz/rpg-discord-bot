# cogs/ficha_criacao.py

import discord
from discord.ext import commands
from database import db
import random

class FichaCriacao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.tree.add_command(self.criar_ficha)
        self.bot.tree.add_command(self.criar_aleatorio)

    @commands.command(name='criar_ficha')
    @commands.has_role('Mestre')
    async def criar_ficha(self, ctx, template_name: str, personagem_name: str):
        template = db.templates.find_one({'name': template_name})
        if not template:
            await ctx.send('Template não encontrado!')
            return

        nova_ficha = {
            'nome': personagem_name,
            'template': template_name,
            'atributos': template['atributos'],
            'faculdades': template['faculdades']
        }
        db.fichas.insert_one(nova_ficha)
        await ctx.send(f'Ficha do personagem {personagem_name} criada com sucesso!')

    @commands.command(name='criar_aleatorio')
    @commands.has_role('Mestre')
    async def criar_aleatorio(self, ctx, template_name: str):
        template = db.templates.find_one({'name': template_name})
        if not template:
            await ctx.send('Template não encontrado!')
            return

        nome_aleatorio = f"Personagem_{random.randint(1000, 9999)}"
        nova_ficha = {
            'nome': nome_aleatorio,
            'template': template_name,
            'atributos': {key: random.randint(1, 10) for key in template['atributos'].keys()},
            'faculdades': {key: random.randint(1, 5) for key in template['faculdades'].keys()}
        }
        db.fichas.insert_one(nova_ficha)
        await ctx.send(f'Ficha do personagem {nome_aleatorio} criada com sucesso!')

async def setup(bot):
    await bot.add_cog(FichaCriacao(bot))
