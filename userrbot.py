from telethon import TelegramClient, events
import asyncio
import random
import time

api_id = 33293988
api_hash = "b9c729dbe75a396f6fc9637e4b57dfa0"

bot = TelegramClient(
    "userbot",
    api_id,
    api_hash
)

start_time = time.time()


@bot.on(events.NewMessage(pattern=r"\.ping"))
async def ping(event):

    start = time.time()

    await event.edit("🏓 Pong...")

    end = round((time.time() - start) * 1000)

    await event.edit(
        f"🏓 Pong: `{end}ms`"
    )


@bot.on(events.NewMessage(pattern=r"\.help"))
async def help_cmd(event):

    text = """
🌘 USERBOT HELP

⚡ Main:
.ping
.help
.info

🎭 RP:
.hug
.kiss
.slap
.hum
.kick

🎲 Fun:
.iq
.gay
.hack
"""

    await event.edit(text)


@bot.on(events.NewMessage(pattern=r"\.info"))
async def info(event):

    me = await bot.get_me()

    uptime = int(time.time() - start_time)

    text = f"""
╔═══ 🌘 USERBOT INFO 🌘 ═══╗

👤 Nick: {me.first_name}
🆔 ID: {me.id}
⚡ Status: Online
⏳ Uptime: {uptime}s
🐍 Python UserBot

╚══════════════════════════╝
"""

    photos = await bot.get_profile_photos(
        me.id,
        limit=1
    )

    if photos:

        await bot.send_file(
            event.chat_id,
            photos[0],
            caption=text
        )

        await event.delete()

    else:

        await event.edit(text)


@bot.on(events.NewMessage(pattern=r"\.iq"))
async def iq(event):

    iq = random.randint(1, 300)

    await event.edit(
        f"🧠 IQ: `{iq}`"
    )


@bot.on(events.NewMessage(pattern=r"\.gay"))
async def gay(event):

    gay = random.randint(1, 100)

    await event.edit(
        f"🏳️‍🌈 Gay level: `{gay}%`"
    )


@bot.on(events.NewMessage(pattern=r"\.hack"))
async def hack(event):

    await event.edit(
        "💻 Hacking..."
    )

    steps = [
        "Connecting to Telegram...",
        "Bypassing security...",
        "Injecting malware...",
        "Downloading data...",
        "Done ✅"
    ]

    for step in steps:

        await asyncio.sleep(1)

        await event.edit(
            f"💻 {step}"
        )


def mention(user):

    return (
        f"[{user.first_name}]"
        f"(tg://user?id={user.id})"
    )


def sender(event):

    return (
        f"[{event.sender.first_name}]"
        f"(tg://user?id={event.sender_id})"
    )


def get_text(action, event, user):

    return (
        f"{sender(event)} "
        f"{action} "
        f"{mention(user)}"
    )


hug_gifs = [
    "🤗 обнял(а)",
    "💞 крепко обнял(а)",
    "🥰 нежно обнял(а)"
]

kiss_gifs = [
    "💋 поцеловал(а)",
    "😘 страстно поцеловал(а)",
    "😚 мило чмокнул(а)"
]

slap_gifs = [
    "👋 дал(а) пощёчину",
    "💥 ударил(а)",
    "😡 врезал(а)"
]

humiliate_text = [
    "🤡 жёстко унизил(а)",
    "💀 уничтожил(а) морально",
    "🔥 опозорил(а) перед всеми"
]

kick_text = [
    "🚪 выгнал(а)",
    "👢 пнул(а) за дверь",
    "💨 прогнал(а) прочь"
]


@bot.on(events.NewMessage(pattern=r"\.hug"))
async def hug(event):

    reply = await event.get_reply_message()

    if not reply:
        return await event.edit(
            "❌ Reply to user"
        )

    user = await reply.get_sender()

    await event.edit(
        get_text(
            random.choice(hug_gifs),
            event,
            user
        )
    )


@bot.on(events.NewMessage(pattern=r"\.kiss"))
async def kiss(event):

    reply = await event.get_reply_message()

    if not reply:
        return await event.edit(
            "❌ Reply to user"
        )

    user = await reply.get_sender()

    await event.edit(
        get_text(
            random.choice(kiss_gifs),
            event,
            user
        )
    )


@bot.on(events.NewMessage(pattern=r"\.slap"))
async def slap(event):

    reply = await event.get_reply_message()

    if not reply:
        return await event.edit(
            "❌ Reply to user"
        )

    user = await reply.get_sender()

    await event.edit(
        get_text(
            random.choice(slap_gifs),
            event,
            user
        )
    )


@bot.on(events.NewMessage(pattern=r"\.hum"))
async def hum(event):

    reply = await event.get_reply_message()

    if not reply:
        return await event.edit(
            "❌ Reply to user"
        )

    user = await reply.get_sender()

    await event.edit(
        get_text(
            random.choice(humiliate_text),
            event,
            user
        )
    )


@bot.on(events.NewMessage(pattern=r"\.kick"))
async def kick(event):

    reply = await event.get_reply_message()

    if not reply:
        return await event.edit(
            "❌ Reply to user"
        )

    user = await reply.get_sender()

    await event.edit(
        get_text(
            random.choice(kick_text),
            event,
            user
        )
    )


print("🌘 USERBOT STARTED")

while True:

    try:

        bot.start()

        bot.run_until_disconnected()

    except Exception as e:

        print(e)
