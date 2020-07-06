#By https://github.com/Kazutettoh/userbot_100101110  #all rights reserved

from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd("hello ?(.*)", outgoing=True))
async def kk(event):
    await event.edit("\n**╔┓┏╦━━╦┓╔┓╔━━╗**"
					           "\n**║┗┛║┗━╣┃║┃║╯╰║**"
					           "\n**║┏┓║┏━╣┗╣┗╣╰╯║**"
					           "\n**╚┛┗╩━━╩━╩━╩━━╝**")
					 
