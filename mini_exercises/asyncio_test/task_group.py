import asyncio

"""
CANCELS IF ANY OF THE TASKS FAIL DURING THE EXECUTION OF TASKGROUP
"""


async def fetch_data(id, delay):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(delay)
    return {"id": id, "data": f"some data from coroutine {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, delay in enumerate([3, 1, 2], start=1):
            task = tg.create_task(fetch_data(i, delay))
            tasks.append(task)

    results = [task.result() for task in tasks]
    for result in results:
        print(f"Received result: {result}")


asyncio.run(main())
