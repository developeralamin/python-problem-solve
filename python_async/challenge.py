import asyncio

async def get_user():
    await asyncio.sleep(2)
    print("Get users After 2 seconds")

async def get_courses():
    await asyncio.sleep(3)
    print("Get course after 3 seconds")

async def get_posts():
    await asyncio.sleep(1)
    print("Get posts after 1 seconds")

async def main():
    await asyncio.gather(get_user(), get_courses(), get_posts())

# run 
asyncio.run(main())
