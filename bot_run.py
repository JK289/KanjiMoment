import logging
import hikaro
import nextcord
from nextcord import SlashOption, Interaction
from nextcord.ext import commands

logging.basicConfig(level=logging.INFO)

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

TESTING_GUILD_ID = 1079551651402219570  # guild ID for server testing
TOKEN = 'bot token goes here'

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'{bot.user} is online')


@bot.slash_command(description='hello', guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send('buenos dias')


@bot.slash_command(guild_ids=[TESTING_GUILD_ID], description='write in katakana, hiragana, romaji')
async def writing_system(
        interaction: Interaction,
        word_to_translate: str = SlashOption(description='word to translate', required=False),
        from_script: str = SlashOption(description="from: romaji, hiragana, katakana", required=False),
        to_script: str = SlashOption(description="to: romaji, hiragana, katakana", required=False),
):
    if not word_to_translate:
        await interaction.response.send_message("Tell me a word!", ephemeral=True)
    else:

        translated = hikaro.tte(word_to_translate, from_script, to_script)

        await interaction.response.send_message(f'{translated}')


bot.run(TOKEN)
