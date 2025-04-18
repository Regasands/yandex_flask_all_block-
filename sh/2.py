
import asyncio
import time

    
async def interview(elems):
    for elem in elems:
        print(f'{elem[0]} started the 1 task.')
    for elem in elems:
        print(f'{elem[0]} started the 2 task.')


async def interiew_2(elem):
    arg = [elem[0]] + [y / 100 for y in elem[1:]]
    await asyncio.sleep(arg[1])
    print(f'{arg[0]} moved on to the defense of the 1 task.')
    await asyncio.sleep(arg[2])
    print(f'{arg[0]} completed the 1 task.')
    await asyncio.sleep(0.05)
    await asyncio.sleep(arg[3])
    print(f'{arg[0]} moved on to the defense of the 2 task.')
    await asyncio.sleep(arg[4])
    print(f'{arg[0]} completed the 2 task.')
    

async def interviews_2(*args):
    time.time()
    await interview(args)
    await asyncio.gather(*[interiew_2(data) for data in args])

