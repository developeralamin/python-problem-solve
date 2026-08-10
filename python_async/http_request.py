#real I/O network
import asyncio
import httpx

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/users/1')

        return response.json()

async def main():
    user = await fetch_data()
    print(user) 

asyncio.run(main())

