import asyncio

async def api_call_1():
    await asyncio.sleep(4)
    print('api_call_1 finished')
    return 'result 1'


async def api_call_2():
    await asyncio.sleep(2)
    print('api_call_2 finished')    
    return 'result 2'

async def main():
    task1 = asyncio.create_task(api_call_1())
    task2 = asyncio.create_task(api_call_2())
    
    tasks = [task1,task2]

    for i, task in enumerate(tasks, 1):
        print(f"  Задача {i}: статус done = {task.done()}")


    for task in asyncio.as_completed(tasks):
        result = await task
        print(f"Результат: {result}")

    for i, task in enumerate(tasks, 1):
        print(f"  Задача {i}: статус done = {task.done()}")
 

asyncio.run(main())