import asyncio


async def task_a():
    print("A started")
    await asyncio.sleep(3)
    print("A finished")


async def task_b():
    print("B started")
    await asyncio.sleep(2)
    print("B finished")

async def main():
    task1 = asyncio.create_task(task_a())
    task2 = asyncio.create_task(task_b())

    await task1
    await task2

asyncio.run(main())