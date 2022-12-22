"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from models import engine, Base, User, Post, Session
from jsonplaceholder_requests import users_get, posts_get


async def create_users(data, session: AsyncSession):
    for item in data:
        user = User(id=item.get("id"), name=item.get("name"), username=item.get("username"), email=item.get("email"))
        session.add(user)
    await session.commit()


async def create_posts(data, session: AsyncSession):
    for item in data:
        post = Post(id=item.get("id"), user_id=item.get("userId"), title=item.get("title"), body=item.get("body"))
        session.add(post)
    await session.commit()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await asyncio.gather(
        users_get(),
        posts_get(),
    )
    async with Session() as session:
        await create_users(users_data, session)
        await create_posts(posts_data, session)
    await session.close()


def main():
    asyncio.run(async_main())



if __name__ == "__main__":
    main()
