import os
import sys
import asyncio

from telethon import events
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd
from platform import uname


@bot.on(dev_cmd(pattern=r"pula"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 12)
    await event.edit("🚨 👮‍")
    animation_chars = [
        await asyncio.wait([e.edit("🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵")])
            f"{DEFAULTUSER} **🚨🚔 CHIAMATE IL CIENTODICIOTTOO!! 🚔🚨**"
