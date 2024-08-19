import asyncio as aio
import nest_asyncio

from bot import bot, manga_updater
# from models import DB  # Comment out or remove if not using DB

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

async def async_main():
    # db = DB()  # Comment out or remove if not using DB
    # await db.connect()  # Comment out or remove if not using DB
    pass  # Placeholder if needed, you can remove it if there's nothing else to execute here

async def run_bot():
    await bot.start()  # Assuming 'bot' has a 'start' method
    print("Bot started.")
    try:
        await aio.Event().wait()  # Keeps the bot running
    finally:
        await bot.stop()  # Assuming 'bot' has a 'stop' method
        print("Bot stopped.")

if __name__ == '__main__':
    aio.run(async_main())  # Runs the async_main function
    aio.create_task(manga_updater())  # Starts the manga_updater as a background task
    aio.run(run_bot())  # Runs the bot in the event loop
