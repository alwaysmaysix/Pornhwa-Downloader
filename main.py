import asyncio as aio
import nest_asyncio

from bot import bot, manga_updater  # Import your bot instance and manga_updater function

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

async def async_main():
    # Placeholder for any asynchronous initializations
    pass

async def run_bot():
    print("Bot starting...")
    await aio.gather(manga_updater())  # Run manga_updater in the background
    bot.run()  # Start the bot
    print("Bot started.")

if __name__ == '__main__':
    loop = aio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(async_main())  # Run any async setup
    loop.run_until_complete(run_bot())  # Start the bot and keep it running
