import os
from pyrogram import Client, filters

Motechyt = Client(
            "MT WELCOME BOT",
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"]
)

@Motechyt.on_message(filters.private & filters.command("start"))
async def start(bot, update):  
    text = f"""
<b> 👋Hello {update.from_user.mention}</b>
"""
    await update.reply_text(
        text=text,
        disable_web_page_preview=True
  )

Motechyt.run()
