import asyncio

"""
GATHER IS NOT SO GOOD AT ERROR HANDLING 
"""


async def fetch_data(id, delay):
    print(f"Coroutine {id} startinf to fetch data.")
    await asyncio.sleep(delay)
    return {"id": id, "data": f"some data from coroutine {id}"}


async def main():
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3),
    )
    for result in results:
        print(f"Received result: {result}")


asyncio.run(main())
