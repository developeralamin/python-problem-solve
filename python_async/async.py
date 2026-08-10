import asyncio


def test():
    print("hello")

async def task_a():
    print("Task1")
    await asyncio.sleep(5)
    print("After 5 seconds  ")


async def task_b():
    print("Task b")
    await asyncio.sleep(5)
    print("After 5 seconds in task b")


def test_2():
    print("Task 2")

async def main():
    await task_a()
    await task_b()
test_2()
asyncio.run(main())

