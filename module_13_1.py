
import asyncio
import random

async def start_strongman(name, power):
    await asyncio.sleep(2)  # simulate waiting for the strength to be ready
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(random.randint(1, 6) / power)
        print(f"Силач {name} поднял шар {i}")
        if i == power:
            break
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    tasks = []
    tasks.append(asyncio.create_task(start_strongman('Pasha', 3)))
    tasks.append( asyncio.create_task(start_strongman('Denis', 4)))
    tasks.append( asyncio.create_task(start_strongman('Apollon', 5)))

    for task in tasks:
        await task


asyncio.run(start_tournament())




