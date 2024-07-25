import discord
from discord.ui import Button, View

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

