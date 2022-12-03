import asyncio
import requests
import time


async def requests_first(a):
    a = requests.get('https://web.telegram.org')
    print(f"Read {len(a.content)} from {a.url} from coroutine {n}")


async def requests_second(a):
    a = requests.get('https://ya.ru')
    print(f"Read {len(a.content)} from {a.url} from coroutine {n} ")


async def requests_third(a):
    a = requests.get('https://vk.com')
    print(f"Read {len(a.content)} from {a.url} from coroutine {n}")


async def main():
    await asyncio.gather(requests_first(1), requests_second(2), requests_third(3))


counter = time.perf_counter()
await main()
elapsed = time.perf_counter() - counter
print(f"The program executed in {elapsed:0.2f} seconds.")
