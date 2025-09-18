import asyncio

from game import Game

async def main():
    await Game().run()


asyncio.run(main())
