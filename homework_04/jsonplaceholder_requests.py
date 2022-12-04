"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def fetch_json(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            print(resp.status)
            return await resp.json()


async def users_get():
    return await fetch_json(USERS_DATA_URL)


async def posts_get():
    return await fetch_json(POSTS_DATA_URL)