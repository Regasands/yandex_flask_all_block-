import asyncio
import math


station = []


a = input()
while a != '':
    a = a.split()
    station.append({'during': float(a[0]) / 100, 'drived': float(a[1]) / 100})
    a = input()

gifts = {}
a = input()
while a != '':
    a = a.split()
    gifts[a[0]] = {
        'time_chose': float(a[1]) / 100, 'pac': float(a[2]) / 100 
    }
    a = input()

sorted_list = sorted(gifts, key=lambda x: gifts[x]['pac'] + gifts[x]['time_chose'], reverse=True)

print(sorted_list)
async def buy_gift(stop_number, avalibale_gifts):
    if stop_number == 'E':
        time_limit = math.inf
    else:
        print(f'Buying gifts at {stop_number + 1} stop')
        time_limit = station[stop_number]['during']
    time = 0
    task = []
    i = 0
    while time <= time_limit and avalibale_gifts:
        time_chose, pac = gifts[avalibale_gifts[i]]['time_chose'], gifts[avalibale_gifts[i]]['pac']
        if round(time + pac + time_chose, 3) > time_limit:
            i += 1
            if i >= len(avalibale_gifts):
                break
            continue
        time += time_chose

        print(f'Buy {avalibale_gifts[i]}')
        await asyncio.sleep(time_chose)

        task.append(asyncio.create_task(pask_gift(avalibale_gifts[i], pac)))
        avalibale_gifts.pop(i)
        i -= 1 if i > 0 else 0

    await asyncio.gather(*task)
    if stop_number != 'E':
        print(f"Arrive from {stop_number + 1} stop")
    return avalibale_gifts


async def pask_gift(name, delay):
    await asyncio.sleep(delay)
    print(f"Got {name}")


async def main():
    remain = sorted_list.copy()

    for i in range(len(station)):
        remain = await buy_gift(i, remain)
        await asyncio.sleep(station[i]['drived'])
    if remain:
        print('Buying gifts after arrival')
        await buy_gift('E', remain)

if __name__ == '__main__':
    asyncio.run(main())
