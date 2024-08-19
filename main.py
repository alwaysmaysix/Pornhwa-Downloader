import asyncio as aio
import nest_asyncio

from bot import bot, manga_updater
# from models import DB  # Comment out or remove if not using DB

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

async def async_main():
    # db = DB()  # Comment out or remove if not using DB
    # await db.connect()  # Comment out or remove if not using DB
    aio.create_task(manga_updater())
    await bot.run()  # Run the bot asynchronously

if __name__ == '__main__':
    loop = aio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(async_main())
