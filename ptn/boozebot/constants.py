# Production variables
import ast
import os

from discord import Intents
from discord.ext import commands
from discord_slash import SlashCommand

PROD_DISCORD_GUILD = 800080948716503040  # PTN Discord server
PROD_ASSASSIN_ID = 806498760586035200

# Testing variables
TEST_DISCORD_GUILD = 818174236480897055  # test Discord server
TEST_ASSASSIN_ID = 806498760586035200

_production = ast.literal_eval(os.environ.get('PTN_BOOZE_BOT', 'False'))

# The bot object:
bot = commands.Bot(command_prefix='b.', intents=Intents.all())
slash = SlashCommand(bot, sync_commands=True)


def bot_guild_id():
    """
    Returns the bots guild ID

    :returns: The guild ID value
    :rtype: int
    """
    return PROD_DISCORD_GUILD if _production else TEST_DISCORD_GUILD


def get_custom_assassin_id():
    """
    Returns the custom emoji ID for assassin

    :returns: The object ID field
    :rtype: str
    """
    return PROD_ASSASSIN_ID if _production else TEST_ASSASSIN_ID
