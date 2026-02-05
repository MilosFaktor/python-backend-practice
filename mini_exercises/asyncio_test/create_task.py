
import asyncio

# define a coroutine that simnulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay) # Simulate an I/O opertion with a sleep
    print("Fetching extra data... id:", id)
    await asyncio.sleep(delay)
    print("Data fetched id:", id)
    return {"data": "Some data", "id": id}    # Return some data


# Define another coroutine that calls the first coroutine
async def main():
    # Creates tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(2, 1))
    task2 = asyncio.create_task(fetch_data(2, 2))
    task3 = asyncio.create_task(fetch_data(2, 3))
    task4 = asyncio.create_task(fetch_data(2, 4))
    task5 = asyncio.create_task(fetch_data(2, 5))

    result1 = await task1
    print(f"Received result: {result1}")
    result2 = await task2
    print(f"Received result: {result2}")
    result3 = await task3
    print(f"Received result: {result3}")
    result4 = await task4
    print(f"Received result: {result4}")
    result5 = await task5
    print(f"Received result: {result5}")  


# Run the main coroutine
asyncio.run(main())
