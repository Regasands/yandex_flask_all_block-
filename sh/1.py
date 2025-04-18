
import asyncio
import time


async def interview(elem):
    arg = [elem[0]] + [y / 100 for y in elem[1:]]
    i = 1
    print(f'{arg[0]} started the {i} task.')
    await asyncio.sleep(arg[1])
    print(f'{arg[0]} moved on to the defense of the {i} task.')
    await asyncio.sleep(arg[2])
    print(f'{arg[0]} completed the {i} task.')
    print(f'{arg[0]} is resting.')
    await asyncio.sleep(0.05)
    i = 2
    print(f'{arg[0]} started the {i} task.')
    await asyncio.sleep(arg[3])
    print(f'{arg[0]} moved on to the defense of the {i} task.')
    await asyncio.sleep(arg[4])
    print(f'{arg[0]} completed the {i} task.')


async def interviews(*args):
    time.time()
    await asyncio.gather(*[interview(data) for data in args])


