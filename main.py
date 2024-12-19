from telethon import TelegramClient

api_id = '20589225'  # o'z API ID'ingiz
api_hash = 'ce33d7600913b9c4a5baa3e87021d7de'  # o'z API hash'ingiz
phone_number = '+998996032141'  # o'z telefon raqamingiz

client = TelegramClient('anon', api_id, api_hash)

async def main():
    await client.start(phone_number)  # Telefon raqamini to'g'ridan-to'g'ri kiriting
    print("Dastur ishga tushmoqda...")
    # keyingi kodni yozing

with client:
    client.loop.run_until_complete(main())
