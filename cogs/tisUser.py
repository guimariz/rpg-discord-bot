import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from database import db 

class MestrarView(View):
    def __init__(self, bot, author):
        super().__init__()
        self.bot = bot
        self.author = author

    @discord.ui.button(label="Criar um novo RPG", style=discord.ButtonStyle.primary)
    async def create_rpg(self, interaction: discord.Interaction, button: Button):
        guild = interaction.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            self.author: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await guild.create_text_channel(f'novo-rpg-{self.author.name}', overwrites=overwrites)
        await interaction.response.send_message(f'Canal {channel.mention} criado para o novo RPG!', ephemeral=True)

    @discord.ui.button(label="Abrir um RPG salvo", style=discord.ButtonStyle.secondary)
    async def open_rpg(self, interaction: discord.Interaction, button: Button):
        guild = interaction.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            self.author: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await guild.create_text_channel(f'rpg-salvo-{self.author.name}', overwrites=overwrites)
        await interaction.response.send_message(f'Canal {channel.mention} criado para abrir um RPG salvo!', ephemeral=True)

class tisUser(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot
        self.rpg_collection = db['rpgs']

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
        # Verifica se o autor da mensagem tem o cargo de "Mestre"
        role_names = [role.name for role in ctx.author.roles]
        if 'Mestre' in role_names:
            view = View()

            criar_button = Button(label="Criar um novo RPG", style=discord.ButtonStyle.green)
            abrir_button = Button(label="Abrir um RPG salvo", style=discord.ButtonStyle.primary)

            async def criar_rpg(interaction: discord.Interaction):
                await interaction.response.send_message("Por favor, digite o nome do novo RPG:")

                def check(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel

                nome_rpg_msg = await self.bot.wait_for('message', check=check)
                nome_rpg = nome_rpg_msg.content
                nome_chat = f"{nome_rpg.lower().replace(' ', '-')}-{ctx.author.name.lower()}"

                # Criação do novo canal
                guild = ctx.guild
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    ctx.author: discord.PermissionOverwrite(read_messages=True)
                }
                new_channel = await guild.create_text_channel(nome_chat, overwrites=overwrites)

                # Registro no MongoDB
                self.rpg_collection.insert_one({
                    'nome_rpg': nome_rpg,
                    'nome_chat': nome_chat,
                    'mestre': ctx.author.id
                })

                await interaction.followup.send(f"O RPG '{nome_rpg}' foi criado com sucesso no canal {new_channel.mention}!")

            async def abrir_rpg(interaction: discord.Interaction):
                rpgs = self.rpg_collection.find({'mestre': ctx.author.id})
                if rpgs.count() == 0:
                    await interaction.response.send_message("Você não tem nenhum RPG salvo.")
                    return

                rpgs_list = [rpg['nome_rpg'] for rpg in rpgs]
                rpgs_message = "RPGs salvos:\n" + "\n".join(rpgs_list)
                await interaction.response.send_message(rpgs_message)

            criar_button.callback = criar_rpg
            abrir_button.callback = abrir_rpg

            view.add_item(criar_button)
            view.add_item(abrir_button)

            await ctx.send("Escolha uma opção:", view=view)
        else:
            await ctx.send("Você não tem o cargo de Mestre. Por favor, peça a um administrador para atribuir o cargo a você.")

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

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if not message.content.startswith('.') or message.content.split()[0][1:] not in ['tis', 'mestrar', 'info']:
            await message.delete()
            return

async def setup(bot):
    await bot.add_cog(tisUser(bot))

