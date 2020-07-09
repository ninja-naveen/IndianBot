"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
INDIANBOT_IS_ALIVE = ("**Ninja Naveen's UserBot** \n`🇳BOT Status : ` **Pro Like Ninja Naveen**\n\n"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "`Ninja Bot Version:` 2.3\n`Python:` **3.7.4**\n"
                     "**Join the Bot Creator's Channel** : [💠Royal Giveaways💠](t.me/royal_giveaway)\n"
                     "**Join the Bot Creator's Group** : [💠Royal Giveaways Chat💠](t.me/royalgiveawaychat)\n\n"
                     "**USERBOT By** [🔥Ninja Naveen🔥](t.me/NinjaNaveen)\n\n"
                     "Copyright [Ninja Naveen](t.me/NinjaNaveen)") 


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_message(chat, INDIANBOT_IS_ALIVE) 
